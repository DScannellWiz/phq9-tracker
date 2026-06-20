import argparse
import csv
import os
import sqlite3
import subprocess
import sys
import tempfile
from dataclasses import dataclass
from datetime import date, datetime, timedelta
from pathlib import Path
from tkinter import (
    BOTH,
    BOTTOM,
    END,
    LEFT,
    RIGHT,
    TOP,
    Button,
    Canvas,
    Checkbutton,
    Entry,
    Frame,
    IntVar,
    Label,
    LabelFrame,
    Menu,
    StringVar,
    Text,
    Tk,
    Toplevel,
    filedialog,
    messagebox,
    ttk,
)

try:
    import pandas as pd
except Exception:
    pd = None

try:
    from openpyxl import load_workbook
except Exception:
    load_workbook = None

try:
    from reportlab.lib import colors
    from reportlab.lib.pagesizes import letter
    from reportlab.lib.styles import getSampleStyleSheet
    from reportlab.lib.units import inch
    from reportlab.platypus import (
        Image,
        PageBreak,
        Paragraph,
        SimpleDocTemplate,
        Spacer,
        Table,
        TableStyle,
    )
except Exception:
    colors = None
    inch = 72
    Image = None
    PageBreak = None
    Paragraph = None
    SimpleDocTemplate = None
    Spacer = None
    Table = None
    TableStyle = None

try:
    from PIL import Image as PILImage
    from PIL import ImageDraw, ImageFont
except Exception:
    PILImage = None


APP_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = APP_DIR.parents[1] if APP_DIR.parent.name == "src" else APP_DIR.parent
DATA_DIR = PROJECT_ROOT / "data"
EXPORTS_DIR = PROJECT_ROOT / "exports"
REPORTS_DIR = PROJECT_ROOT / "reports"


def default_db_path() -> Path:
    explicit = os.environ.get("PHQ9_TRACKER_DB_PATH")
    if explicit:
        return Path(explicit)
    if getattr(sys, "frozen", False):
        if os.environ.get("PHQ9_TRACKER_PORTABLE") == "1":
            return Path(sys.executable).resolve().parent / "phq9_tracker.sqlite"
        local_app_data = os.environ.get("LOCALAPPDATA")
        if local_app_data:
            return Path(local_app_data) / "PHQ9Tracker" / "phq9_tracker.sqlite"
    return DATA_DIR / "phq9_tracker.sqlite"


DB_PATH = default_db_path()
BUNDLED_PYTHON = Path(os.environ["PHQ9_TRACKER_BUNDLED_PYTHON"]) if os.environ.get("PHQ9_TRACKER_BUNDLED_PYTHON") else None
DISCLAIMER = "This report is for discussion with a licensed clinician and is not a diagnosis."

ITEM_LABELS = [
    "Little interest or pleasure in doing things",
    "Feeling down, depressed, or hopeless",
    "Sleep changes",
    "Low energy",
    "Appetite changes",
    "Feeling bad about yourself",
    "Trouble concentrating",
    "Moving/speaking slowly or being restless",
    "Thoughts of self-harm",
]

SEVERITY_ORDER = {
    "Minimal": 0,
    "Mild": 1,
    "Moderate": 2,
    "Moderately severe": 3,
    "Severe": 4,
}


@dataclass
class EntryRow:
    id: int
    entry_date: str
    items: list[int]
    total: int
    severity: str
    notes: str
    note_tag: str = ""


def severity_for_score(score: int) -> str:
    if score <= 4:
        return "Minimal"
    if score <= 9:
        return "Mild"
    if score <= 14:
        return "Moderate"
    if score <= 19:
        return "Moderately severe"
    return "Severe"


def parse_date(value) -> str | None:
    if value is None or value == "":
        return None
    if hasattr(value, "date"):
        return value.date().isoformat()
    text = str(value).strip()
    if not text or text.lower() == "nan":
        return None
    for fmt in ("%Y-%m-%d", "%m/%d/%Y", "%m/%d/%y", "%d-%m-%Y"):
        try:
            return datetime.strptime(text[:10], fmt).date().isoformat()
        except ValueError:
            pass
    try:
        return datetime.fromisoformat(text).date().isoformat()
    except ValueError:
        return None


def init_db(db_path: Path = DB_PATH) -> None:
    db_path.parent.mkdir(parents=True, exist_ok=True)
    with sqlite3.connect(db_path) as conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS phq9_entries (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                entry_date TEXT NOT NULL UNIQUE,
                item1 INTEGER NOT NULL,
                item2 INTEGER NOT NULL,
                item3 INTEGER NOT NULL,
                item4 INTEGER NOT NULL,
                item5 INTEGER NOT NULL,
                item6 INTEGER NOT NULL,
                item7 INTEGER NOT NULL,
                item8 INTEGER NOT NULL,
                item9 INTEGER NOT NULL,
                total INTEGER NOT NULL,
                severity TEXT NOT NULL,
                notes TEXT DEFAULT '',
                note_tag TEXT DEFAULT '',
                source TEXT DEFAULT 'manual',
                created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
                updated_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
            )
            """
        )
        existing_columns = {row[1] for row in conn.execute("PRAGMA table_info(phq9_entries)").fetchall()}
        if "note_tag" not in existing_columns:
            conn.execute("ALTER TABLE phq9_entries ADD COLUMN note_tag TEXT DEFAULT ''")
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS treatment_events (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                event_date TEXT NOT NULL,
                event_type TEXT NOT NULL,
                description TEXT DEFAULT '',
                created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
            )
            """
        )
        conn.commit()


def upsert_entry(entry_date: str, items: list[int], notes: str = "", source: str = "manual", note_tag: str = "") -> None:
    total = sum(items)
    severity = severity_for_score(total)
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute(
            """
            INSERT INTO phq9_entries (
                entry_date, item1, item2, item3, item4, item5, item6, item7, item8, item9,
                total, severity, notes, note_tag, source
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ON CONFLICT(entry_date) DO UPDATE SET
                item1=excluded.item1,
                item2=excluded.item2,
                item3=excluded.item3,
                item4=excluded.item4,
                item5=excluded.item5,
                item6=excluded.item6,
                item7=excluded.item7,
                item8=excluded.item8,
                item9=excluded.item9,
                total=excluded.total,
                severity=excluded.severity,
                notes=CASE
                    WHEN excluded.notes != '' THEN excluded.notes
                    ELSE phq9_entries.notes
                END,
                note_tag=CASE
                    WHEN excluded.note_tag != '' THEN excluded.note_tag
                    ELSE phq9_entries.note_tag
                END,
                source=excluded.source,
                updated_at=CURRENT_TIMESTAMP
            """,
            (entry_date, *items, total, severity, notes or "", note_tag or "", source),
        )
        conn.commit()


def fetch_entries(start: str | None = None, end: str | None = None, limit: int | None = None) -> list[EntryRow]:
    clauses = []
    params = []
    if start:
        clauses.append("entry_date >= ?")
        params.append(start)
    if end:
        clauses.append("entry_date <= ?")
        params.append(end)
    where = "WHERE " + " AND ".join(clauses) if clauses else ""
    limit_sql = f"LIMIT {int(limit)}" if limit else ""
    sql = f"""
        SELECT id, entry_date, item1, item2, item3, item4, item5, item6, item7, item8, item9,
               total, severity, COALESCE(notes, ''), COALESCE(note_tag, '')
        FROM phq9_entries
        {where}
        ORDER BY entry_date ASC
        {limit_sql}
    """
    with sqlite3.connect(DB_PATH) as conn:
        rows = conn.execute(sql, params).fetchall()
    return [
        EntryRow(
            id=row[0],
            entry_date=row[1],
            items=[int(v) for v in row[2:11]],
            total=int(row[11]),
            severity=row[12],
            notes=row[13] or "",
            note_tag=row[14] or "",
        )
        for row in rows
    ]


