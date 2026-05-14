# =============================================================================
# core/engine.py
# Scoring and interpretation engine — pure business logic, no UI
#
# This module is intentionally isolated from the display layer.
# Separation of Concerns: this file never imports from utils/display.py
# and never calls print(). It only computes and returns data.
# =============================================================================

from datetime import datetime
from data.scales import SCALES


def get_scale(scale_id: str) -> dict | None:
    """
    Retrieve a scale definition by its ID.

    Args:
        scale_id: One of the keys defined in data/scales.py (e.g. "phq9").

    Returns:
        Scale dict, or None if the ID is not found.
    """
    return SCALES.get(scale_id)


def get_options_for_question(scale: dict, question: dict) -> list[tuple]:
    """
    Return the response options for a given question.

    Some scales (e.g. ISI) define per-question options under "custom_options".
    Others (PHQ-9, GAD-7) share a single options list at the scale level.

    Args:
        scale:    The scale dict containing a global "options" field.
        question: The question dict, which may contain "custom_options".

    Returns:
        List of (score_value, en_label, pt_label) tuples.
    """
    if "custom_options" in question:
        return question["custom_options"]
    return scale["options"]


def calculate_score(answers: list[int]) -> int:
    """
    Sum all item scores to produce the total scale score.

    Args:
        answers: List of integer scores, one per question.

    Returns:
        Integer total score.
    """
    return sum(answers)


def interpret_score(scale: dict, score: int) -> dict:
    """
    Map a total score to its corresponding severity range.

    Performs a linear search over the scale's "ranges" list and returns
    the first range whose [min, max] interval contains the score.

    Args:
        scale: Scale dict containing a "ranges" list.
        score: Total score to classify.

    Returns:
        Range dict with keys: label, label_pt, color, note, note_pt.
        Returns a fallback dict if no range matches (should not occur).
    """
    for severity_range in scale["ranges"]:
        if severity_range["min"] <= score <= severity_range["max"]:
            return severity_range

    # Defensive fallback — only reached if score is outside all defined ranges
    return {
        "label":    "Undetermined",
        "label_pt": "Indeterminado",
        "color":    "white",
        "note":     "Score is outside all defined severity ranges.",
        "note_pt":  "Pontuação fora das faixas definidas.",
    }


def check_special_alerts(scale: dict, answers: list[int]) -> list[str | dict]:
    """
    Check for special clinical alerts triggered by individual item responses.

    Currently used for PHQ-9 item 9 (suicidal ideation screening).
    An alert fires when the answer to a specific item meets or exceeds a threshold.

    Args:
        scale:   Scale dict with an optional "special_alerts" mapping.
        answers: List of integer responses, 0-indexed.

    Returns:
        List of alert dicts (with "en" and "pt" message keys), or empty list.
    """
    alerts: list = []

    for question_id, alert_config in scale.get("special_alerts", {}).items():
        index = question_id - 1  # Convert 1-indexed ID to 0-indexed list position
        if index < len(answers) and answers[index] >= alert_config["threshold"]:
            # Return a bilingual dict so display.py can pick the right language
            alerts.append({
                "en": alert_config.get("message",    alert_config.get("message_pt", "")),
                "pt": alert_config.get("message_pt", alert_config.get("message",    "")),
            })

    return alerts


def build_result(scale: dict, answers: list[int]) -> dict:
    """
    Construct a complete result object after a scale has been administered.

    This is a factory function: it assembles all computed values into
    a single dict that the display layer can render without any further logic.

    Args:
        scale:   Scale dict from SCALES.
        answers: Ordered list of integer scores from the user session.

    Returns:
        Result dict containing score, interpretation, alerts, metadata, etc.
    """
    score = calculate_score(answers)
    interpretation = interpret_score(scale, score)
    alerts = check_special_alerts(scale, answers)

    return {
        "scale_id":       scale["id"],
        "scale_name":     scale["name"],
        "full_name":      scale["full_name"],
        "category":       scale["category"],
        "category_pt":    scale.get("category_pt", scale["category"]),
        "score":          score,
        "max_score":      scale["max_score"],
        "percentage":     round((score / scale["max_score"]) * 100, 1),
        "interpretation": interpretation,
        "alerts":         alerts,
        "answers":        answers,
        "timestamp":      datetime.now().isoformat(),
        "reference":      scale["reference"],
    }
