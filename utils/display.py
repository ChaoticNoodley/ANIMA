# =============================================================================
# utils/display.py
# Terminal UI layer — all visual rendering for ANIMA
#
# This module owns the presentation layer exclusively.
# It never computes scores or interprets results — it only renders data
# received from the engine and i18n layers.
#
# Visual identity: clinical, minimal, modern, technological.
# Color palette: steel blue + pale turquoise (medical/professional aesthetic).
# =============================================================================

import os
import textwrap

from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.text import Text
from rich import box

from data.i18n import t

console = Console()

# ── Color palette ─────────────────────────────────────────────────────────────
# Consistent token names used throughout the module.
# Change a value here to retheme the entire application.
COLORS: dict[str, str] = {
    "primary":   "steel_blue1",
    "secondary": "cadet_blue",
    "accent":    "pale_turquoise1",
    "muted":     "grey58",
    "warning":   "gold1",
    "danger":    "indian_red",
    "success":   "medium_spring_green",
    "text":      "grey93",
}


# ── Utilities ─────────────────────────────────────────────────────────────────

def clear_screen() -> None:
    """Clear the terminal — compatible with Linux, macOS, and Windows."""
    os.system("cls" if os.name == "nt" else "clear")


def _build_progress_bar(current: int, total: int) -> str:
    """
    Render an ASCII progress bar for the current question position.

    Args:
        current: 1-indexed current question number.
        total:   Total number of questions in the scale.

    Returns:
        Rich markup string representing the progress bar.
    """
    bar_length = 30
    filled = int((current / total) * bar_length)
    empty = bar_length - filled
    percentage = int((current / total) * 100)

    filled_bar = f"[{COLORS['success']}]{'█' * filled}[/{COLORS['success']}]"
    empty_bar  = f"[{COLORS['muted']}]{'░' * empty}[/{COLORS['muted']}]"

    return f"{filled_bar}{empty_bar} [{COLORS['accent']}]{percentage}%[/{COLORS['accent']}]"


# ── Language selection ────────────────────────────────────────────────────────

def pick_language() -> str:
    """
    Display the language selection screen before any other UI.

    Returns:
        "en" or "pt" based on the user's choice.
    """
    clear_screen()

    header = Text(justify="center")
    header.append("A N I M A\n", style=f"bold {COLORS['accent']}")
    header.append(
        "Clinical Psychological Scale Assessor  ·  Avaliador de Escalas Psicológicas",
        style=COLORS["secondary"],
    )
    console.print(Panel(header, border_style=COLORS["primary"], padding=(1, 4), box=box.DOUBLE))
    console.print()

    console.print(Panel(
        f"  [bold {COLORS['accent']}][ 1 ][/bold {COLORS['accent']}]  🇺🇸  English\n\n"
        f"  [bold {COLORS['accent']}][ 2 ][/bold {COLORS['accent']}]  🇧🇷  Português",
        title=f"[bold {COLORS['warning']}]Select language  /  Selecione o idioma[/bold {COLORS['warning']}]",
        border_style=COLORS["secondary"],
        padding=(1, 4),
    ))
    console.print()

    while True:
        raw = console.input(
            f"  [bold {COLORS['secondary']}]Option / Opção [1/2]: [/bold {COLORS['secondary']}]"
        ).strip()

        if raw == "1":
            return "en"
        if raw == "2":
            return "pt"

        console.print(f"  [red]{t('lang_invalid', 'en')}[/red]")


# ── Header ────────────────────────────────────────────────────────────────────

def print_header(lang: str = "en") -> None:
    """Render the ANIMA application header banner."""
    console.print()
    header = Text(justify="center")
    header.append(f"{t('app_title', lang)}\n",    style=f"bold {COLORS['accent']}")
    header.append(f"{t('app_subtitle', lang)}\n", style=COLORS["secondary"])
    header.append(t("app_version", lang),          style=f"dim {COLORS['muted']}")
    console.print(Panel(header, border_style=COLORS["primary"], padding=(1, 4), box=box.DOUBLE))


