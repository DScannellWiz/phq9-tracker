import csv
import importlib
import os
import sys
import tempfile
import unittest
from pathlib import Path


class DataExportTests(unittest.TestCase):
    def test_export_uses_fake_temp_database_and_expected_columns(self):
        project_root = Path(__file__).resolve().parents[1]
        sys.path.insert(0, str(project_root / "src"))
        with tempfile.TemporaryDirectory(ignore_cleanup_errors=True) as tmp:
            os.environ["PHQ9_TRACKER_DB_PATH"] = str(Path(tmp) / "fake.sqlite")
            app = importlib.import_module("phq9_tracker.app")
            app.DB_PATH = Path(tmp) / "fake.sqlite"
            app.init_db()
            app.upsert_entry("2026-01-01", [0, 1, 2, 1, 0, 1, 2, 1, 0], notes="Fake note", note_tag="Other")
            app.add_event("2026-01-01", "Therapy", "Fake therapy marker")
            output = Path(tmp) / "export.csv"
            app.export_entries(str(output))
            with output.open(newline="", encoding="utf-8") as handle:
                rows = list(csv.DictReader(handle))
            self.assertEqual(len(rows), 1)
            self.assertEqual(rows[0]["PHQ-9 Total Score"], "8")
            self.assertEqual(rows[0]["Question 9 Score"], "0")
            self.assertEqual(rows[0]["GAD-7 Total Score"], "")
            self.assertEqual(rows[0]["Therapy"], "Yes")


if __name__ == "__main__":
    unittest.main()
