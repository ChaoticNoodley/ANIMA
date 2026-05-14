#!/usr/bin/env python3
# =============================================================================
# main.py
# ANIMA — Clinical Psychological Scale Assessor
# Entry point and application flow controller
#
# Flow:
#   1. Language selection
#   2. Ethical disclaimer
#   3. Main menu loop
#      ├─ Run a scale  → question loop → results → optional save
#      ├─ View history
#      ├─ Export CSV
#      └─ Quit
# =============================================================================

import sys

from data.scales import SCALES
from data.i18n import t
from core.engine import get_scale, get_options_for_question, build_result
from utils.display import (
    console,
    clear_screen,
    pick_language,
    print_header,
    print_ethical_disclaimer,
    print_main_menu,
    print_scale_intro,
    prompt_question,
    print_result,
    ask_save_result,
    print_history,
    print_success,
    print_error,
    print_info,
    wait_enter,
)
from utils.history import save_result, load_history, export_csv, get_history_summary


# ── Scale runner ──────────────────────────────────────────────────────────────

def run_scale(scale_id: str, lang: str) -> None:
    """
    Execute a full scale administration session.

    Displays the intro, iterates through all questions, computes the result,
    renders it, and offers to persist it to the history file.

    Args:
        scale_id: Key identifying the scale in SCALES (e.g. "phq9").
        lang:     Active language code ("en" or "pt").
    """
    scale = get_scale(scale_id)
    if not scale:
        print_error(f"Scale '{scale_id}' not found.")
        return

    print_scale_intro(scale, lang)

    start = console.input(
        f"  [bold steel_blue1]{t('scale_start_prompt', lang)}[/bold steel_blue1]"
    ).strip().lower()

    if start == "q":
        return

    answers: list[int] = []
    questions = scale["questions"]
    total = len(questions)

    for idx, question in enumerate(questions, start=1):
        clear_screen()
        print_header(lang)
        options = get_options_for_question(scale, question)
        score_value = prompt_question(question, options, idx, total, lang)
        answers.append(score_value)
        console.print()

    result = build_result(scale, answers)
    print_result(result, lang)

    if ask_save_result(lang):
        if save_result(result):
            print_success(t("save_success", lang))
        else:
            print_error(t("save_error", lang))

    wait_enter(lang)


# ── History view ──────────────────────────────────────────────────────────────

def show_history(lang: str) -> None:
    """Display the assessment history with summary statistics."""
    clear_screen()
    print_header(lang)

    history = load_history()
    print_history(history, lang)

    summary = get_history_summary()
    if summary["total"] > 0:
        print_info(t("history_total", lang, n=summary["total"]))
        for scale_name, data in summary["by_scale"].items():
            print_info(t("history_avg", lang,
                         scale=scale_name,
                         count=data["count"],
                         avg=data["avg_score"]))

    wait_enter(lang)


# ── CSV export ────────────────────────────────────────────────────────────────

def show_export(lang: str) -> None:
    """Export history to CSV and display the outcome."""
    clear_screen()
    print_header(lang)

    if export_csv():
        print_success(t("export_success", lang))
    else:
        print_error(t("export_error", lang))

    wait_enter(lang)


# ── Input parser ──────────────────────────────────────────────────────────────

def parse_menu_input(raw: str, scale_keys: list[str], lang: str) -> str | None:
    """
    Interpret a raw menu input string into a named action.

    Accepts:
        - "1", "2", "3" → scale by position
        - "phq9", "gad7", "isi" → scale by ID
        - "H" / "history" / "histórico"
        - "E" / "export" / "exportar"
        - "Q" / "S" / "quit" / "sair" / "exit"

    Returns:
        Action string, or None if the input is not recognized.
    """
    choice = raw.strip().lower()

    if choice in ("h", "history", "histórico", "historico"):
        return "history"
    if choice in ("e", "export", "exportar"):
        return "export"
    if choice in ("q", "s", "quit", "sair", "exit"):
        return "quit"

    if choice.isdigit():
        idx = int(choice) - 1
        if 0 <= idx < len(scale_keys):
            return scale_keys[idx]

    if choice in scale_keys:
        return choice

    return None


# ── Application entry point ───────────────────────────────────────────────────

def main() -> None:
    """
    Main application loop.

    Handles language selection, ethical disclaimer, and the main menu
    event loop until the user chooses to quit.
    """
    scale_keys = list(SCALES.keys())

    # Language selection is always the first screen
    lang = pick_language()

    # Ethical disclaimer — mandatory before any clinical tool interaction
    clear_screen()
    print_header(lang)
    print_ethical_disclaimer(lang)
    wait_enter(lang)

    # Main event loop
    running = True
    while running:
        clear_screen()
        print_header(lang)
        print_main_menu(SCALES, lang)

        raw = console.input(
            f"  [bold steel_blue1]{t('menu_input_prompt', lang)}[/bold steel_blue1]"
        )
        action = parse_menu_input(raw, scale_keys, lang)

        if action is None:
            console.print(f"\n  [red]{t('menu_invalid', lang)}[/red]")
            wait_enter(lang)

        elif action == "quit":
            running = False

        elif action == "history":
            show_history(lang)

        elif action == "export":
            show_export(lang)

        elif action in scale_keys:
            run_scale(action, lang)

    # Exit screen
    clear_screen()
    print_header(lang)
    console.print()
    console.print(
        f"  [dim italic {COLORS['secondary']}]{t('goodbye', lang)}"
        f"[/dim italic {COLORS['secondary']}]"
    )
    console.print()


# ── Guard ─────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    try:
        from utils.display import COLORS  # local import for exit screen
        main()
    except KeyboardInterrupt:
        lang_fallback = "en"
        console.print(f"\n\n  [dim]{t('interrupted', lang_fallback)}[/dim]\n")
        sys.exit(0)