def fetch_recent_entries(days: int = 14) -> list[EntryRow]:
    with sqlite3.connect(DB_PATH) as conn:
        rows = conn.execute(
            """
            SELECT id, entry_date, item1, item2, item3, item4, item5, item6, item7, item8, item9,
                   total, severity, COALESCE(notes, ''), COALESCE(note_tag, '')
            FROM phq9_entries
            ORDER BY entry_date DESC
            LIMIT ?
            """,
            (days,),
        ).fetchall()
    rows.reverse()
    return [
        EntryRow(row[0], row[1], [int(v) for v in row[2:11]], int(row[11]), row[12], row[13] or "", row[14] or "")
        for row in rows
    ]


def fetch_events(start: str | None = None, end: str | None = None) -> list[tuple[int, str, str, str]]:
    clauses = []
    params = []
    if start:
        clauses.append("event_date >= ?")
        params.append(start)
    if end:
        clauses.append("event_date <= ?")
        params.append(end)
    where = "WHERE " + " AND ".join(clauses) if clauses else ""
    with sqlite3.connect(DB_PATH) as conn:
        return conn.execute(
            f"""
            SELECT id, event_date, event_type, COALESCE(description, '')
            FROM treatment_events
            {where}
            ORDER BY event_date ASC, id ASC
            """,
            params,
        ).fetchall()


def import_spreadsheet(path: str) -> int:
    if load_workbook is None:
        raise RuntimeError("The openpyxl package is required for Excel import.")
    workbook = load_workbook(path, read_only=True, data_only=True)
    required = {"date", *(f"item {i}" for i in range(1, 10))}
    target = None
    headers = None
    for sheet in workbook.worksheets:
        first_row = next(sheet.iter_rows(min_row=1, max_row=1, values_only=True), None)
        if not first_row:
            continue
        names = {str(c).strip().lower() for c in first_row if c is not None}
        if required.issubset(names):
            target = sheet
            headers = [str(c).strip() if c is not None else "" for c in first_row]
            break
    if target is None or headers is None:
        raise ValueError("No sheet was found with Date and Item 1 through Item 9 columns.")

    col_index = {name.lower(): idx for idx, name in enumerate(headers)}
    count = 0
    blank_streak = 0
    for row in target.iter_rows(min_row=2, values_only=True):
        raw_date = row[col_index["date"]] if col_index["date"] < len(row) else None
        entry_date = parse_date(raw_date)
        if not entry_date:
            blank_streak += 1
            if blank_streak >= 50:
                break
            continue
        blank_streak = 0
        items = []
        for i in range(1, 10):
            idx = col_index[f"item {i}"]
            value = row[idx] if idx < len(row) else None
            if value is None or str(value).strip().lower() == "nan":
                items = []
                break
            score = int(value)
            if score < 0 or score > 3:
                raise ValueError(f"Item {i} on {entry_date} has value {score}; expected 0-3.")
            items.append(score)
        if len(items) != 9:
            continue
        notes = ""
        if "notes" in col_index and col_index["notes"] < len(row) and row[col_index["notes"]]:
            notes = str(row[col_index["notes"]])
        note_tag = ""
        if "note tag" in col_index and col_index["note tag"] < len(row) and row[col_index["note tag"]]:
            note_tag = str(row[col_index["note tag"]])
        upsert_entry(
            entry_date,
            items,
            notes=notes if notes.lower() != "nan" else "",
            source="spreadsheet",
            note_tag=note_tag if note_tag.lower() != "nan" else "",
        )
        for event_name in ("Ketamine", "Therapy"):
            key = event_name.lower()
            if key in col_index:
                value = row[col_index[key]] if col_index[key] < len(row) else None
                if bool(value) and str(value).lower() not in ("nan", "false", "0"):
                    add_event(entry_date, event_name, f"{event_name} marked in imported spreadsheet", dedupe=True)
        count += 1
    workbook.close()
    return count


def add_event(event_date: str, event_type: str, description: str = "", dedupe: bool = False) -> None:
    with sqlite3.connect(DB_PATH) as conn:
        if dedupe:
            found = conn.execute(
                """
                SELECT id FROM treatment_events
                WHERE event_date = ? AND event_type = ? AND description = ?
                """,
                (event_date, event_type, description),
            ).fetchone()
            if found:
                return
        conn.execute(
            "INSERT INTO treatment_events (event_date, event_type, description) VALUES (?, ?, ?)",
            (event_date, event_type, description),
        )
        conn.commit()


def export_entries(path: str) -> None:
    rows = fetch_entries()
    event_map: dict[str, set[str]] = {}
    for _, event_date, event_type, _desc in fetch_events():
        event_map.setdefault(event_date, set()).add(normalize_event_type(event_type))
    data = []
    for row in rows:
        event_types = event_map.get(row.entry_date, set())
        record = {
            "Date": row.entry_date,
            "PHQ-9 Total Score": row.total,
            "Severity": row.severity,
        }
        for idx, score in enumerate(row.items, start=1):
            record[f"Item {idx}"] = score
        record["Question 9 Score"] = row.items[8]
        record["Notes"] = row.notes
        record["Tags"] = row.note_tag
        record["Ketamine"] = "Yes" if "Ketamine" in event_types else "No"
        record["Therapy"] = "Yes" if "Therapy" in event_types else "No"
        record["Medication Change"] = "Yes" if any(event.startswith("Medication") for event in event_types) else "No"
        data.append(record)
    fieldnames = [
        "Date",
        "PHQ-9 Total Score",
        "Severity",
        *(f"Item {i}" for i in range(1, 10)),
        "Question 9 Score",
        "Notes",
        "Tags",
        "Ketamine",
        "Therapy",
        "Medication Change",
    ]
    if path.lower().endswith(".xlsx"):
        if pd is None:
            raise RuntimeError("Excel export requires pandas/openpyxl.")
        with pd.ExcelWriter(path, engine="openpyxl") as writer:
            pd.DataFrame(data, columns=fieldnames).to_excel(writer, index=False, sheet_name="PHQ-9 Data Export")
    else:
        with open(path, "w", newline="", encoding="utf-8") as handle:
            writer = csv.DictWriter(handle, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)


def run_bundled_cli(args: list[str]) -> None:
    if BUNDLED_PYTHON is None or not BUNDLED_PYTHON.exists():
        raise RuntimeError("Set PHQ9_TRACKER_BUNDLED_PYTHON or use a Python environment with openpyxl, reportlab, Pillow, and pandas installed.")
    command = [str(BUNDLED_PYTHON), str(Path(__file__).resolve()), *args]
    result = subprocess.run(command, capture_output=True, text=True)
    if result.returncode != 0:
        raise RuntimeError(result.stderr.strip() or result.stdout.strip() or "Bundled command failed.")


def score_change_flags(entries: list[EntryRow]) -> list[str]:
    flags = []
    prior = None
    for row in entries:
        pieces = []
        if prior:
            delta = row.total - prior.total
            if delta > 0:
                pieces.append(f"score increased by {delta}")
            if SEVERITY_ORDER[row.severity] > SEVERITY_ORDER[prior.severity]:
                pieces.append(f"severity changed from {prior.severity} to {row.severity}")
        flags.append("; ".join(pieces))
        prior = row
    return flags


def period_stats(entries: list[EntryRow]) -> dict[str, str]:
    if not entries:
        return {"Average": "n/a", "Minimum": "n/a", "Maximum": "n/a"}
    totals = [row.total for row in entries]
    return {
        "Average": f"{sum(totals) / len(totals):.1f}",
        "Minimum": str(min(totals)),
        "Maximum": str(max(totals)),
    }


