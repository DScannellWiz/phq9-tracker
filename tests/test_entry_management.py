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


class EntryManagementTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(ignore_cleanup_errors=True)
        self.db_path = Path(self.tmp.name) / "synthetic.sqlite"
        os.environ["PHQ9_TRACKER_DB_PATH"] = str(self.db_path)
        app.DB_PATH = self.db_path
        app.init_db()

    def tearDown(self):
        self.tmp.cleanup()

    def test_repeated_submission_updates_assessments_and_note_without_duplicates(self):
        day = "2026-06-01"
        app.upsert_entry(day, [1] * 9, notes="first note", note_tag="Work")
        app.upsert_assessment_entry("gad7", day, [1] * 7, notes="first note", note_tag="Work")
        original = app.fetch_day_data(day)
        original_ids = {key: row.id for key, row in original["assessments"].items()}

        app.upsert_entry(day, [2] * 9, notes="revised note", note_tag="Sleep")
        app.upsert_assessment_entry("gad7", day, [2] * 7, notes="revised note", note_tag="Sleep")
        app.update_daily_note(day, "revised note", "Sleep")

        revised = app.fetch_day_data(day)
        self.assertEqual({key: row.id for key, row in revised["assessments"].items()}, original_ids)
        self.assertEqual(revised["assessments"]["phq9"].total, 18)
        self.assertEqual(revised["assessments"]["gad7"].total, 14)
        self.assertEqual(revised["notes"], "revised note")
        with sqlite3.connect(self.db_path) as conn:
            self.assertEqual(conn.execute("SELECT COUNT(*) FROM assessment_entries WHERE entry_date = ?", (day,)).fetchone()[0], 2)

    def test_stable_id_assessment_edit_and_note_clear(self):
        day = "2026-06-02"
        app.upsert_entry(day, [1] * 9, notes="to edit")
        app.upsert_assessment_entry("gad7", day, [1] * 7, notes="to edit")
        rows = app.fetch_day_data(day)["assessments"]
        app.update_assessment_entry(rows["phq9"].id, "phq9", [3, 0, 0, 0, 0, 0, 0, 0, 0])
        app.update_assessment_entry(rows["gad7"].id, "gad7", [0, 1, 2, 3, 0, 1, 2])
        app.delete_daily_note(day)
        edited = app.fetch_day_data(day)
        self.assertEqual(edited["assessments"]["phq9"].id, rows["phq9"].id)
        self.assertEqual(edited["assessments"]["phq9"].total, 3)
        self.assertEqual(edited["assessments"]["gad7"].id, rows["gad7"].id)
        self.assertEqual(edited["assessments"]["gad7"].total, 9)
        self.assertEqual(edited["notes"], "")

    def test_delete_assessments_removes_legacy_phq9_and_survives_migration(self):
        day = "2026-06-03"
        app.upsert_entry(day, [1] * 9)
        app.upsert_assessment_entry("gad7", day, [1] * 7)
        rows = app.fetch_day_data(day)["assessments"]
        app.delete_assessment_entry(rows["phq9"].id, "phq9")
        app.delete_assessment_entry(rows["gad7"].id, "gad7")
        app.init_db()
        self.assertEqual(app.fetch_day_data(day)["assessments"], {})

    def test_daily_event_resubmission_is_idempotent_and_multiple_events_are_valid(self):
        day = "2026-06-04"
        therapy_id = app.upsert_daily_event(day, "Therapy", "appointment")
        self.assertEqual(app.upsert_daily_event(day, "Therapy", ""), therapy_id)
        self.assertEqual(app.fetch_events(day, day)[0][3], "appointment")
        self.assertEqual(app.upsert_daily_event(day, "Therapy", "revised appointment"), therapy_id)
        app.upsert_daily_event(day, "Ketamine infusion", "infusion")
        events = app.fetch_events(day, day)
        self.assertEqual(len(events), 2)
        self.assertEqual({event[2] for event in events}, {"Therapy", "Ketamine infusion"})
        self.assertEqual(next(event[3] for event in events if event[2] == "Therapy"), "revised appointment")

    def test_explicit_add_update_and_delete_treatment_event(self):
        day = "2026-06-05"
        first_id = app.add_event(day, "Therapy", "morning", dedupe=False)
        second_id = app.add_event(day, "Therapy", "evening", dedupe=False)
        self.assertNotEqual(first_id, second_id)
        self.assertEqual(len(app.fetch_events(day, day)), 2)
        app.update_event(second_id, day, "Support group", "evening group")
        self.assertEqual(app.fetch_events(day, day)[1][2:], ("Support group", "evening group"))
        app.delete_event(first_id)
        self.assertEqual([event[0] for event in app.fetch_events(day, day)], [second_id])


if __name__ == "__main__":
    unittest.main()