# ── Ethical disclaimer ────────────────────────────────────────────────────────

def print_ethical_disclaimer(lang: str) -> None:
    """Render the mandatory ethical and professional notice panel."""
    console.print(Panel(
        t("disclaimer_body", lang),
        title=f"[bold {COLORS['warning']}]{t('disclaimer_title', lang)}[/bold {COLORS['warning']}]",
        border_style=COLORS["warning"],
        style="on grey7",
        padding=(1, 3),
    ))
    console.print()


# ── Main menu ─────────────────────────────────────────────────────────────────

def print_main_menu(scales: dict, lang: str) -> None:
    """
    Render the main menu table listing all available scales.

    The table is generated dynamically from the SCALES dict, so adding a
    new scale to data/scales.py automatically adds it to the menu.
    """
    table = Table(
        title=f"[bold]{t('menu_title', lang)}[/bold]",
        box=box.ROUNDED,
        border_style=COLORS["primary"],
        header_style=f"bold {COLORS['accent']}",
        show_lines=True,
        padding=(0, 2),
    )

    table.add_column(t("menu_col_num",      lang), style="bold white",        width=4,  justify="center")
    table.add_column(t("menu_col_code",     lang), style=COLORS["secondary"], width=8)
    table.add_column(t("menu_col_scale",    lang), style="bold white",        width=22)
    table.add_column(t("menu_col_area",     lang), style=COLORS["accent"],    width=14)
    table.add_column(t("menu_col_items",    lang), style=COLORS["muted"],     width=6,  justify="center")
    table.add_column(t("menu_col_maxscore", lang), style=COLORS["muted"],     width=12, justify="center")

    for idx, (key, scale) in enumerate(scales.items(), start=1):
        # Use language-specific category if available
        area = scale.get(f"category_{lang}", scale["category"]) if lang == "pt" else scale["category"]
        table.add_row(
            str(idx),
            f"[bold]{scale['name']}[/bold]",
            scale["full_name"],
            area,
            str(len(scale["questions"])),
            str(scale["max_score"]),
        )

    console.print(table)
    console.print()
    console.print(
        f"  [bold {COLORS['muted']}]{t('menu_other_opts', lang)}[/bold {COLORS['muted']}]"
    )
    console.print()


# ── Scale intro ───────────────────────────────────────────────────────────────

def print_scale_intro(scale: dict, lang: str) -> None:
    """Render the scale description and instruction before starting the assessment."""
    clear_screen()
    print_header(lang)

    description = scale.get(f"description_{lang}", scale.get("description", ""))
    instruction = scale.get(f"instruction_{lang}", scale.get("instruction", ""))
    instr_label = "Instruction" if lang == "en" else "Instrução"

    console.print(Panel(
        f"[bold {COLORS['accent']}]{scale['full_name']}[/bold {COLORS['accent']}]\n\n"
        f"[{COLORS['text']}]{description}[/{COLORS['text']}]\n\n"
        f"[bold {COLORS['warning']}]{instr_label}:[/bold {COLORS['warning']}] "
        f"[italic]{instruction}[/italic]",
        title=f"[bold]{scale['name']}[/bold]",
        border_style=COLORS["secondary"],
        padding=(1, 3),
    ))
    console.print()


# ── Question prompt ───────────────────────────────────────────────────────────

