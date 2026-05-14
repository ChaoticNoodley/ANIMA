# =============================================================================
# utils/history.py
# Assessment history — persistence layer (JSON storage + CSV export)
#
# Responsibilities:
#   - Load and save assessment results to a local JSON file
#   - Export full history to CSV (Excel-compatible)
#   - Compute summary statistics for the history view
#
# The JSON file is created automatically on first save.
# =============================================================================

import json
import csv
from pathlib import Path

HISTORY_FILE = Path("anima_history.json")
CSV_EXPORT_FILE = Path("anima_history.csv")


def load_history() -> list[dict]:
    """
    Load the assessment history from the JSON file.

    Returns:
        List of result entry dicts. Returns an empty list if the file
        does not exist or cannot be parsed.
    """
    if not HISTORY_FILE.exists():
        return []

    try:
        with open(HISTORY_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return []


def save_result(result: dict) -> bool:
    """
    Append a new assessment result to the history file.

    Serializes only the fields relevant for historical tracking.
    The full result dict (with nested objects) is not saved directly.

    Args:
        result: Result dict as returned by core/engine.py build_result().

    Returns:
        True on success, False on write error.
    """
    try:
        history = load_history()

        entry = {
            "scale_id":   result["scale_id"],
            "scale_name": result["scale_name"],
            "category":   result["category"],
            "score":      result["score"],
            "max_score":  result["max_score"],
            "percentage": result["percentage"],
            "severity":   result["interpretation"]["label"],
            "timestamp":  result["timestamp"],
        }

        history.append(entry)

        with open(HISTORY_FILE, "w", encoding="utf-8") as f:
            json.dump(history, f, ensure_ascii=False, indent=2)

        return True

    except IOError:
        return False


def export_csv() -> bool:
    """
    Export the full history to a CSV file.

    The output file is compatible with Excel, LibreOffice Calc, and
    any tool that accepts standard CSV.

    Returns:
        True on success, False if no data exists or a write error occurs.
    """
    history = load_history()

    if not history:
        return False

    try:
        fieldnames = [
            "scale_name", "category", "score",
            "max_score", "percentage", "severity", "timestamp",
        ]

        with open(CSV_EXPORT_FILE, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(history)

        return True

    except IOError:
        return False


def get_history_summary() -> dict:
    """
    Compute aggregate statistics from the stored history.

    Groups results by scale name and calculates per-scale assessment
    count and average score.

    Returns:
        Dict with keys:
            "total"    → int, total number of assessments
            "by_scale" → dict mapping scale name to {"count": int, "avg_score": float}
    """
    history = load_history()

    if not history:
        return {"total": 0, "by_scale": {}}

    grouped: dict[str, list[int]] = {}
    for entry in history:
        name = entry["scale_name"]
        grouped.setdefault(name, []).append(entry["score"])

    by_scale = {
        name: {
            "count":     len(scores),
            "avg_score": round(sum(scores) / len(scores), 1),
        }
        for name, scores in grouped.items()
    }

    return {"total": len(history), "by_scale": by_scale}
