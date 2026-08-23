import importlib
import os
import sqlite3
import sys
import tempfile
import unittest
from pathlib import Path


project_root = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(project_root / "src"))

app = importlib.import_module("phq9_tracker.app")


class MultiAssessmentTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(ignore_cleanup_errors=True)
        self.db_path = Path(self.tmp.name) / "fake.sqlite"
        os.environ["PHQ9_TRACKER_DB_PATH"] = str(self.db_path)
        app.DB_PATH = self.db_path
        app.init_db()

    def tearDown(self):
        self.tmp.cleanup()

    def test_gad7_scoring_and_14_day_frequency(self):
        self.assertEqual(app.gad7_severity_for_score(4), "Minimal")
        self.assertEqual(app.gad7_severity_for_score(9), "Mild")
        self.assertEqual(app.gad7_severity_for_score(14), "Moderate")
        self.assertEqual(app.gad7_severity_for_score(15), "Severe")
        for day in range(1, 15):
            app.upsert_assessment_entry("gad7", f"2026-01-{day:02d}", [1, 0, 1, 0, 1, 0, 1])
        rows = app.fetch_assessment_entries("gad7")
        score = app.calculate_14_day_symptom_frequency_score(rows, 7, "gad7")
        self.assertEqual(score.item_scores, [3, 0, 3, 0, 3, 0, 3])
        self.assertEqual(score.total_score, 12)
        self.assertEqual(score.severity, "Moderate")

    def test_legacy_phq9_rows_migrate_to_assessment_entries(self):
        with sqlite3.connect(self.db_path) as conn:
            conn.execute(
                """
                INSERT INTO phq9_entries (
                    entry_date, item1, item2, item3, item4, item5, item6, item7, item8, item9,
                    total, severity, notes, note_tag, source
                )
                VALUES ('2026-02-01', 1, 1, 1, 1, 1, 1, 1, 1, 1, 9, 'Mild', 'legacy note', 'Work', 'manual')
                """
            )
            conn.commit()
        app.init_db()
        rows = app.fetch_assessment_entries("phq9")
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0].total, 9)
        self.assertEqual(rows[0].notes, "legacy note")

    def test_combined_report_writes_pdf_without_companion_csv(self):
        if app.colors is None or app.PILImage is None:
            self.skipTest("PDF report generation requires reportlab and Pillow.")
        app.upsert_entry("2026-04-01", [0, 1, 1, 1, 0, 1, 1, 1, 0], notes="PHQ note")
        app.upsert_assessment_entry("gad7", "2026-04-01", [1, 1, 1, 1, 1, 0, 0], notes="GAD note")
        app.add_event("2026-04-01", "Medication Start", "Fake medication marker")
        pdf_path = Path(self.tmp.name) / "report.pdf"
        app.generate_report("2026-04-01", "2026-04-01", str(pdf_path))
        self.assertTrue(pdf_path.exists())
        self.assertFalse(pdf_path.with_suffix(".csv").exists())


if __name__ == "__main__":
    unittest.main()
