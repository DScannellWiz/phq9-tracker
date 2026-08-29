import importlib
import os
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import Mock


project_root = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(project_root / "src"))
app = importlib.import_module("phq9_tracker.app")


class ValueStub:
    def __init__(self, value):
        self.value = value

    def get(self):
        return self.value


def phq_entry(entry_date: str, item9: int) -> app.AssessmentEntryRow:
    items = [0] * 8 + [item9]
    return app.AssessmentEntryRow(
        1,
        "phq9",
        entry_date,
        items,
        item9,
        app.severity_for_score(item9),
        "",
    )


class ChartAccessibilityTests(unittest.TestCase):
    def test_callout_shows_exact_date_series_and_score(self):
        point = app.ChartPoint(100, 80, "2026-08-24", "PHQ-9", 7, "#2563EB")

        self.assertEqual(app.chart_point_callout_text(point), "2026-08-24  |  PHQ-9: 7")
        self.assertIn("hover or click a point", app.CHART_INTERACTION_HELP)
        self.assertIn("Left/Right", app.CHART_INTERACTION_HELP)

    def test_nearest_point_uses_forgiving_but_bounded_hit_target(self):
        points = [
            app.ChartPoint(100, 80, "2026-08-24", "PHQ-9", 7, "#2563EB"),
            app.ChartPoint(160, 40, "2026-08-25", "PHQ-9", 4, "#2563EB"),
        ]

        self.assertEqual(app.nearest_chart_point(points, 106, 85), points[0])
        self.assertIsNone(app.nearest_chart_point(points, 125, 105))


class Item9ConversationStarterTests(unittest.TestCase):
    def test_recent_above_zero_is_highlighted_with_coverage(self):
        entries = [
            phq_entry("2026-08-01", 2),
            phq_entry("2026-08-20", 0),
            phq_entry("2026-08-24", 1),
        ]

        context = app.item9_context(entries, "2026-08-28")
        summary = app.item9_context_summary(context)
        prompt = app.item9_conversation_starter(context)

        self.assertEqual(context.recent_start, "2026-08-15")
        self.assertEqual(context.recent_checkins, 2)
        self.assertEqual(context.recent_above_zero, 1)
        self.assertIn("most recent 14-day window", summary)
        self.assertIn("2 of 14 calendar days", summary)
        self.assertIn("1 of 2 recorded check-ins", prompt)
        self.assertIn("missing days are missing information", prompt)

    def test_older_above_zero_is_neutral_historical_context(self):
        entries = [
            phq_entry("2026-07-10", 1),
            phq_entry("2026-08-18", 0),
            phq_entry("2026-08-25", 0),
        ]

        context = app.item9_context(entries, "2026-08-28")
        summary = app.item9_context_summary(context)
        prompt = app.item9_conversation_starter(context)

        self.assertFalse(context.has_recent_above_zero)
        self.assertEqual(context.latest_historical_date, "2026-07-10")
        self.assertIn("neutral historical context", summary)
        self.assertIn("does not establish current risk", summary)
        self.assertIn("does not indicate current risk", prompt)
        self.assertNotIn("support is needed now", prompt)

    def test_prompt_is_omitted_when_no_above_zero_response_exists(self):
        context = app.item9_context(
            [phq_entry("2026-08-18", 0), phq_entry("2026-08-25", 0)],
            "2026-08-28",
        )

        self.assertIsNone(app.item9_context_summary(context))
        self.assertIsNone(app.item9_conversation_starter(context))


class SafeDateLoadingTests(unittest.TestCase):
    def test_checkin_date_auto_loads_when_no_unsaved_changes_exist(self):
        target = type("CheckinAutoLoadStub", (), {})()
        target.date_var = ValueStub("2026-08-20")
        target._loaded_checkin_date = "2026-08-19"
        target.has_unsaved_checkin_changes = Mock(return_value=False)
        target.load_checkin_date = Mock()
        target.checkin_mode = Mock()

        app.PHQ9App.auto_load_checkin_date_if_safe(target)

        target.load_checkin_date.assert_called_once_with(confirm_unsaved=False)

    def test_checkin_date_does_not_auto_load_over_unsaved_changes(self):
        target = type("CheckinAutoLoadStub", (), {})()
        target.date_var = ValueStub("2026-08-20")
        target._loaded_checkin_date = "2026-08-19"
        target.has_unsaved_checkin_changes = Mock(return_value=True)
        target.load_checkin_date = Mock()
        target.checkin_mode = Mock()

        app.PHQ9App.auto_load_checkin_date_if_safe(target)

        target.load_checkin_date.assert_not_called()
        target.checkin_mode.config.assert_called_once()

    def test_history_date_auto_loads_when_no_unsaved_changes_exist(self):
        target = type("HistoryAutoLoadStub", (), {})()
        target.history_date = ValueStub("2026-08-20")
        target._loaded_history_date = "2026-08-19"
        target.has_unsaved_history_changes = Mock(return_value=False)
        target.load_history_date = Mock()
        target.history_status = Mock()

        app.PHQ9App.auto_load_history_date_if_safe(target)

        target.load_history_date.assert_called_once_with(confirm_unsaved=False)


class Item9ReportIntegrationTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(ignore_cleanup_errors=True)
        self.previous_db_path = app.DB_PATH
        self.previous_env_path = os.environ.get("PHQ9_TRACKER_DB_PATH")
        self.db_path = Path(self.tmp.name) / "fictional.sqlite"
        os.environ["PHQ9_TRACKER_DB_PATH"] = str(self.db_path)
        app.DB_PATH = self.db_path
        app.init_db()

    def tearDown(self):
        app.DB_PATH = self.previous_db_path
        if self.previous_env_path is None:
            os.environ.pop("PHQ9_TRACKER_DB_PATH", None)
        else:
            os.environ["PHQ9_TRACKER_DB_PATH"] = self.previous_env_path
        self.tmp.cleanup()

    def test_generated_report_keeps_older_item9_response_historical(self):
        if app.colors is None or app.PILImage is None:
            self.skipTest("PDF report generation requires reportlab and Pillow.")
        try:
            from pypdf import PdfReader
        except ImportError:
            self.skipTest("PDF structure validation requires pypdf.")

        app.upsert_entry("2026-07-10", [0] * 8 + [1])
        app.upsert_entry("2026-08-20", [0] * 9)
        app.upsert_entry("2026-08-25", [0] * 9)
        pdf_path = Path(self.tmp.name) / "historical-item9.pdf"

        app.generate_report("2026-07-10", "2026-08-28", str(pdf_path))

        text = " ".join(
            " ".join(page.extract_text() or "" for page in PdfReader(str(pdf_path)).pages).split()
        )
        self.assertIn("PHQ-9 item 9 context", text)
        self.assertIn("neutral historical context", text)
        self.assertIn("Recent check-in coverage was 2 of 14 calendar days", text)
        self.assertIn("does not indicate current risk", text)
        self.assertNotIn("support is needed now", text)


if __name__ == "__main__":
    unittest.main()
