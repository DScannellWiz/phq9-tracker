import importlib
import os
import sys
import tempfile
import unittest
from pathlib import Path


project_root = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(project_root / "src"))
app = importlib.import_module("phq9_tracker.app")


class Iteration008ReviewExportTests(unittest.TestCase):
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

    def test_review_has_approved_fifth_output_management_action_and_no_clinician_report_tab(self):
        self.assertEqual(
            app.REVIEW_ACTION_LABELS,
            ("Refresh", "Import Spreadsheet", "Generate PDF", "Analysis Workbook", "Open Reports Folder"),
        )
        self.assertNotIn("Clinician Report", app.PRIMARY_TAB_ORDER)

    def test_full_history_report_range_is_recalculated_from_assessments(self):
        with self.assertRaisesRegex(ValueError, "No check-ins"):
            app.available_report_date_range()

        app.upsert_assessment_entry("gad7", "2026-02-05", [1, 0, 0, 0, 0, 0, 0])
        app.upsert_entry("2026-01-10", [1, 0, 0, 0, 0, 0, 0, 0, 0])
        self.assertEqual(app.available_report_date_range(), ("2026-01-10", "2026-02-05"))

        app.upsert_entry("2026-03-12", [0, 1, 0, 0, 0, 0, 0, 0, 0])
        self.assertEqual(app.available_report_date_range(), ("2026-01-10", "2026-03-12"))

    def test_legacy_combined_export_function_is_removed(self):
        self.assertFalse(hasattr(app, "export_entries"))


if __name__ == "__main__":
    unittest.main()
