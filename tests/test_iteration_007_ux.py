import importlib
import os
import sys
import tempfile
import unittest
from datetime import date, timedelta
from pathlib import Path


project_root = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(project_root / "src"))
app = importlib.import_module("phq9_tracker.app")


def assessment_entry(entry_date: str, assessment_id: str, items: list[int]):
    severity = app.severity_for_assessment(assessment_id, sum(items))
    return app.AssessmentEntryRow(1, assessment_id, entry_date, items, sum(items), severity, "")


class Iteration007LogicTests(unittest.TestCase):
    def test_date_navigation_rolls_across_month_and_year_boundaries(self):
        today = date(2026, 8, 1)
        self.assertEqual(app.shift_calendar_date("2026-08-01", -1, today), "2026-07-31")
        self.assertEqual(app.shift_calendar_date("2026-01-01", -1, today), "2025-12-31")

    def test_date_navigation_prevents_future_checkins(self):
        with self.assertRaisesRegex(ValueError, "Future check-ins"):
            app.shift_calendar_date("2026-08-01", 1, date(2026, 8, 1))

    def test_symptom_highlight_uses_neutral_frequency_language(self):
        entries = []
        for day_number in range(1, 29):
            sleep_present = day_number in {1, 2} or day_number >= 19
            items = [0, 0, int(sleep_present), 0, 0, 0, 0, 0, 0]
            entries.append(assessment_entry(f"2026-01-{day_number:02d}", "phq9", items))

        highlights = app.symptom_highlights("phq9", entries, "2026-01-28", limit=1)

        self.assertIn("Responses related to sleep changes were recorded more often", highlights[0])
        self.assertIn("10 of 14 check-ins", highlights[0])
        self.assertNotIn("worse", highlights[0].lower())
        self.assertNotIn("caused", highlights[0].lower())

    def test_treatment_cycles_select_current_and_previous_windows(self):
        entries = [
            assessment_entry(f"2026-01-{day_number:02d}", "phq9", [1] + [0] * 8)
            for day_number in range(1, 29)
        ]
        events = [
            (1, "2026-01-05", "Ketamine infusion", "first"),
            (2, "2026-01-20", "Ketamine infusion", "second"),
        ]

        cycles = app.treatment_cycles(entries, events, "2026-01-28")

        self.assertEqual([(cycle.label, cycle.start_date, cycle.end_date) for cycle in cycles], [
            ("Current cycle", "2026-01-20", "2026-01-28"),
            ("Previous cycle", "2026-01-05", "2026-01-19"),
        ])

    def test_dependency_probe_accepts_standard_library_module(self):
        self.assertTrue(app.python_supports_modules(Path(sys.executable), ("json",)))


class Iteration007ReportTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(ignore_cleanup_errors=True)
        self.db_path = Path(self.tmp.name) / "synthetic.sqlite"
        os.environ["PHQ9_TRACKER_DB_PATH"] = str(self.db_path)
        app.DB_PATH = self.db_path
        app.init_db()

    def tearDown(self):
        self.tmp.cleanup()

    def test_conversation_report_is_compact_and_omits_duplicate_raw_tables(self):
        if app.colors is None or app.PILImage is None:
            self.skipTest("PDF report generation requires reportlab and Pillow.")
        try:
            from pypdf import PdfReader
        except ImportError:
            self.skipTest("PDF structure validation requires pypdf.")

        start_day = date(2026, 1, 1)
        for offset in range(60):
            day = (start_day + timedelta(days=offset)).isoformat()
            phq_items = [offset % 2, 1, 1 if offset >= 42 else 0, 1, 0, 0, 1, 0, 0]
            gad_items = [1, offset % 2, 1, 1 if offset >= 45 else 0, 0, 0, 0]
            has_note = offset in {5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55}
            note = "Synthetic context with enough detail to exercise wrapping in the compact timeline table." if has_note else ""
            app.upsert_entry(day, phq_items, notes=note, note_tag="Sleep")
            app.upsert_assessment_entry("gad7", day, gad_items, notes=note, note_tag="Sleep")
        app.add_event("2026-01-10", "Ketamine infusion", "Synthetic infusion")
        app.add_event("2026-02-05", "Ketamine infusion", "Synthetic infusion")
        app.add_event("2026-02-20", "Therapy", "Synthetic appointment")

        pdf_path = Path(self.tmp.name) / "discussion-report.pdf"
        csv_path = Path(self.tmp.name) / "discussion-report.csv"
        app.generate_report("2026-01-01", "2026-03-01", str(pdf_path), str(csv_path))

        reader = PdfReader(str(pdf_path))
        report_text = "\n".join(page.extract_text() or "" for page in reader.pages)
        self.assertGreaterEqual(len(reader.pages), 2)
        self.assertLessEqual(len(reader.pages), 4)
        self.assertIn("Period at a Glance", report_text)
        self.assertIn("Treatment-Cycle Observations", report_text)
        self.assertIn("Possible topics for conversation", report_text)
        self.assertNotIn("Most Recent 14-Day Symptom Responses", report_text)
        self.assertNotIn("Recent Symptom Detail", report_text)
        self.assertNotIn("Ketamine Response Review", report_text)
        self.assertIn("PHQ-9 Entries", csv_path.read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
