import importlib
import os
import sys
import tempfile
import unittest
from datetime import date
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

    def set(self, value):
        self.value = value


class Iteration0071NavigationTests(unittest.TestCase):
    def test_primary_tab_order_starts_with_today_then_review_then_history(self):
        self.assertEqual(
            app.PRIMARY_TAB_ORDER[:3],
            ("Today's Check-In", "Review", "History / Manage Entries"),
        )

    def test_history_navigation_uses_calendar_rollover_and_loads_target(self):
        target = type("HistoryNavigationStub", (), {})()
        target.history_date = ValueStub("2026-01-01")
        target.confirm_discard_history_changes = Mock(return_value=True)
        target.load_history_date = Mock()

        app.PHQ9App.navigate_history_date(target, -1)

        self.assertEqual(target.history_date.get(), "2025-12-31")
        target.load_history_date.assert_called_once_with(confirm_unsaved=False)

    def test_history_navigation_preserves_unsaved_edits_when_discard_is_declined(self):
        target = type("HistoryNavigationStub", (), {})()
        target.history_date = ValueStub("2026-01-01")
        target.confirm_discard_history_changes = Mock(return_value=False)
        target.load_history_date = Mock()

        app.PHQ9App.navigate_history_date(target, -1)

        self.assertEqual(target.history_date.get(), "2026-01-01")
        target.load_history_date.assert_not_called()

    def test_unsaved_history_state_is_detected(self):
        target = type("HistoryStateStub", (), {})()
        target._history_snapshot = ("saved",)
        target.history_state = Mock(return_value=("changed",))

        self.assertTrue(app.PHQ9App.has_unsaved_history_changes(target))

    def test_future_date_is_rejected_for_direct_history_loading(self):
        with self.assertRaisesRegex(ValueError, "Future dates"):
            app.validate_nonfuture_date("2026-08-08", date(2026, 8, 7))


class Iteration0071EmptyHistoryTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(ignore_cleanup_errors=True)
        self.previous_db_path = app.DB_PATH
        self.previous_env_path = os.environ.get("PHQ9_TRACKER_DB_PATH")
        self.db_path = Path(self.tmp.name) / "synthetic.sqlite"
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

    def test_empty_date_has_calm_manage_only_status(self):
        day_data = app.fetch_day_data("2026-07-31")

        self.assertEqual(app.history_record_count(day_data), 0)
        self.assertEqual(
            app.history_status_text("2026-07-31", day_data),
            "No existing records for 2026-07-31. History can edit only dates that already contain "
            "a check-in, note, or treatment event.",
        )

    def test_existing_records_are_loaded_and_counted(self):
        app.upsert_entry("2026-07-31", [1] + [0] * 8, notes="Synthetic note", note_tag="Other")
        app.add_event("2026-07-31", "Therapy", "Synthetic event")

        day_data = app.fetch_day_data("2026-07-31")

        self.assertIn("phq9", day_data["assessments"])
        self.assertEqual(history_count := app.history_record_count(day_data), 3)
        self.assertEqual(
            app.history_status_text("2026-07-31", day_data),
            f"Showing {history_count} existing records for 2026-07-31. Edits apply only to this loaded date.",
        )


class Iteration0071ChartLayoutTests(unittest.TestCase):
    def test_responsive_chart_uses_smaller_live_width_after_resize(self):
        self.assertEqual(app.responsive_canvas_dimension(438, 520), 438)
        self.assertEqual(app.responsive_canvas_dimension(1, 520), 520)

    def test_chart_title_legend_and_plot_have_separate_vertical_bands(self):
        title_bottom = 29
        legend_top, plot_top = app.chart_vertical_positions(title_bottom)

        self.assertGreater(legend_top, title_bottom)
        self.assertGreaterEqual(plot_top, legend_top + 24)


if __name__ == "__main__":
    unittest.main()
