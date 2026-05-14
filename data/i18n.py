# =============================================================================
# data/i18n.py
# Internationalization (i18n) — interface strings in English and Portuguese
#
# All user-facing text lives here. No hardcoded strings in display.py or
# main.py. Adding a new language means adding a key to each entry below.
#
# Usage:
#   from data.i18n import t
#   t("menu_title", lang)                          → "Available Scales"
#   t("question_of", lang, current=3, total=9)    → "Question 3 of 9"
# =============================================================================

STRINGS: dict[str, dict] = {

    # ── Application header ────────────────────────────────────────────────────
    "app_title": {
        "en": "ANIMA",
        "pt": "ANIMA",
    },
    "app_subtitle": {
        "en": "Clinical Psychological Scale Assessor",
        "pt": "Avaliador de Escalas Psicológicas Clínicas",
    },
    "app_version": {
        "en": "v1.0  ·  Educational & Research Use Only",
        "pt": "v1.0  ·  Uso Educacional e de Pesquisa",
    },

    # ── Language selection ────────────────────────────────────────────────────
    "lang_invalid": {
        "en": "Invalid option. Please enter 1 or 2.",
        "pt": "Opção inválida. Digite 1 ou 2.",
    },

    # ── Ethical disclaimer ────────────────────────────────────────────────────
    "disclaimer_title": {
        "en": "Ethical & Professional Notice",
        "pt": "Aviso Ético e Profissional",
    },
    "disclaimer_body": {
        "en": (
            "⚕  IMPORTANT NOTICE\n\n"
            "ANIMA is a clinical screening and educational tool intended "
            "exclusively for academic and research purposes. "
            "[bold]It does NOT replace assessment, diagnosis, or treatment "
            "by a licensed mental health professional.[/bold]\n\n"
            "If you are experiencing psychological distress or a mental health crisis, "
            "please reach out to a psychologist, psychiatrist, or a crisis helpline "
            "in your country immediately."
        ),
        "pt": (
            "⚕  AVISO IMPORTANTE\n\n"
            "O ANIMA é uma ferramenta de rastreio clínico e educacional destinada "
            "exclusivamente a fins acadêmicos e de pesquisa. "
            "[bold]NÃO substitui avaliação, diagnóstico ou tratamento por profissional "
            "de saúde mental habilitado.[/bold]\n\n"
            "Em caso de sofrimento psíquico ou crise, procure um psicólogo, psiquiatra "
            "ou o CVV – Centro de Valorização da Vida: [bold cyan]188[/bold cyan] (24h)."
        ),
    },

    # ── Main menu ─────────────────────────────────────────────────────────────
    "menu_title": {
        "en": "Available Scales",
        "pt": "Escalas Disponíveis",
    },
    "menu_col_num":      {"en": "#",         "pt": "#"},
    "menu_col_code":     {"en": "Code",      "pt": "Código"},
    "menu_col_scale":    {"en": "Scale",     "pt": "Escala"},
    "menu_col_area":     {"en": "Area",      "pt": "Área"},
    "menu_col_items":    {"en": "Items",     "pt": "Itens"},
    "menu_col_maxscore": {"en": "Max Score", "pt": "Pont. Máx."},

    "menu_other_opts": {
        "en": "Other options:  [bold]H[/bold] History   [bold]E[/bold] Export CSV   [bold]Q[/bold] Quit",
        "pt": "Outras opções:  [bold]H[/bold] Histórico   [bold]E[/bold] Exportar CSV   [bold]S[/bold] Sair",
    },
    "menu_input_prompt": {
        "en": "Select an option: ",
        "pt": "Selecione uma opção: ",
    },
    "menu_invalid": {
        "en": "Invalid option. Enter a number, scale code, H (history), E (export) or Q (quit).",
        "pt": "Opção inválida. Digite o número, o código da escala, H (histórico), E (exportar) ou S (sair).",
    },

    # ── Scale application ─────────────────────────────────────────────────────
    "scale_start_prompt": {
        "en": "Press Enter to begin or 'q' to go back: ",
        "pt": "Pressione Enter para iniciar ou 'q' para voltar: ",
    },
    "question_of": {
        "en": "Question {current} of {total}",
        "pt": "Questão {current} de {total}",
    },
    "answer_prompt": {
        "en": "Your answer [0–{max}]: ",
        "pt": "Sua resposta [0–{max}]: ",
    },
    "answer_invalid_range": {
        "en": "Please enter a number between 0 and {max}.",
        "pt": "Por favor, escolha um número entre 0 e {max}.",
    },
    "answer_invalid_input": {
        "en": "Invalid input. Please enter a number only.",
        "pt": "Entrada inválida. Digite apenas um número.",
    },

    # ── Results ───────────────────────────────────────────────────────────────
    "result_percentage": {
        "en": "{pct}% of maximum score",
        "pt": "{pct}% da pontuação máxima",
    },
    "result_clinical_interp": {
        "en": "Clinical Interpretation",
        "pt": "Interpretação Clínica",
    },
    "result_ref_table": {
        "en": "Severity Reference Ranges",
        "pt": "Faixas de Referência",
    },
    "result_ref_score": {"en": "Score",          "pt": "Pontuação"},
    "result_ref_label": {"en": "Classification", "pt": "Classificação"},
    "result_biblio": {
        "en": "Bibliographic Reference",
        "pt": "Referência Bibliográfica",
    },
    "result_disclaimer": {
        "en": (
            "This result is a screening tool only and does NOT constitute a clinical diagnosis. "
            "Please consult a licensed mental health professional."
        ),
        "pt": (
            "Este resultado é apenas uma triagem e NÃO constitui diagnóstico clínico. "
            "Consulte um profissional de saúde mental habilitado."
        ),
    },

    # ── Save / history ────────────────────────────────────────────────────────
    "save_prompt": {
        "en": "Save this result to history? [Y/n]: ",
        "pt": "Deseja salvar este resultado no histórico? [S/n]: ",
    },
    "save_yes_keys": {
        "en": ("y", "yes", ""),
        "pt": ("s", "sim", ""),
    },
    "save_success": {
        "en": "Result saved to history.",
        "pt": "Resultado salvo no histórico com sucesso.",
    },
    "save_error": {
        "en": "Could not save the result.",
        "pt": "Não foi possível salvar o resultado.",
    },

    # ── History view ──────────────────────────────────────────────────────────
    "history_title": {
        "en": "Assessment History",
        "pt": "Histórico de Avaliações",
    },
    "history_col_date":  {"en": "Date / Time",     "pt": "Data / Hora"},
    "history_col_scale": {"en": "Scale",            "pt": "Escala"},
    "history_col_area":  {"en": "Area",             "pt": "Área"},
    "history_col_score": {"en": "Score",            "pt": "Pontuação"},
    "history_col_class": {"en": "Classification",   "pt": "Classificação"},
    "history_empty": {
        "en": "No assessments recorded yet.",
        "pt": "Nenhuma avaliação registrada ainda.",
    },
    "history_total": {
        "en": "Total assessments recorded: {n}",
        "pt": "Total de avaliações registradas: {n}",
    },
    "history_avg": {
        "en": "{scale}: {count} assessment(s)  ·  Average score: {avg}",
        "pt": "{scale}: {count} avaliação(ões)  ·  Média de pontuação: {avg}",
    },

    # ── Export ────────────────────────────────────────────────────────────────
    "export_success": {
        "en": "History exported to 'anima_history.csv'.",
        "pt": "Histórico exportado para 'anima_historico.csv'.",
    },
    "export_error": {
        "en": "No data to export or file write error.",
        "pt": "Nenhum dado para exportar ou erro ao criar arquivo.",
    },

    # ── General ───────────────────────────────────────────────────────────────
    "press_enter": {
        "en": "Press Enter to continue...",
        "pt": "Pressione Enter para continuar...",
    },
    "goodbye": {
        "en": "Session ended. Take care of yourself and your patients.",
        "pt": "Encerrando o sistema. Cuide-se e cuide bem dos seus pacientes.",
    },
    "interrupted": {
        "en": "Session interrupted by user.",
        "pt": "Programa interrompido pelo usuário.",
    },
}


def t(key: str, lang: str, **kwargs: object) -> str:
    """
    Translate a UI string key into the specified language.

    Falls back to English if the key or language is not found,
    then to the raw key name as a last resort.

    Args:
        key:    String identifier defined in STRINGS above.
        lang:   Language code — "en" or "pt".
        **kwargs: Named placeholders for format substitution.

    Returns:
        Translated and formatted string.

    Examples:
        t("menu_title", "en")                        → "Available Scales"
        t("question_of", "en", current=2, total=7)  → "Question 2 of 7"
    """
    entry = STRINGS.get(key, {})
    text = entry.get(lang) or entry.get("en") or key

    if kwargs:
        text = text.format(**kwargs)

    return text