def plain_language_summary(entries: list[EntryRow], prior_entries: list[EntryRow]) -> str:
    if not entries:
        return "No PHQ-9 entries were recorded for the selected date range."
    first = entries[0]
    last = entries[-1]
    delta = last.total - first.total
    prior_text = ""
    if prior_entries:
        current_avg = sum(r.total for r in entries) / len(entries)
        prior_avg = sum(r.total for r in prior_entries) / len(prior_entries)
        prior_delta = current_avg - prior_avg
        direction = "higher" if prior_delta > 0 else "lower" if prior_delta < 0 else "unchanged"
        prior_text = f" The average score for this period was {abs(prior_delta):.1f} points {direction} than the prior comparable period."
    direction = "increased" if delta > 0 else "decreased" if delta < 0 else "was unchanged"
    return (
        f"Across {len(entries)} recorded entries, the PHQ-9 total score {direction} from "
        f"{first.total} to {last.total}. The most recent entry was in the {last.severity.lower()} range."
        f"{prior_text} Review item-level patterns and treatment-event timing with the clinician."
    )


def add_pdf_table(
    story,
    title: str,
    rows: list[list[str]],
    repeat_header: bool = True,
    highlight_flag_col: int | None = None,
    col_widths: list[float] | None = None,
    wrap_columns: set[int] | None = None,
) -> None:
    styles = getSampleStyleSheet()
    story.append(Paragraph(title, styles["Heading2"]))
    if wrap_columns:
        wrapped = []
        for row_idx, row in enumerate(rows):
            wrapped_row = []
            for col_idx, value in enumerate(row):
                if row_idx > 0 and col_idx in wrap_columns:
                    wrapped_row.append(Paragraph(str(value), styles["BodyText"]))
                else:
                    wrapped_row.append(str(value))
            wrapped.append(wrapped_row)
        rows = wrapped
    table = Table(rows, repeatRows=1 if repeat_header and len(rows) > 1 else 0, colWidths=col_widths)
    style_commands = [
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#E8EEF5")),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.HexColor("#172033")),
        ("GRID", (0, 0), (-1, -1), 0.25, colors.HexColor("#CBD5E1")),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("FONTSIZE", (0, 0), (-1, -1), 8),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#F8FAFC")]),
    ]
    if highlight_flag_col is not None:
        for row_idx, row in enumerate(rows[1:], start=1):
            if highlight_flag_col < len(row) and str(row[highlight_flag_col]).strip():
                style_commands.append(("BACKGROUND", (0, row_idx), (-1, row_idx), colors.HexColor("#FFF7ED")))
                style_commands.append(("TEXTCOLOR", (highlight_flag_col, row_idx), (highlight_flag_col, row_idx), colors.HexColor("#9A3412")))
    table.setStyle(TableStyle(style_commands)
    )
    story.append(table)
    story.append(Spacer(1, 0.14 * inch))


def moving_average(values: list[int], window: int) -> list[float | None]:
    result = []
    for idx in range(len(values)):
        if idx + 1 < window:
            result.append(None)
        else:
            chunk = values[idx + 1 - window : idx + 1]
            result.append(sum(chunk) / len(chunk))
    return result


def normalize_event_type(event_type: str) -> str:
    text = (event_type or "").strip().lower()
    if "ketamine" in text:
        return "Ketamine"
    if "therapy" in text:
        return "Therapy"
    if "dose increase" in text:
        return "Medication Dose Increase"
    if "dose decrease" in text:
        return "Medication Dose Decrease"
    if "start" in text:
        return "Medication Start"
    if "stop" in text or "discontinued" in text:
        return "Medication Stop"
    return event_type or "Treatment event"


def average_total(entries: list[EntryRow]) -> float | None:
    return sum(row.total for row in entries) / len(entries) if entries else None


def entries_near_date(entries: list[EntryRow], target: str, before: int = 0, after: int = 0) -> list[EntryRow]:
    target_date = datetime.fromisoformat(target).date()
    start_date = target_date - timedelta(days=before)
    end_date = target_date + timedelta(days=after)
    return [
        row
        for row in entries
        if start_date <= datetime.fromisoformat(row.entry_date).date() <= end_date
    ]


def treatment_analysis(entries: list[EntryRow], events: list[tuple[int, str, str, str]], treatment: str) -> list[list[str]]:
    rows = []
    matching = [event for event in events if normalize_event_type(event[2]) == treatment]
    for _, event_date, event_type, description in matching:
        if treatment == "Ketamine":
            before_avg = average_total(entries_near_date(entries, event_date, before=7, after=-1))
            day_avg = average_total(entries_near_date(entries, event_date))
            after_avg = average_total(entries_near_date(entries, event_date, before=-1, after=7))
            change = None if before_avg is None or after_avg is None else after_avg - before_avg
            rows.append(
                [
                    event_date,
                    description or event_type,
                    "n/a" if before_avg is None else f"{before_avg:.1f}",
                    "n/a" if day_avg is None else f"{day_avg:.1f}",
                    "n/a" if after_avg is None else f"{after_avg:.1f}",
                    "n/a" if change is None else f"{change:+.1f}",
                ]
            )
        else:
            before_avg = average_total(entries_near_date(entries, event_date, before=7, after=-1))
            after_avg = average_total(entries_near_date(entries, event_date, before=-1, after=7))
            change = None if before_avg is None or after_avg is None else after_avg - before_avg
            rows.append(
                [
                    event_date,
                    description or event_type,
                    "n/a" if before_avg is None else f"{before_avg:.1f}",
                    "n/a" if after_avg is None else f"{after_avg:.1f}",
                    "n/a" if change is None else f"{change:+.1f}",
                ]
            )
    return rows