def prompt_question(
    question: dict,
    options: list[tuple],
    current: int,
    total: int,
    lang: str,
) -> int:
    """
    Display a single question and collect a validated numeric response.

    Loops until the user enters an integer within the valid option range.

    Args:
        question: Question dict with "text" and optional "text_pt".
        options:  List of (score, en_label, pt_label) tuples.
        current:  1-indexed current question number.
        total:    Total questions in this scale.
        lang:     Active language code ("en" or "pt").

    Returns:
        Integer score value corresponding to the chosen option.
    """
    progress_bar = _build_progress_bar(current, total)
    console.print(
        f"  [{COLORS['muted']}]{t('question_of', lang, current=current, total=total)}"
        f"[/{COLORS['muted']}]  {progress_bar}"
    )
    console.print()

    # Select question text by language
    raw_text = question.get("text_pt" if lang == "pt" else "text", question["text"])
    wrapped_text = textwrap.fill(raw_text, width=70)

    console.print(Panel(
        f"[bold white]{wrapped_text}[/bold white]",
        border_style=COLORS["primary"],
        padding=(1, 2),
    ))
    console.print()

    # Render options — each is (score, en_label, pt_label)
    for idx, option in enumerate(options):
        score_val = option[0]
        # Select label by language: index 2 = PT, index 1 = EN
        label = option[2] if lang == "pt" and len(option) > 2 else option[1]
        console.print(
            f"  [bold {COLORS['accent']}][ {idx} ][/bold {COLORS['accent']}]  "
            f"[{COLORS['text']}]{label}[/{COLORS['text']}]"
        )

    console.print()

    # Input validation loop
    while True:
        try:
            raw = console.input(
                f"  [bold {COLORS['secondary']}]"
                f"{t('answer_prompt', lang, max=len(options) - 1)}"
                f"[/bold {COLORS['secondary']}]"
            )
            choice = int(raw)
            if 0 <= choice < len(options):
                return options[choice][0]  # Return score value
            console.print(
                f"  [red]{t('answer_invalid_range', lang, max=len(options) - 1)}[/red]"
            )
        except ValueError:
            console.print(f"  [red]{t('answer_invalid_input', lang)}[/red]")


# ── Results ───────────────────────────────────────────────────────────────────

def print_result(result: dict, lang: str) -> None:
    """Render the complete assessment result screen."""
    clear_screen()
    print_header(lang)

    interp = result["interpretation"]
    color = interp.get("color", "white")
    label = interp.get(f"label_{'pt' if lang == 'pt' else ''}", interp.get("label", "—"))
    note  = interp.get(f"note_{'pt'  if lang == 'pt' else ''}",  interp.get("note",  "—"))

    # Normalize: if lang == "en", use "label" / "note" directly
    if lang == "en":
        label = interp.get("label", "—")
        note  = interp.get("note",  "—")

    # ── Score panel ──
    score_text = Text(justify="center")
    score_text.append(f"\n{result['score']}", style=f"bold {color}")
    score_text.append(f"  /  {result['max_score']}\n", style="dim white")
    score_text.append(
        t("result_percentage", lang, pct=result["percentage"]),
        style=f"dim {COLORS['muted']}",
    )
    score_text.append("\n")

    category = result.get("category_pt" if lang == "pt" else "category", result["category"])

    console.print(Panel(
        score_text,
        title=(
            f"[bold {COLORS['accent']}]"
            f"{result['scale_name']}  —  {result['full_name']}"
            f"[/bold {COLORS['accent']}]"
        ),
        subtitle=f"[{COLORS['muted']}]{category}[/{COLORS['muted']}]",
        border_style=color,
        padding=(1, 4),
    ))
    console.print()

    # ── Clinical interpretation panel ──
    console.print(Panel(
        f"[bold {color}]{label}[/bold {color}]\n\n"
        f"[{COLORS['text']}]{note}[/{COLORS['text']}]",
        title=f"[bold]{t('result_clinical_interp', lang)}[/bold]",
        border_style=COLORS["secondary"],
        padding=(1, 3),
    ))

    # ── Special alerts (e.g. PHQ-9 item 9) ──
    for alert in result.get("alerts", []):
        alert_text = alert.get(lang, alert.get("en", str(alert))) if isinstance(alert, dict) else alert
        console.print()
        console.print(Panel(
            f"[bold yellow]{alert_text}[/bold yellow]",
            border_style="bright_red",
            padding=(1, 2),
        ))

    # ── Reference ranges table ──
    console.print()
    _print_reference_table(result, lang)

    # ── Bibliographic reference ──
    console.print()
    console.print(Panel(
        f"[dim italic]{result['reference']}[/dim italic]",
        title=f"[dim]{t('result_biblio', lang)}[/dim]",
        border_style=COLORS["muted"],
        padding=(0, 2),
    ))

    # ── Footer disclaimer ──
    console.print()
    console.print(
        f"  [dim italic {COLORS['muted']}]{t('result_disclaimer', lang)}[/dim italic {COLORS['muted']}]"
    )
    console.print()


