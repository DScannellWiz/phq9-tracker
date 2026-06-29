import sys
import unittest
from pathlib import Path


project_root = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(project_root / "src"))

from phq9_tracker.app import EntryRow, calculate_14_day_symptom_frequency_score


def fake_entry(day: int, items: list[int]) -> EntryRow:
    return EntryRow(
        id=day,
        entry_date=f"2026-01-{day:02d}",
        items=items,
        total=sum(items),
        severity="",
        notes="",
    )


class FourteenDayScoringTests(unittest.TestCase):
    def score_for_presence_days(self, days_present: int) -> int:
        entries = []
        for day in range(1, 15):
            item_value = 1 if day <= days_present else 0
            entries.append(fake_entry(day, [item_value, 0, 0, 0, 0, 0, 0, 0, 0]))
        return calculate_14_day_symptom_frequency_score(entries).item_scores[0]

    def test_all_zero_scores_for_14_days_total_zero(self):
        entries = [fake_entry(day, [0] * 9) for day in range(1, 15)]
        result = calculate_14_day_symptom_frequency_score(entries)
        self.assertEqual(result.item_counts, [0] * 9)
        self.assertEqual(result.item_scores, [0] * 9)
        self.assertEqual(result.total_score, 0)
        self.assertEqual(result.severity, "Minimal")

    def test_threshold_1_day_scores_1(self):
        self.assertEqual(self.score_for_presence_days(1), 1)

    def test_threshold_6_days_scores_1(self):
        self.assertEqual(self.score_for_presence_days(6), 1)

    def test_threshold_7_days_scores_2(self):
        self.assertEqual(self.score_for_presence_days(7), 2)

    def test_threshold_11_days_scores_2(self):
        self.assertEqual(self.score_for_presence_days(11), 2)

    def test_threshold_12_days_scores_3(self):
        self.assertEqual(self.score_for_presence_days(12), 3)

    def test_threshold_14_days_scores_3(self):
        self.assertEqual(self.score_for_presence_days(14), 3)

    def test_mixed_item_scores_produce_correct_total(self):
        entries = []
        for day in range(1, 15):
            entries.append(
                fake_entry(
                    day,
                    [
                        1 if day <= 0 else 0,
                        1 if day <= 1 else 0,
                        1 if day <= 6 else 0,
                        1 if day <= 7 else 0,
                        1 if day <= 11 else 0,
                        1 if day <= 12 else 0,
                        1 if day <= 14 else 0,
                        0,
                        1 if day in (2, 4, 6, 8, 10, 12, 14) else 0,
                    ],
                )
            )
        result = calculate_14_day_symptom_frequency_score(entries)
        self.assertEqual(result.item_scores, [0, 1, 1, 2, 2, 3, 3, 0, 2])
        self.assertEqual(result.total_score, 14)
        self.assertEqual(result.severity, "Moderate")

    def test_missing_days_count_as_no_recorded_symptom_present_day(self):
        entries = [
            fake_entry(1, [1, 0, 0, 0, 0, 0, 0, 0, 0]),
            fake_entry(7, [1, 0, 0, 0, 0, 0, 0, 0, 0]),
            fake_entry(14, [1, 0, 0, 0, 0, 0, 0, 0, 0]),
        ]
        result = calculate_14_day_symptom_frequency_score(entries)
        self.assertEqual(result.entries_included, 3)
        self.assertEqual(result.item_counts[0], 3)
        self.assertEqual(result.item_scores[0], 1)
        self.assertEqual(result.start_date, "2026-01-01")
        self.assertEqual(result.end_date, "2026-01-14")


if __name__ == "__main__":
    unittest.main()