def draw_line_chart(
    path: str,
    entries: list[EntryRow],
    series: list[tuple[str, list[float | int | None], str]],
    title: str,
    y_max: int,
    events: list[tuple[int, str, str, str]] | None = None,
    show_severity: bool = False,
    note_markers: bool = False,
    width: int = 1100,
    height: int = 520,
) -> None:
    if PILImage is None:
        raise RuntimeError("Chart generation requires Pillow.")
    img = PILImage.new("RGB", (width, height), "white")
    draw = ImageDraw.Draw(img)
    font = ImageFont.load_default()
    title_font = ImageFont.load_default()
    left, right, top, bottom = 70, 35, 58, 72
    plot_w = width - left - right
    plot_h = height - top - bottom
    draw.text((left, 18), title, fill="#172033", font=title_font)
    if not entries:
        draw.text((width // 2 - 60, height // 2), "No entries", fill="#64748B", font=font)
        img.save(path)
        return

    def x_for_idx(idx: int) -> float:
        return left + (idx / max(len(entries) - 1, 1)) * plot_w

    def y_for_value(value: float) -> float:
        return top + plot_h - (value / y_max) * plot_h

    if show_severity:
        bands = [
            (0, 4, "#ECFDF5", "Minimal"),
            (5, 9, "#F0FDF4", "Mild"),
            (10, 14, "#FEFCE8", "Moderate"),
            (15, 19, "#FFF7ED", "Moderately Severe"),
            (20, 27, "#FEF2F2", "Severe"),
        ]
        for low, high, color, label in bands:
            y1 = y_for_value(high)
            y2 = y_for_value(low)
            draw.rectangle([left, y1, left + plot_w, y2], fill=color)
            draw.text((left + 6, y1 + 4), label, fill="#475569", font=font)

    for tick in range(0, y_max + 1, 3 if y_max > 5 else 1):
        y = y_for_value(tick)
        draw.line([(left, y), (left + plot_w, y)], fill="#E2E8F0")
        draw.text((18, y - 6), str(tick), fill="#475569", font=font)
    draw.line([(left, top), (left, top + plot_h), (left + plot_w, top + plot_h)], fill="#94A3B8", width=2)

    event_lookup = {}
    for event in events or []:
        event_lookup.setdefault(event[1], []).append(event)
    for idx, row in enumerate(entries):
        x = x_for_idx(idx)
        for event in event_lookup.get(row.entry_date, []):
            kind = normalize_event_type(event[2])
            color = {
                "Ketamine": "#7C3AED",
                "Therapy": "#0F766E",
                "Medication Start": "#2563EB",
                "Medication Stop": "#DC2626",
                "Medication Dose Increase": "#EA580C",
                "Medication Dose Decrease": "#0891B2",
            }.get(kind, "#64748B")
            draw.line([(x, top), (x, top + plot_h)], fill=color, width=2)
            draw.polygon([(x, top - 8), (x - 5, top), (x + 5, top)], fill=color)
        if note_markers and row.notes.strip():
            y = y_for_value(row.total)
            draw.ellipse([x - 5, y - 5, x + 5, y + 5], outline="#111827", width=2)

    for name, values, color in series:
        points = []
        for idx, value in enumerate(values):
            if value is None:
                if len(points) > 1:
                    draw.line(points, fill=color, width=3)
                points = []
                continue
            points.append((x_for_idx(idx), y_for_value(float(value))))
        if len(points) > 1:
            draw.line(points, fill=color, width=3)
        for x, y in points[:: max(1, len(points) // 35)]:
            draw.ellipse([x - 3, y - 3, x + 3, y + 3], fill=color)

    draw.text((left, height - 44), entries[0].entry_date, fill="#475569", font=font)
    draw.text((width - 110, height - 44), entries[-1].entry_date, fill="#475569", font=font)
    legend_x, legend_y = left, height - 24
    for name, _, color in series:
        draw.rectangle([legend_x, legend_y, legend_x + 12, legend_y + 12], fill=color)
        draw.text((legend_x + 18, legend_y - 1), name, fill="#334155", font=font)
        legend_x += 150
    if events:
        draw.text((legend_x, legend_y - 1), "Vertical markers: treatment/medication events", fill="#64748B", font=font)
    if note_markers:
        draw.text((left + 420, 18), "Outlined dots: notes", fill="#111827", font=font)
    img.save(path)


def add_chart(story, image_path: str, caption: str | None = None, width: float = 7.2 * inch) -> None:
    if caption:
        story.append(Paragraph(caption, getSampleStyleSheet()["Heading2"]))
    story.append(Image(image_path, width=width, height=width * 0.47))
    story.append(Spacer(1, 0.14 * inch))


def draw_treatment_bar_chart(path: str, title: str, rows: list[list[str]], labels: list[str]) -> None:
    if PILImage is None:
        raise RuntimeError("Chart generation requires Pillow.")
    width, height = 950, 360
    img = PILImage.new("RGB", (width, height), "white")
    draw = ImageDraw.Draw(img)
    font = ImageFont.load_default()
    draw.text((50, 18), title, fill="#172033", font=font)
    if not rows:
        draw.text((width // 2 - 80, height // 2), "No events recorded", fill="#64748B", font=font)
        img.save(path)
        return
    values_by_label = []
    for col_idx in range(2, 2 + len(labels)):
        values = []
        for row in rows:
            try:
                values.append(float(row[col_idx]))
            except (ValueError, IndexError):
                pass
        values_by_label.append(sum(values) / len(values) if values else None)
    left, top, bottom = 85, 68, 58
    plot_h = height - top - bottom
    plot_w = width - left - 45
    y_max = max([27, *[v for v in values_by_label if v is not None]])
    for tick in range(0, 28, 3):
        y = top + plot_h - (tick / y_max) * plot_h
        draw.line([(left, y), (left + plot_w, y)], fill="#E2E8F0")
        draw.text((35, y - 6), str(tick), fill="#475569", font=font)
    colors_local = ["#2563EB", "#7C3AED", "#0F766E"]
    bar_gap = plot_w / max(len(labels), 1)
    for idx, label in enumerate(labels):
        value = values_by_label[idx]
        x1 = left + idx * bar_gap + bar_gap * 0.2
        x2 = left + (idx + 1) * bar_gap - bar_gap * 0.2
        if value is not None:
            y = top + plot_h - (value / y_max) * plot_h
            draw.rectangle([x1, y, x2, top + plot_h], fill=colors_local[idx % len(colors_local)])
            draw.text((x1, y - 18), f"{value:.1f}", fill="#172033", font=font)
        draw.text((x1, top + plot_h + 12), label, fill="#334155", font=font)
    draw.line([(left, top), (left, top + plot_h), (left + plot_w, top + plot_h)], fill="#94A3B8", width=2)
    img.save(path)


def on_report_page(canvas, doc):
    canvas.saveState()
    canvas.setFont("Helvetica", 8)
    canvas.setFillColor(colors.HexColor("#64748B"))
    canvas.drawString(36, 20, DISCLAIMER)
    canvas.drawRightString(576, 20, f"Page {doc.page}")
    canvas.restoreState()


def anchor_heading(text: str, anchor: str, style) -> Paragraph:
    return Paragraph(f'<a name="{anchor}"/>{text}', style)


def toc_link(text: str, anchor: str, style) -> Paragraph:
    return Paragraph(f'<a href="#{anchor}">{text}</a>', style)


def ketamine_response_analysis(entries: list[EntryRow], events: list[tuple[int, str, str, str]]) -> list[list[str]]:
    rows = []
    ketamine_events = [event for event in events if normalize_event_type(event[2]) == "Ketamine"]
    for _, event_date, _event_type, description in ketamine_events:
        event_dt = datetime.fromisoformat(event_date).date()
        pre_entries = [
            row
            for row in entries
            if event_dt - timedelta(days=14) <= datetime.fromisoformat(row.entry_date).date() < event_dt
        ]
        post_entries = [
            row
            for row in entries
            if event_dt <= datetime.fromisoformat(row.entry_date).date() <= event_dt + timedelta(days=30)
        ]
        notes = []
        if len(pre_entries) < 3:
            notes.append("limited pre-treatment data")
        if len(post_entries) < 3:
            notes.append("limited post-treatment data")
        pre_avg = average_total(pre_entries)
        if pre_avg is None or not post_entries:
            rows.append([event_date, description or "Ketamine", "n/a", "n/a", "n/a", "n/a", "; ".join(notes) or "insufficient data"])
            continue
        best_row = min(post_entries, key=lambda row: row.total)
        improvement = pre_avg - best_row.total
        baseline_return = "not observed"
        for row in post_entries:
            row_dt = datetime.fromisoformat(row.entry_date).date()
            if row_dt > datetime.fromisoformat(best_row.entry_date).date() and row.total >= pre_avg - 1:
                baseline_return = str((row_dt - event_dt).days)
                break
        rows.append(
            [
                event_date,
                description or "Ketamine",
                f"{pre_avg:.1f}",
                f"{best_row.total} on {best_row.entry_date}",
                f"{improvement:+.1f}",
                baseline_return,
                "; ".join(notes) or "sufficient for screening-level review",
            ]
        )
    return rows


def generate_report(start: str, end: str, pdf_path: str, csv_path: str) -> None:
    if colors is None:
        raise RuntimeError("PDF export requires reportlab.")
    entries = fetch_entries(start, end)
    if not entries:
        raise ValueError("No entries found in the selected date range.")
    events = fetch_events(start, end)
    recent = entries[-14:]
    totals = [row.total for row in entries]
    events = [(event_id, event_date, normalize_event_type(event_type), desc) for event_id, event_date, event_type, desc in events]
    therapy_count = sum(1 for event in events if event[2] == "Therapy")
    ketamine_count = sum(1 for event in events if event[2] == "Ketamine")
    medication_count = sum(1 for event in events if event[2].startswith("Medication"))
    last_30_start = (datetime.fromisoformat(end).date() - timedelta(days=29)).isoformat()
    last_30_entries = fetch_entries(last_30_start, end)
    prev_30_end = datetime.fromisoformat(last_30_start).date() - timedelta(days=1)
    prev_30_start = prev_30_end - timedelta(days=29)
    prev_30_entries = fetch_entries(prev_30_start.isoformat(), prev_30_end.isoformat())
    last_30_avg = average_total(last_30_entries)
    prev_30_avg = average_total(prev_30_entries)
    avg_30_change = None if last_30_avg is None or prev_30_avg is None else last_30_avg - prev_30_avg

    with open(csv_path, "w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle)
        writer.writerow(["Date", "Total", "Severity", *(f"Item {i}" for i in range(1, 10)), "Question 9", "Notes", "Tag"])
        for row in entries:
            writer.writerow([row.entry_date, row.total, row.severity, *row.items, row.items[8], row.notes, row.note_tag])
        writer.writerow([])
        writer.writerow(["Ketamine Response Analysis"])
        writer.writerow(["Treatment date", "Description", "Pre-treatment average", "Best post-treatment score", "Improvement", "Days until return to baseline", "Data sufficiency notes"])
        writer.writerows(ketamine_response_analysis(entries, events))

    styles = getSampleStyleSheet()
    doc = SimpleDocTemplate(pdf_path, pagesize=letter, rightMargin=36, leftMargin=36, topMargin=36, bottomMargin=36)
    chart_dir = Path(tempfile.mkdtemp(prefix="phq9_report_charts_"))
    item9_chart = chart_dir / "item9_trend.png"
    draw_line_chart(
        str(item9_chart),
        entries[-90:],
        [("Item 9", [row.items[8] for row in entries[-90:]], "#B45309")],
        "Question 9 Response Trend",
        3,
    )

    story = [
        Paragraph("PHQ-9 Clinician Discussion Report", styles["Title"]),
        Paragraph(f"Date range: {start} to {end}", styles["Normal"]),
        Paragraph(DISCLAIMER, styles["BodyText"]),
        Spacer(1, 0.18 * inch),
        Paragraph("Table of Contents", styles["Title"]),
        toc_link("Question 9 Monitoring", "q9", styles["Normal"]),
        toc_link("Clinical Summary / Current Status", "clinical_summary", styles["Normal"]),
        toc_link("Recent 14-Day and 30-Day Score Summaries", "recent_scores", styles["Normal"]),
        toc_link("Most Recent 14-Day Symptom Responses", "recent_symptoms", styles["Normal"]),
        toc_link("Item-Level Analysis", "item_analysis", styles["Normal"]),
        toc_link("Treatment / Ketamine Analysis", "ketamine_analysis", styles["Normal"]),
        toc_link("Disclaimers", "disclaimers", styles["Normal"]),
        PageBreak(),
        anchor_heading("Question 9 Monitoring", "q9", styles["Heading1"]),
        Paragraph('"Thoughts that you would be better off dead or of hurting yourself"', styles["Heading2"]),
    ]
    item9_values = [row.items[8] for row in entries]
    add_pdf_table(
        story,
        "Question 9 Summary",
        [
            ["Metric", "Value"],
            ["Average score", f"{sum(item9_values) / len(item9_values):.1f}"],
            ["Maximum score", str(max(item9_values))],
            ["Days score > 0", str(sum(1 for value in item9_values if value > 0))],
            ["Days score > 1", str(sum(1 for value in item9_values if value > 1))],
            ["Most recent score", str(item9_values[-1])],
        ],
        col_widths=[2.8 * inch, 2.0 * inch],
    )
    add_chart(story, str(item9_chart), "Question 9 Trend", width=6.7 * inch)
    tag_groups = {}
    for row in entries:
        if row.note_tag:
            tag_groups.setdefault(row.note_tag, []).append(row.total)
    if tag_groups:
        tag_rows = [["Tag", "Entries", "Average total"]] + [
            [tag, str(len(values)), f"{sum(values) / len(values):.1f}"] for tag, values in sorted(tag_groups.items())
        ]
        add_pdf_table(story, "Note Tag Score Summary", tag_rows, col_widths=[2.2 * inch, 1.2 * inch, 1.5 * inch])
    story.append(PageBreak())

    story.append(anchor_heading("Clinical Summary / Current Status", "clinical_summary", styles["Heading1"]))
    current_rows = [
        ["Date range", f"{start} to {end}", "Entries", str(len(entries))],
        ["Most recent score", str(entries[-1].total), "Current severity", entries[-1].severity],
        ["Highest score", str(max(totals)), "Lowest score", str(min(totals))],
        ["Overall average", f"{sum(totals) / len(totals):.1f}", "30-day average", "n/a" if last_30_avg is None else f"{last_30_avg:.1f}"],
        ["Change vs prior 30 days", "n/a" if avg_30_change is None else f"{avg_30_change:+.1f}", "Therapy / Ketamine", f"{therapy_count} / {ketamine_count}"],
        ["Medication changes", str(medication_count), "First score", str(entries[0].total)],
    ]
    add_pdf_table(story, "Current Status", current_rows, col_widths=[1.7 * inch, 1.4 * inch, 1.7 * inch, 1.6 * inch])
    story.append(PageBreak())

    story.append(anchor_heading("Recent 14-Day and 30-Day Score Summaries", "recent_scores", styles["Heading1"]))
    recent_14_avg = average_total(recent)
    score_rows = [
        ["Window", "Entries", "Average", "Minimum", "Maximum", "Most recent"],
        ["Last 14 entries", str(len(recent)), "n/a" if recent_14_avg is None else f"{recent_14_avg:.1f}", str(min(row.total for row in recent)), str(max(row.total for row in recent)), str(recent[-1].total)],
        ["Last 30 days", str(len(last_30_entries)), "n/a" if last_30_avg is None else f"{last_30_avg:.1f}", "n/a" if not last_30_entries else str(min(row.total for row in last_30_entries)), "n/a" if not last_30_entries else str(max(row.total for row in last_30_entries)), str(entries[-1].total)],
    ]
    add_pdf_table(story, "Recent Score Summary", score_rows, col_widths=[1.5 * inch, 0.8 * inch, 0.9 * inch, 0.9 * inch, 0.9 * inch, 1.0 * inch])

    add_pdf_table(
        story,
        "Most Recent 14-Day Symptom Responses",
        [["Date", *(f"I{i}" for i in range(1, 10)), "Total", "Severity"]]
        + [[row.entry_date, *[str(v) for v in row.items], str(row.total), row.severity] for row in recent],
        col_widths=[0.85 * inch, *([0.33 * inch] * 9), 0.55 * inch, 1.25 * inch],
    )
    story.append(PageBreak())

    story.append(anchor_heading("Most Recent 14-Day Symptom Responses", "recent_symptoms", styles["Heading1"]))
    add_pdf_table(
        story,
        "Recent Symptom Detail",
        [["Date", *(f"I{i}" for i in range(1, 10)), "Total", "Severity"]]
        + [[row.entry_date, *[str(v) for v in row.items], str(row.total), row.severity] for row in recent],
        col_widths=[0.85 * inch, *([0.33 * inch] * 9), 0.55 * inch, 1.25 * inch],
    )
    story.append(PageBreak())

    story.append(anchor_heading("Item-Level Analysis", "item_analysis", styles["Heading1"]))
    item_rows = [["Item", "Lifetime average", "Last 14-day average", "Most recent"]]
    for idx, label in enumerate(ITEM_LABELS, start=1):
        values = [row.items[idx - 1] for row in entries]
        recent_values = [row.items[idx - 1] for row in recent]
        item_rows.append([f"{idx}. {label}", f"{sum(values) / len(values):.1f}", f"{sum(recent_values) / len(recent_values):.1f}", str(values[-1])])
    add_pdf_table(story, "Item Summary Statistics", item_rows, col_widths=[3.8 * inch, 1.1 * inch, 1.35 * inch, 0.8 * inch], wrap_columns={0})
    chart_entries = entries[-90:]
    for idx, label in enumerate(ITEM_LABELS, start=1):
        item_chart = chart_dir / f"item_{idx}.png"
        item_values = [row.items[idx - 1] for row in chart_entries]
        draw_line_chart(
            str(item_chart),
            chart_entries,
            [
                (f"Item {idx}", item_values, "#2563EB" if idx != 9 else "#B45309"),
                ("14-entry average", moving_average(item_values, min(14, max(1, len(item_values)))), "#0F766E"),
            ],
            f"Item {idx}: {label} (last 90 days)",
            3,
            width=950,
            height=360,
        )
        add_chart(story, str(item_chart), f"Item {idx} Trend", width=6.7 * inch)
        if idx in (4, 8):
            story.append(PageBreak())

    story.append(PageBreak())
    story.append(anchor_heading("Treatment / Ketamine Analysis", "ketamine_analysis", styles["Heading1"]))
    ketamine_rows = ketamine_response_analysis(entries, events)
    add_pdf_table(
        story,
        "Ketamine Response Review",
        [["Treatment date", "Description", "Pre-treatment average", "Best post-treatment score", "Improvement", "Days to baseline", "Data notes"]]
        + (ketamine_rows if ketamine_rows else [["No ketamine treatments recorded", "", "", "", "", "", ""]]),
        col_widths=[0.85 * inch, 1.45 * inch, 0.9 * inch, 1.15 * inch, 0.75 * inch, 0.75 * inch, 1.2 * inch],
        wrap_columns={1, 6},
    )
    story.append(Paragraph("This section estimates whether each ketamine treatment was followed by a lower PHQ-9 score and whether scores returned near pre-treatment baseline within the available follow-up window.", styles["BodyText"]))
    story.append(PageBreak())

    story.append(anchor_heading("Disclaimers", "disclaimers", styles["Heading1"]))
    story.append(Paragraph(DISCLAIMER, styles["BodyText"]))
    doc.build(story, onFirstPage=on_report_page, onLaterPages=on_report_page)


class LineChart(Canvas):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, bg="#FFFFFF", highlightthickness=1, highlightbackground="#CBD5E1", **kwargs)

    def draw_series(self, entries: list[EntryRow], series: list[tuple[str, list[int], str]], y_max: int, title: str) -> None:
        self.delete("all")
        width = max(self.winfo_width(), int(self["width"]))
        height = max(self.winfo_height(), int(self["height"]))
        pad_l, pad_r, pad_t, pad_b = 46, 18, 34, 36
        self.create_text(12, 12, text=title, anchor="nw", fill="#172033", font=("Segoe UI", 11, "bold"))
        if not entries or not series:
            self.create_text(width / 2, height / 2, text="No entries to display", fill="#64748B")
            return
        plot_w = width - pad_l - pad_r
        plot_h = height - pad_t - pad_b
        self.create_line(pad_l, pad_t, pad_l, pad_t + plot_h, fill="#94A3B8")
        self.create_line(pad_l, pad_t + plot_h, pad_l + plot_w, pad_t + plot_h, fill="#94A3B8")
        for tick in range(0, y_max + 1, max(1, y_max // 5)):
            y = pad_t + plot_h - (tick / y_max) * plot_h
            self.create_line(pad_l - 4, y, pad_l + plot_w, y, fill="#E2E8F0")
            self.create_text(pad_l - 8, y, text=str(tick), anchor="e", fill="#475569", font=("Segoe UI", 8))
        points_count = max(len(entries) - 1, 1)
        for name, values, color in series:
            points = []
            for idx, value in enumerate(values):
                x = pad_l + (idx / points_count) * plot_w
                y = pad_t + plot_h - (value / y_max) * plot_h
                points.extend([x, y])
                self.create_oval(x - 3, y - 3, x + 3, y + 3, fill=color, outline=color)
            if len(points) >= 4:
                self.create_line(*points, fill=color, width=2, smooth=True)
        labels = [entries[0].entry_date, entries[-1].entry_date] if len(entries) > 1 else [entries[0].entry_date]
        self.create_text(pad_l, height - 14, text=labels[0], anchor="w", fill="#475569", font=("Segoe UI", 8))
        if len(labels) > 1:
            self.create_text(width - pad_r, height - 14, text=labels[1], anchor="e", fill="#475569", font=("Segoe UI", 8))
        legend_x = pad_l + 8
        for name, _, color in series:
            self.create_rectangle(legend_x, pad_t - 18, legend_x + 10, pad_t - 8, fill=color, outline=color)
            self.create_text(legend_x + 14, pad_t - 13, text=name, anchor="w", fill="#334155", font=("Segoe UI", 8))
            legend_x += max(90, len(name) * 7)


class PHQ9App(Tk):
    def __init__(self):
        super().__init__()
        self.title("Local PHQ-9 Tracker")
        self.geometry("1180x780")
        self.minsize(980, 680)
        self.configure(bg="#F8FAFC")
        init_db()
        self.create_menu()
        self.create_widgets()
        self.refresh_all()

    def create_menu(self):
        menu = Menu(self)
        file_menu = Menu(menu, tearoff=0)
        file_menu.add_command(label="Import spreadsheet...", command=self.import_file)
        file_menu.add_command(label="Export entries...", command=self.export_file)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.destroy)
        menu.add_cascade(label="File", menu=file_menu)
        self.config(menu=menu)

    def create_widgets(self):
        header = Frame(self, bg="#172033", padx=16, pady=12)
        header.pack(fill="x")
        Label(header, text="Local PHQ-9 Tracker", fg="white", bg="#172033", font=("Segoe UI", 18, "bold")).pack(side=LEFT)
        Label(
            header,
            text="All data is stored locally in SQLite. No upload or cloud sync is performed by this app.",
            fg="#DDE7F3",
            bg="#172033",
            font=("Segoe UI", 10),
        ).pack(side=RIGHT)

        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill=BOTH, expand=True, padx=12, pady=12)
        self.dashboard = Frame(self.notebook, bg="#F8FAFC")
        self.entry_tab = Frame(self.notebook, bg="#F8FAFC")
        self.report_tab = Frame(self.notebook, bg="#F8FAFC")
        self.events_tab = Frame(self.notebook, bg="#F8FAFC")
        self.notebook.add(self.dashboard, text="Dashboard")
        self.notebook.add(self.entry_tab, text="Daily Entry")
        self.notebook.add(self.events_tab, text="Treatment Events")
        self.notebook.add(self.report_tab, text="Clinician Report")
        self.build_dashboard()
        self.build_entry_tab()
        self.build_events_tab()
        self.build_report_tab()

    def build_dashboard(self):
        top = Frame(self.dashboard, bg="#F8FAFC")
        top.pack(fill="x", pady=(0, 10))
        Label(top, text="Dashboard", bg="#F8FAFC", fg="#172033", font=("Segoe UI", 16, "bold")).pack(side=LEFT)
        Button(top, text="Import Spreadsheet", command=self.import_file).pack(side=RIGHT, padx=(6, 0))
        Button(top, text="Refresh", command=self.refresh_all).pack(side=RIGHT)

        cards = Frame(self.dashboard, bg="#F8FAFC")
        cards.pack(fill="x", pady=(0, 14))
        self.dashboard_cards = {}
        for label in ["Total Entries", "Most Recent Date", "Most Recent Score", "14-Day Average"]:
            card = Frame(cards, bg="#FFFFFF", padx=14, pady=10, highlightthickness=1, highlightbackground="#CBD5E1")
            card.pack(side=LEFT, fill="x", expand=True, padx=(0, 10))
            Label(card, text=label, bg="#FFFFFF", fg="#64748B", font=("Segoe UI", 9, "bold")).pack(anchor="w")
            value = Label(card, text="--", bg="#FFFFFF", fg="#172033", font=("Segoe UI", 15, "bold"))
            value.pack(anchor="w", pady=(4, 0))
            self.dashboard_cards[label] = value

        main = Frame(self.dashboard, bg="#F8FAFC")
        main.pack(fill=BOTH, expand=True)
        left = Frame(main, bg="#F8FAFC")
        left.pack(side=LEFT, fill=BOTH, expand=True, padx=(0, 8))
        right = Frame(main, bg="#F8FAFC")
        right.pack(side=RIGHT, fill=BOTH, expand=True, padx=(8, 0))

        Label(left, text="Most Recent 14 Entries", bg="#F8FAFC", fg="#172033", font=("Segoe UI", 12, "bold")).pack(anchor="w")
        cols = ["Date", "Total", "Severity", "Score Change", "Severity Change"]
        self.recent_table = ttk.Treeview(left, columns=cols, show="headings", height=15)
        for col in cols:
            self.recent_table.heading(col, text=col)
            width = 115 if col != "Severity Change" else 150
            self.recent_table.column(col, width=width, anchor="w")
        self.recent_table.tag_configure("worse", foreground="#B91C1C")
        self.recent_table.tag_configure("better", foreground="#047857")
        self.recent_table.tag_configure("neutral", foreground="#475569")
        self.recent_table.pack(fill=BOTH, expand=True, pady=(6, 0))

        Label(right, text="Item Averages", bg="#F8FAFC", fg="#172033", font=("Segoe UI", 12, "bold")).pack(anchor="w")
        self.item_table = ttk.Treeview(right, columns=["Item", "Lifetime Average", "Last 14 Days Average"], show="headings", height=14)
        for col, width in [("Item", 360), ("Lifetime Average", 130), ("Last 14 Days Average", 150)]:
            self.item_table.heading(col, text=col)
            self.item_table.column(col, width=width, anchor="w")
        self.item_table.pack(fill=BOTH, expand=True, pady=(6, 0))

    def build_entry_tab(self):
        form = LabelFrame(self.entry_tab, text="Manual Daily PHQ-9 Entry", bg="#F8FAFC", padx=12, pady=12)
        form.pack(fill=BOTH, expand=False, padx=4, pady=4)
        Label(form, text="Date (YYYY-MM-DD)", bg="#F8FAFC").grid(row=0, column=0, sticky="w")
        self.date_var = StringVar(value=date.today().isoformat())
        Entry(form, textvariable=self.date_var, width=16).grid(row=0, column=1, sticky="w", padx=8, pady=4)

        self.item_vars = []
        for idx, label in enumerate(ITEM_LABELS, start=1):
            Label(form, text=f"Item {idx}: {label}", bg="#F8FAFC", wraplength=560, justify=LEFT).grid(row=idx, column=0, sticky="w", pady=3)
            var = IntVar(value=0)
            self.item_vars.append(var)
            ttk.Spinbox(form, from_=0, to=3, textvariable=var, width=5).grid(row=idx, column=1, sticky="w", padx=8)

        Label(form, text="Optional notes", bg="#F8FAFC").grid(row=10, column=0, sticky="nw", pady=(8, 2))
        self.notes_box = Text(form, height=5, width=72)
        self.notes_box.grid(row=10, column=1, sticky="we", padx=8, pady=(8, 2))
        Label(form, text="Optional note tag", bg="#F8FAFC").grid(row=11, column=0, sticky="w", pady=(4, 2))
        self.note_tag = StringVar(value="")
        ttk.Combobox(
            form,
            textvariable=self.note_tag,
            values=["", "Finances", "Work", "Family", "Health", "Sleep", "Relationships", "Other"],
            state="readonly",
            width=20,
        ).grid(row=11, column=1, sticky="w", padx=8, pady=(4, 2))
        Button(form, text="Save Daily Entry", command=self.save_entry).grid(row=12, column=1, sticky="w", padx=8, pady=12)

    def build_events_tab(self):
        form = LabelFrame(self.events_tab, text="Medication/Treatment Event Marker", bg="#F8FAFC", padx=12, pady=12)
        form.pack(fill="x", padx=4, pady=4)
        self.event_date = StringVar(value=date.today().isoformat())
        self.event_type = StringVar(value="Ketamine")
        Label(form, text="Date (YYYY-MM-DD)", bg="#F8FAFC").grid(row=0, column=0, sticky="w")
        Entry(form, textvariable=self.event_date, width=16).grid(row=0, column=1, sticky="w", padx=8)
        Label(form, text="Type", bg="#F8FAFC").grid(row=0, column=2, sticky="w", padx=(18, 0))
        ttk.Combobox(
            form,
            textvariable=self.event_type,
            values=[
                "Ketamine",
                "Therapy",
                "Medication Start",
                "Medication Stop",
                "Medication Dose Increase",
                "Medication Dose Decrease",
                "Other treatment event",
            ],
            width=30,
        ).grid(row=0, column=3, sticky="w", padx=8)
        Label(form, text="Description", bg="#F8FAFC").grid(row=1, column=0, sticky="nw", pady=(8, 0))
        self.event_desc = Text(form, height=4, width=80)
        self.event_desc.grid(row=1, column=1, columnspan=3, sticky="we", padx=8, pady=(8, 0))
        Button(form, text="Add Event", command=self.save_event).grid(row=2, column=1, sticky="w", padx=8, pady=10)

        self.events_table = ttk.Treeview(self.events_tab, columns=["Date", "Type", "Description"], show="headings", height=16)
        for col, width in [("Date", 120), ("Type", 180), ("Description", 620)]:
            self.events_table.heading(col, text=col)
            self.events_table.column(col, width=width, anchor="w")
        self.events_table.pack(fill=BOTH, expand=True, padx=4, pady=10)

    def build_report_tab(self):
        box = LabelFrame(self.report_tab, text="Clinician Report", bg="#F8FAFC", padx=12, pady=12)
        box.pack(fill="x", padx=4, pady=4)
        entries = fetch_entries()
        default_start = entries[0].entry_date if entries else (date.today() - timedelta(days=30)).isoformat()
        default_end = entries[-1].entry_date if entries else date.today().isoformat()
        self.report_start = StringVar(value=default_start)
        self.report_end = StringVar(value=default_end)
        Label(box, text="Start date", bg="#F8FAFC").grid(row=0, column=0, sticky="w")
        Entry(box, textvariable=self.report_start, width=16).grid(row=0, column=1, sticky="w", padx=8)
        Label(box, text="End date", bg="#F8FAFC").grid(row=0, column=2, sticky="w", padx=(18, 0))
        Entry(box, textvariable=self.report_end, width=16).grid(row=0, column=3, sticky="w", padx=8)
        Button(box, text="Generate PDF and CSV Report", command=self.create_report).grid(row=0, column=4, padx=18)
        Label(
            self.report_tab,
            text=DISCLAIMER,
            bg="#F8FAFC",
            fg="#334155",
            font=("Segoe UI", 10, "italic"),
            wraplength=900,
        ).pack(anchor="w", padx=8, pady=10)
        self.report_status = Label(self.report_tab, text="", bg="#F8FAFC", fg="#172033", justify=LEFT)
        self.report_status.pack(anchor="w", padx=8)

    def refresh_all(self):
        self.refresh_recent_table()
        self.refresh_item_table()
        self.refresh_events()
        entries = fetch_entries()
        if entries:
            recent = fetch_recent_entries(14)
            recent_avg = sum(row.total for row in recent) / len(recent) if recent else 0
            self.dashboard_cards["Total Entries"].config(text=str(len(entries)))
            self.dashboard_cards["Most Recent Date"].config(text=entries[-1].entry_date)
            self.dashboard_cards["Most Recent Score"].config(text=f"{entries[-1].total} ({entries[-1].severity})")
            self.dashboard_cards["14-Day Average"].config(text=f"{recent_avg:.1f} ({severity_for_score(round(recent_avg))})")
            self.report_start.set(self.report_start.get() or entries[0].entry_date)
            self.report_end.set(entries[-1].entry_date)
        else:
            for value in self.dashboard_cards.values():
                value.config(text="--")

    def refresh_recent_table(self):
        for row in self.recent_table.get_children():
            self.recent_table.delete(row)
        entries = fetch_recent_entries(14)
        prior = None
        for row in entries:
            if prior:
                score_delta = row.total - prior.total
                score_text = f"{score_delta:+d}" if score_delta else "0"
                severity_delta = SEVERITY_ORDER[row.severity] - SEVERITY_ORDER[prior.severity]
                if severity_delta > 0:
                    severity_text = f"Worse: {prior.severity} to {row.severity}"
                    tag = "worse"
                elif severity_delta < 0:
                    severity_text = f"Improved: {prior.severity} to {row.severity}"
                    tag = "better"
                else:
                    severity_text = "No change"
                    tag = "worse" if score_delta > 0 else "better" if score_delta < 0 else "neutral"
            else:
                score_text = "--"
                severity_text = "--"
                tag = "neutral"
            self.recent_table.insert("", END, values=[row.entry_date, row.total, row.severity, score_text, severity_text], tags=(tag,))
            prior = row

    def refresh_item_table(self):
        for row in self.item_table.get_children():
            self.item_table.delete(row)
        entries = fetch_entries()
        recent = fetch_recent_entries(14)
        if not entries:
            return
        for idx, label in enumerate(ITEM_LABELS, start=1):
            values = [row.items[idx - 1] for row in entries]
            recent_values = [row.items[idx - 1] for row in recent]
            self.item_table.insert(
                "",
                END,
                values=[f"Item {idx}: {label}", f"{sum(values) / len(values):.1f}", f"{sum(recent_values) / len(recent_values):.1f}" if recent_values else "n/a"],
            )

    def refresh_events(self):
        for row in self.events_table.get_children():
            self.events_table.delete(row)
        for _, event_date, event_type, desc in fetch_events():
            self.events_table.insert("", END, values=[event_date, event_type, desc])

    def draw_charts(self):
        return

    def import_file(self):
        path = filedialog.askopenfilename(
            title="Import PHQ-9 spreadsheet",
            filetypes=[("Excel files", "*.xlsx *.xls"), ("CSV files", "*.csv"), ("All files", "*.*")],
        )
        if not path:
            return
        try:
            if load_workbook is None:
                run_bundled_cli(["--import", path])
                count = "the selected"
            else:
                count = import_spreadsheet(path)
            self.refresh_all()
            messagebox.showinfo("Import complete", f"Imported or updated {count} PHQ-9 entries.")
        except Exception as exc:
            messagebox.showerror("Import failed", str(exc))

    def export_file(self):
        path = filedialog.asksaveasfilename(
            title="Export PHQ-9 data",
            initialdir=str(EXPORTS_DIR),
            defaultextension=".xlsx",
            filetypes=[("Excel workbook", "*.xlsx"), ("CSV file", "*.csv")],
        )
        if not path:
            return
        try:
            if path.lower().endswith(".xlsx") and pd is None:
                run_bundled_cli(["--export", path])
            else:
                export_entries(path)
            messagebox.showinfo("Export complete", f"Saved export to:\n{path}")
        except Exception as exc:
            messagebox.showerror("Export failed", str(exc))

    def save_entry(self):
        entry_date = parse_date(self.date_var.get())
        if not entry_date:
            messagebox.showerror("Invalid date", "Enter the date as YYYY-MM-DD.")
            return
        items = [int(var.get()) for var in self.item_vars]
        if any(score < 0 or score > 3 for score in items):
            messagebox.showerror("Invalid score", "Each PHQ-9 item must be 0, 1, 2, or 3.")
            return
        notes = self.notes_box.get("1.0", END).strip()
        upsert_entry(entry_date, items, notes=notes, source="manual", note_tag=self.note_tag.get().strip())
        self.refresh_all()
        messagebox.showinfo("Saved", f"Saved PHQ-9 entry for {entry_date}.")

    def save_event(self):
        event_date = parse_date(self.event_date.get())
        if not event_date:
            messagebox.showerror("Invalid date", "Enter the event date as YYYY-MM-DD.")
            return
        add_event(event_date, self.event_type.get().strip() or "Treatment event", self.event_desc.get("1.0", END).strip())
        self.event_desc.delete("1.0", END)
        self.refresh_events()
        messagebox.showinfo("Saved", f"Saved event for {event_date}.")

    def create_report(self):
        start = parse_date(self.report_start.get())
        end = parse_date(self.report_end.get())
        if not start or not end:
            messagebox.showerror("Invalid date range", "Enter dates as YYYY-MM-DD.")
            return
        if start > end:
            messagebox.showerror("Invalid date range", "Start date must be before or equal to end date.")
            return
        target = filedialog.asksaveasfilename(
            title="Save clinician report PDF",
            initialdir=str(REPORTS_DIR),
            initialfile=f"PHQ9_Clinician_Report_{start}_to_{end}.pdf",
            defaultextension=".pdf",
            filetypes=[("PDF report", "*.pdf")],
        )
        if not target:
            return
        csv_path = str(Path(target).with_suffix(".csv"))
        try:
            if colors is None or PILImage is None:
                run_bundled_cli(["--report-start", start, "--report-end", end, "--report-pdf", target])
            else:
                generate_report(start, end, target, csv_path)
            self.report_status.config(text=f"Saved PDF report:\n{target}\n\nSaved CSV report:\n{csv_path}")
            messagebox.showinfo("Report saved", f"Saved PDF and CSV report.\n\n{target}\n{csv_path}")
        except Exception as exc:
            messagebox.showerror("Report failed", str(exc))


def main():
    parser = argparse.ArgumentParser(description="Local PHQ-9 tracker")
    parser.add_argument("--import", dest="import_path", help="Import an Excel workbook, then exit unless --launch is also set.")
    parser.add_argument("--launch", action="store_true", help="Launch the GUI after command-line actions.")
    parser.add_argument("--report-start", help="Generate a report starting on YYYY-MM-DD.")
    parser.add_argument("--report-end", help="Generate a report ending on YYYY-MM-DD.")
    parser.add_argument("--report-pdf", help="PDF output path for command-line report generation.")
    parser.add_argument("--export", help="Export entries to CSV or XLSX, then exit.")
    args = parser.parse_args()

    init_db()
    if args.import_path:
        count = import_spreadsheet(args.import_path)
        print(f"Imported or updated {count} entries.")
    if args.report_start and args.report_end and args.report_pdf:
        pdf_path = Path(args.report_pdf)
        generate_report(args.report_start, args.report_end, str(pdf_path), str(pdf_path.with_suffix(".csv")))
        print(f"Saved report to {pdf_path}")
    if args.export:
        export_entries(args.export)
        print(f"Saved export to {args.export}")
    has_cli_action = bool(args.import_path or args.report_pdf or args.export)
    if args.launch or not has_cli_action:
        PHQ9App().mainloop()


if __name__ == "__main__":
    main()