def _print_reference_table(result: dict, lang: str) -> None:
    """Render the severity reference ranges table, highlighting the current range."""
    from data.scales import SCALES

    scale = SCALES.get(result["scale_id"])
    if not scale:
        return

    table = Table(
        title=f"[dim]{t('result_ref_table', lang)}[/dim]",
        box=box.SIMPLE,
        border_style=COLORS["muted"],
        header_style=f"dim {COLORS['muted']}",
        padding=(0, 2),
    )
    table.add_column(t("result_ref_score", lang), justify="center", width=12)
    table.add_column(t("result_ref_label", lang), width=36)
    table.add_column("", width=3, justify="center")

    current_label = result["interpretation"]["label"]

    for r in scale["ranges"]:
        is_active = r["label"] == current_label
        display_label = r.get(f"label_pt", r["label"]) if lang == "pt" else r["label"]
        table.add_row(
            f"{r['min']}–{r['max']}",
            display_label,
            "◄" if is_active else "",
            style=f"bold {r['color']}" if is_active else None,
        )

    console.print(table)


# ── History view ──────────────────────────────────────────────────────────────

def print_history(history: list[dict], lang: str) -> None:
    """Render the assessment history as a formatted table."""
    if not history:
        console.print(Panel(
            f"[dim]{t('history_empty', lang)}[/dim]",
            border_style=COLORS["muted"],
        ))
        return

    table = Table(
        title=f"[bold]{t('history_title', lang)}[/bold]",
        box=box.ROUNDED,
        border_style=COLORS["primary"],
        header_style=f"bold {COLORS['accent']}",
    )
    table.add_column(t("history_col_date",  lang), style=COLORS["muted"],     width=18)
    table.add_column(t("history_col_scale", lang), style="bold white",        width=8)
    table.add_column(t("history_col_area",  lang), style=COLORS["secondary"], width=14)
    table.add_column(t("history_col_score", lang), justify="center",          width=12)
    table.add_column(t("history_col_class", lang),                            width=32)

    for entry in history[-20:]:
        try:
            dt = entry["timestamp"][:16].replace("T", " ")
        except Exception:
            dt = entry.get("timestamp", "—")

        table.add_row(
            dt,
            entry.get("scale_name", "—"),
            entry.get("category", "—"),
            f"{entry.get('score', '?')} / {entry.get('max_score', '?')}",
            entry.get("severity", "—"),
        )

    console.print(table)
    console.print()


# ── Interaction helpers ───────────────────────────────────────────────────────

def ask_save_result(lang: str) -> bool:
    """
    Prompt the user to optionally save the result to history.

    Returns:
        True if the user confirms, False otherwise.
    """
    console.print()
    response = console.input(
        f"  [bold {COLORS['secondary']}]{t('save_prompt', lang)}[/bold {COLORS['secondary']}]"
    ).strip().lower()
    return response in t("save_yes_keys", lang)


def print_success(message: str) -> None:
    """Render a success status message."""
    console.print(f"  [bold {COLORS['success']}]✔  {message}[/bold {COLORS['success']}]")


def print_error(message: str) -> None:
    """Render an error status message."""
    console.print(f"  [bold {COLORS['danger']}]✖  {message}[/bold {COLORS['danger']}]")


def print_info(message: str) -> None:
    """Render an informational status message."""
    console.print(f"  [{COLORS['secondary']}]ℹ  {message}[/{COLORS['secondary']}]")


def wait_enter(lang: str = "en") -> None:
    """Pause execution until the user presses Enter."""
    console.print()
    console.input(f"  [{COLORS['muted']}]{t('press_enter', lang)}[/{COLORS['muted']}]")
