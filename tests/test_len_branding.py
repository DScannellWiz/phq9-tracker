from pathlib import Path
import unittest

from phq9_tracker import app


ROOT = Path(__file__).resolve().parents[1]


class LenBrandingTests(unittest.TestCase):
    def test_current_application_brand_is_len(self):
        self.assertEqual(app.APPLICATION_NAME, "Len")
        self.assertTrue(app.SCORING_EXPLANATION.startswith("Len calculates"))

    def test_current_launchers_and_installer_use_len(self):
        self.assertTrue((ROOT / "Launch Len.bat").is_file())
        self.assertFalse((ROOT / "Launch Mental Health Tracker.bat").exists())

        build_script = (ROOT / "packaging" / "build_release.ps1").read_text(encoding="utf-8")
        installer = (ROOT / "packaging" / "PHQ9Tracker.iss").read_text(encoding="utf-8")

        self.assertIn("Launch Portable Len.bat", build_script)
        self.assertIn('"Len-Portable-$ArtifactLabel"', build_script)
        self.assertIn('if ($Version -eq "0.3.0-alpha.1")', build_script)
        self.assertIn('#define MyAppName "Len"', installer)
        self.assertIn("#ifndef MyAppVersion", installer)
        self.assertNotIn("Launch Mental Health Tracker", installer)

    def test_compatibility_identifiers_are_preserved(self):
        source = (ROOT / "src" / "phq9_tracker" / "app.py").read_text(encoding="utf-8")

        self.assertIn('"PHQ9Tracker" / "phq9_tracker.sqlite"', source)
        self.assertIn("PHQ9_TRACKER_PORTABLE", source)
        self.assertIn("PHQ9_TRACKER_DB_PATH", source)


if __name__ == "__main__":
    unittest.main()
