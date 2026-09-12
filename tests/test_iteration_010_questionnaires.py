import importlib
import os
import sys
import tempfile
import unittest
from pathlib import Path


project_root = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(project_root / "src"))
app = importlib.import_module("phq9_tracker.app")


class Iteration010QuestionnaireTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(ignore_cleanup_errors=True)
        self.db_path = Path(self.tmp.name) / "iteration010.sqlite"
        os.environ["PHQ9_TRACKER_DB_PATH"] = str(self.db_path)
        app.DB_PATH = self.db_path
        app.init_db()

    def tearDown(self):
        self.tmp.cleanup()

    def test_builtins_use_public_questionnaire_contract_and_redistributable_metadata(self):
        self.assertIs(app.QUESTIONNAIRES, app.ASSESSMENTS)
        self.assertEqual(app.QUESTIONNAIRE_ORDER, ["phq9", "gad7"])
        self.assertTrue(app.QUESTIONNAIRES["phq9"].has_item9_safety_context)
        self.assertFalse(app.QUESTIONNAIRES["gad7"].has_item9_safety_context)
        for definition in app.QUESTIONNAIRES.values():
            self.assertTrue(definition.source)
            self.assertEqual(definition.redistribution_status, "Redistributable built-in")

    def test_daily_completion_is_independent_for_each_questionnaire(self):
        entry_date = "2026-09-12"
        self.assertEqual(
            app.questionnaire_completion_status(entry_date),
            {"phq9": "Not completed", "gad7": "Not completed"},
        )
        app.upsert_assessment_entry("gad7", entry_date, [1, 0, 0, 0, 0, 0, 0])
        self.assertEqual(
            app.questionnaire_completion_status(entry_date),
            {"phq9": "Not completed", "gad7": "Complete"},
        )

    def test_selected_profile_and_workbook_omit_unselected_questionnaire(self):
        app.upsert_entry("2026-09-12", [1] * 9)
        app.upsert_assessment_entry("gad7", "2026-09-12", [2] * 7)
        profile = app.build_14_day_item_profile("2026-09-12", ["gad7"])
        self.assertEqual({row["assessment_id"] for row in profile}, {"gad7"})
        workbook = app._analysis_workbook_data(["gad7"])
        self.assertEqual({row["assessment_id"] for row in workbook["Daily Assessments"]}, {"gad7"})
        self.assertEqual(
            next(row["metadata_value"] for row in workbook["Metadata"] if row["metadata_key"] == "questionnaires_included"),
            "gad7",
        )

    def test_selection_rejects_empty_and_unknown_questionnaires(self):
        with self.assertRaisesRegex(ValueError, "at least one"):
            app.normalize_questionnaire_selection([])
        with self.assertRaisesRegex(ValueError, "Unknown questionnaire"):
            app.normalize_questionnaire_selection(["custom-not-installed"])

    def test_today_checkin_has_vertical_scrolling_and_reveals_optional_submit(self):
        source = (project_root / "src" / "phq9_tracker" / "app.py").read_text(encoding="utf-8")
        self.assertIn('self.entry_scrollbar = ttk.Scrollbar', source)
        self.assertIn('yscrollcommand=self.entry_scrollbar.set', source)
        self.assertIn('self.entry_canvas.yview_moveto(1.0)', source)
        self.assertIn('text="Save Optional Details"', source)

    def test_gad_only_pdf_generates_without_phq9_item9_section(self):
        if app.colors is None or app.PILImage is None:
            self.skipTest("PDF report generation requires reportlab and Pillow.")
        app.upsert_assessment_entry("gad7", "2026-09-12", [1] * 7)
        target = Path(self.tmp.name) / "gad-only.pdf"
        app.generate_report("2026-09-12", "2026-09-12", str(target), ["gad7"])
        self.assertTrue(target.exists())
        summary = app.overall_pattern_summary([], app.fetch_assessment_entries("gad7"), "2026-09-12", ["gad7"])
        self.assertIn("GAD-7", summary)
        self.assertNotIn("PHQ-9", summary)


if __name__ == "__main__":
    unittest.main()
