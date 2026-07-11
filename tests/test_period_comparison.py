import sys
import unittest
from pathlib import Path


project_root = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(project_root / "src"))

from phq9_tracker.app import AssessmentEntryRow, EntryRow, compare_recent_14_day_periods, comparison_trend_text


def fake_phq_entry(entry_date: str, item_value: int) -> EntryRow:
    items = [item_value] + [0] * 8
    return EntryRow(1, entry_date, items, sum(items), "Minimal", "")


class PeriodComparisonTests(unittest.TestCase):
    def test_compares_adjacent_calendar_windows_ending_on_requested_date(self):
        entries = [
            fake_phq_entry(f"2026-01-{day:02d}", 1 if day <= 14 else 0)
            for day in range(1, 29)
        ]

        result = compare_recent_14_day_periods(entries, "phq9", "2026-01-28")

        self.assertEqual(result.previous_start, "2026-01-01")
        self.assertEqual(result.previous_end, "2026-01-14")
        self.assertEqual(result.current_start, "2026-01-15")
        self.assertEqual(result.current_end, "2026-01-28")
        self.assertEqual(result.previous.total_score, 3)
        self.assertEqual(result.current.total_score, 0)
        self.assertEqual(result.delta, -3)
        self.assertEqual(comparison_trend_text(result), "Lower by 3 points")

    def test_reports_insufficient_comparison_when_prior_period_has_no_entries(self):
        result = compare_recent_14_day_periods([fake_phq_entry("2026-01-28", 1)], "phq9", "2026-01-28")

        self.assertFalse(result.has_comparable_data)
        self.assertEqual(result.current.entries_included, 1)
        self.assertEqual(result.previous.entries_included, 0)
        self.assertEqual(comparison_trend_text(result), "Not enough data for comparison")

    def test_gad7_uses_seven_items_and_gad_severity_ranges(self):
        entries = []
        for day in range(1, 29):
            value = 1 if day >= 15 else 0
            entries.append(
                AssessmentEntryRow(1, "gad7", f"2026-01-{day:02d}", [value] * 7, value * 7, "Minimal", "")
            )

        result = compare_recent_14_day_periods(entries, "gad7", "2026-01-28")

        self.assertEqual(result.current.total_score, 21)
        self.assertEqual(result.current.severity, "Severe")
        self.assertEqual(result.previous.total_score, 0)
        self.assertEqual(comparison_trend_text(result), "Higher by 21 points")


if __name__ == "__main__":
    unittest.main()
