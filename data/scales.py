# =============================================================================
# data/scales.py
# Validated psychological scale definitions
#
# This file acts as an in-memory database using nested Python dictionaries.
# Each scale is a self-contained dict with questions, options, scoring ranges,
# bilingual content (EN/PT), references, and special clinical alerts.
#
# Data structure rationale:
#   dict[str, dict]  →  keyed by scale ID ("phq9", "gad7", "isi")
#   Each scale dict  →  contains all metadata, questions, and ranges
#   Each question    →  dict with id, EN text, PT text, optional custom options
#   Each range       →  dict with min/max thresholds, labels, colors, notes
# =============================================================================

SCALES: dict[str, dict] = {

    # -------------------------------------------------------------------------
    # PHQ-9 — Patient Health Questionnaire-9
    # Gold-standard screening tool for depressive symptoms
    # -------------------------------------------------------------------------
    "phq9": {
        "id": "phq9",
        "name": "PHQ-9",
        "full_name": "Patient Health Questionnaire-9",

        # Bilingual category labels
        "category":    "Depression",
        "category_pt": "Depressão",

        # Bilingual descriptions
        "description": (
            "The PHQ-9 is one of the most widely used tools worldwide for "
            "screening depressive symptoms in clinical and hospital settings. "
            "It assesses the frequency of 9 symptoms over the past 2 weeks, "
            "aligned with DSM-5 diagnostic criteria for Major Depressive Disorder."
        ),
        "description_pt": (
            "O PHQ-9 é uma das ferramentas mais utilizadas mundialmente para "
            "rastreio de sintomas depressivos em contextos clínicos e hospitalares. "
            "Avalia a frequência de 9 sintomas nas últimas 2 semanas, alinhados "
            "aos critérios diagnósticos do DSM-5 para Transtorno Depressivo Maior."
        ),

        # Bilingual instructions
        "instruction": (
            "Over the last 2 weeks, how often have you been bothered "
            "by any of the following problems?"
        ),
        "instruction_pt": (
            "Nas últimas 2 semanas, com que frequência você foi incomodado(a) "
            "por algum dos problemas abaixo?"
        ),

        # Questions — each contains EN and PT text
        "questions": [
            {"id": 1,
             "text":    "Little interest or pleasure in doing things",
             "text_pt": "Pouco interesse ou prazer em fazer as coisas"},
            {"id": 2,
             "text":    "Feeling down, depressed, or hopeless",
             "text_pt": "Sentir-se para baixo, deprimido(a) ou sem perspectiva"},
            {"id": 3,
             "text":    "Trouble falling or staying asleep, or sleeping too much",
             "text_pt": "Dificuldade para adormecer ou permanecer dormindo, ou dormir demais"},
            {"id": 4,
             "text":    "Feeling tired or having little energy",
             "text_pt": "Sentir-se cansado(a) ou com pouca energia"},
            {"id": 5,
             "text":    "Poor appetite or overeating",
             "text_pt": "Falta de apetite ou comer em excesso"},
            {"id": 6,
             "text":    "Feeling bad about yourself — or that you are a failure or have let yourself or your family down",
             "text_pt": "Sentir-se mal consigo mesmo(a), ou achar que é um fracasso ou que decepcionou sua família ou a você mesmo(a)"},
            {"id": 7,
             "text":    "Trouble concentrating on things, such as reading the newspaper or watching television",
             "text_pt": "Dificuldade para se concentrar nas coisas, como ler o jornal ou ver televisão"},
            {"id": 8,
             "text":    "Moving or speaking so slowly that other people could have noticed — or the opposite, being so fidgety or restless that you have been moving around a lot more than usual",
             "text_pt": "Mover-se ou falar tão lentamente que as outras pessoas podem ter notado. Ou ao contrário, ficar tão agitado(a) que você fica andando de um lado para o outro mais do que de costume"},
            {"id": 9,
             "text":    "Thoughts that you would be better off dead, or thoughts of hurting yourself in some way",
             "text_pt": "Pensar em se machucar de alguma maneira ou que seria melhor estar morto(a)"},
        ],

        # Shared response options — tuples of (score_value, EN_label, PT_label)
        "options": [
            (0, "Not at all",          "Nenhuma vez"),
            (1, "Several days",        "Vários dias"),
            (2, "More than half the days", "Mais da metade dos dias"),
            (3, "Nearly every day",    "Quase todos os dias"),
        ],

        # Severity ranges with bilingual labels and clinical notes
        "ranges": [
            {"min": 0,  "max": 4,
             "label": "Minimal",  "label_pt": "Mínimo",  "color": "green",
             "note":    "Minimal or no depressive symptoms.",
             "note_pt": "Sintomas depressivos mínimos ou ausentes."},

            {"min": 5,  "max": 9,
             "label": "Mild",     "label_pt": "Leve",    "color": "yellow",
             "note":    "Mild symptoms. Watchful waiting and psychoeducation may be indicated.",
             "note_pt": "Sintomas leves. Monitoramento e psicoeducação podem ser indicados."},

            {"min": 10, "max": 14,
             "label": "Moderate", "label_pt": "Moderado", "color": "dark_orange",
             "note":    "Moderate symptoms. A more thorough clinical evaluation is recommended.",
             "note_pt": "Sintomas moderados. Avaliação clínica aprofundada é recomendada."},

            {"min": 15, "max": 19,
             "label": "Moderately Severe", "label_pt": "Moderadamente Grave", "color": "red",
             "note":    "Moderately severe symptoms. Active treatment is indicated.",
             "note_pt": "Sintomas moderadamente graves. Intervenção terapêutica indicada."},

            {"min": 20, "max": 27,
             "label": "Severe",   "label_pt": "Grave",   "color": "bright_red",
             "note":    "Severe symptoms. Immediate evaluation and intervention are strongly recommended.",
             "note_pt": "Sintomas graves. Avaliação e intervenção imediata recomendadas."},
        ],

        "max_score": 27,

        "reference": (
            "Kroenke K, Spitzer RL, Williams JBW. The PHQ-9: Validity of a "
            "brief depression severity measure. J Gen Intern Med. 2001;16(9):606–613."
        ),

        # Special alert for item 9 (suicidal ideation)
        "special_alerts": {
            9: {
                "threshold": 1,
                "message": (
                    "⚠  Item 9 screens for thoughts of self-harm or death. "
                    "Any score above zero warrants immediate clinical evaluation "
                    "by a qualified mental health professional."
                ),
                "message_pt": (
                    "⚠  A questão 9 avalia pensamentos de automutilação ou morte. "
                    "Qualquer pontuação acima de zero indica necessidade de avaliação "
                    "clínica imediata por profissional habilitado."
                ),
            }
        },
    },

    # -------------------------------------------------------------------------
    # GAD-7 — Generalized Anxiety Disorder Scale-7
    # -------------------------------------------------------------------------
    "gad7": {
        "id": "gad7",
        "name": "GAD-7",
        "full_name": "Generalized Anxiety Disorder Scale-7",

        "category":    "Anxiety",
        "category_pt": "Ansiedade",

        "description": (
            "The GAD-7 is a brief, widely validated scale for screening and "
            "measuring the severity of Generalized Anxiety Disorder. "
            "It evaluates the presence and frequency of 7 anxiety symptoms "
            "over the past 2 weeks."
        ),
        "description_pt": (
            "O GAD-7 é uma escala breve amplamente validada para rastreio e "
            "mensuração da gravidade do Transtorno de Ansiedade Generalizada. "
            "Avalia a presença e frequência de 7 sintomas ansiosos nas últimas 2 semanas."
        ),

        "instruction": (
            "Over the last 2 weeks, how often have you been bothered "
            "by the following problems?"
        ),
        "instruction_pt": (
            "Nas últimas 2 semanas, com que frequência você foi incomodado(a) "
            "por algum dos problemas a seguir?"
        ),

        "questions": [
            {"id": 1,
             "text":    "Feeling nervous, anxious, or on edge",
             "text_pt": "Sentir-se nervoso(a), ansioso(a) ou no limite"},
            {"id": 2,
             "text":    "Not being able to stop or control worrying",
             "text_pt": "Não conseguir parar ou controlar as preocupações"},
            {"id": 3,
             "text":    "Worrying too much about different things",
             "text_pt": "Preocupar-se demais com diferentes coisas"},
            {"id": 4,
             "text":    "Trouble relaxing",
             "text_pt": "Dificuldade para relaxar"},
            {"id": 5,
             "text":    "Being so restless that it is hard to sit still",
             "text_pt": "Ficar tão agitado(a) que se torna difícil permanecer sentado(a) quieto(a)"},
            {"id": 6,
             "text":    "Becoming easily annoyed or irritable",
             "text_pt": "Ficar facilmente aborrecido(a) ou irritado(a)"},
            {"id": 7,
             "text":    "Feeling afraid, as if something awful might happen",
             "text_pt": "Sentir medo como se algo terrível fosse acontecer"},
        ],

        "options": [
            (0, "Not at all",              "Nenhuma vez"),
            (1, "Several days",            "Vários dias"),
            (2, "More than half the days", "Mais da metade dos dias"),
            (3, "Nearly every day",        "Quase todos os dias"),
        ],

        "ranges": [
            {"min": 0,  "max": 4,
             "label": "Minimal",  "label_pt": "Mínimo",  "color": "green",
             "note":    "Minimal or no anxiety symptoms.",
             "note_pt": "Sintomas ansiosos mínimos ou ausentes."},

            {"min": 5,  "max": 9,
             "label": "Mild",     "label_pt": "Leve",    "color": "yellow",
             "note":    "Mild anxiety. Monitoring and coping strategies may be helpful.",
             "note_pt": "Ansiedade leve. Acompanhamento e técnicas de manejo podem ajudar."},

            {"min": 10, "max": 14,
             "label": "Moderate", "label_pt": "Moderado", "color": "dark_orange",
             "note":    "Moderate anxiety. Evaluation by a mental health professional is recommended.",
             "note_pt": "Ansiedade moderada. Avaliação por profissional de saúde mental recomendada."},

            {"min": 15, "max": 21,
             "label": "Severe",   "label_pt": "Grave",   "color": "bright_red",
             "note":    "Severe anxiety. Clinical assessment and intervention are indicated.",
             "note_pt": "Ansiedade grave. Avaliação clínica e intervenção indicadas."},
        ],

        "max_score": 21,

        "reference": (
            "Spitzer RL, Kroenke K, Williams JBW, Löwe B. A brief measure for "
            "assessing generalized anxiety disorder. Arch Intern Med. 2006;166(10):1092–1097."
        ),

        "special_alerts": {},
    },

    # -------------------------------------------------------------------------
    # ISI — Insomnia Severity Index
    # -------------------------------------------------------------------------
    "isi": {
        "id": "isi",
        "name": "ISI",
        "full_name": "Insomnia Severity Index",

        "category":    "Insomnia",
        "category_pt": "Insônia",

        "description": (
            "The ISI is a widely used scale for assessing the nature, severity, "
            "and daytime impact of insomnia. Its 7 items evaluate difficulty "
            "initiating and maintaining sleep, early awakening, sleep satisfaction, "
            "and functional impairment over the past 2 weeks."
        ),
        "description_pt": (
            "O ISI é uma escala amplamente utilizada para avaliar a natureza, "
            "gravidade e impacto da insônia. Composto por 7 itens, avalia a "
            "dificuldade para iniciar e manter o sono, a satisfação com o sono "
            "e o impacto funcional nas últimas 2 semanas."
        ),

        "instruction": (
            "For each item, please rate the current (i.e., last 2 weeks) "
            "severity of your insomnia problem."
        ),
        "instruction_pt": (
            "Para cada questão, selecione a opção que melhor descreve sua "
            "experiência de sono nas últimas 2 semanas."
        ),

        # ISI uses per-question custom options
        "questions": [
            {
                "id": 1,
                "text":    "Difficulty FALLING asleep",
                "text_pt": "Dificuldade para INICIAR o sono",
                "custom_options": [
                    (0, "None",      "Nenhuma"),
                    (1, "Mild",      "Leve"),
                    (2, "Moderate",  "Moderada"),
                    (3, "Severe",    "Grave"),
                    (4, "Very Severe", "Muito grave"),
                ],
            },
            {
                "id": 2,
                "text":    "Difficulty STAYING asleep (waking up during the night)",
                "text_pt": "Dificuldade para MANTER o sono (acordar durante a noite)",
                "custom_options": [
                    (0, "None",      "Nenhuma"),
                    (1, "Mild",      "Leve"),
                    (2, "Moderate",  "Moderada"),
                    (3, "Severe",    "Grave"),
                    (4, "Very Severe", "Muito grave"),
                ],
            },
            {
                "id": 3,
                "text":    "Problem waking up TOO EARLY",
                "text_pt": "Problema de acordar CEDO demais",
                "custom_options": [
                    (0, "None",      "Nenhum"),
                    (1, "Mild",      "Leve"),
                    (2, "Moderate",  "Moderado"),
                    (3, "Severe",    "Grave"),
                    (4, "Very Severe", "Muito grave"),
                ],
            },
            {
                "id": 4,
                "text":    "How SATISFIED / dissatisfied are you with your CURRENT sleep pattern?",
                "text_pt": "Quão SATISFEITO(A) você está com seu padrão de sono ATUAL?",
                "custom_options": [
                    (0, "Very Satisfied",    "Muito satisfeito(a)"),
                    (1, "Satisfied",         "Satisfeito(a)"),
                    (2, "Neutral",           "Neutro(a)"),
                    (3, "Dissatisfied",      "Insatisfeito(a)"),
                    (4, "Very Dissatisfied", "Muito insatisfeito(a)"),
                ],
            },
            {
                "id": 5,
                "text":    "How NOTICEABLE to others do you think your sleep problem is in terms of impairing the quality of your life? (fatigue, mood, ability to function, memory, concentration, etc.)",
                "text_pt": "Em que medida os problemas de sono INTERFEREM no seu funcionamento diário? (cansaço, humor, desempenho, memória etc.)",
                "custom_options": [
                    (0, "Not at all",   "Nada"),
                    (1, "A little",     "Um pouco"),
                    (2, "Somewhat",     "De alguma forma"),
                    (3, "Much",         "Muito"),
                    (4, "Very Much",    "Extremamente"),
                ],
            },
            {
                "id": 6,
                "text":    "How WORRIED / distressed are you about your current sleep problem?",
                "text_pt": "Em que medida os seus problemas de sono são PERCEPTÍVEIS para os outros em termos de comprometimento da qualidade de vida?",
                "custom_options": [
                    (0, "Not at all",   "Nada"),
                    (1, "A little",     "Um pouco"),
                    (2, "Somewhat",     "De alguma forma"),
                    (3, "Much",         "Muito"),
                    (4, "Very Much",    "Extremamente"),
                ],
            },
            {
                "id": 7,
                "text":    "To what extent do you consider your sleep problem to INTERFERE with your daily functioning?",
                "text_pt": "Em que medida você está PREOCUPADO(A) com seus problemas de sono?",
                "custom_options": [
                    (0, "Not at all",   "Nada"),
                    (1, "A little",     "Um pouco"),
                    (2, "Somewhat",     "De alguma forma"),
                    (3, "Much",         "Muito"),
                    (4, "Very Much",    "Extremamente"),
                ],
            },
        ],

        "options": None,  # ISI uses per-question custom_options

        "ranges": [
            {"min": 0,  "max": 7,
             "label": "No Clinically Significant Insomnia", "label_pt": "Ausência de insônia clinicamente significativa",
             "color": "green",
             "note":    "No significant insomnia. Sleep considered within normal limits.",
             "note_pt": "Sem insônia significativa. Sono considerado dentro da normalidade."},

            {"min": 8,  "max": 14,
             "label": "Subthreshold Insomnia", "label_pt": "Insônia Subclínica",
             "color": "yellow",
             "note":    "Mild insomnia. Sleep hygiene and behavioral interventions may help.",
             "note_pt": "Insônia leve. Higiene do sono e intervenções comportamentais podem ajudar."},

            {"min": 15, "max": 21,
             "label": "Moderate Clinical Insomnia", "label_pt": "Insônia Clínica Moderada",
             "color": "dark_orange",
             "note":    "Moderate clinical insomnia. Specialist evaluation is recommended.",
             "note_pt": "Insônia clínica moderada. Avaliação por especialista recomendada."},

            {"min": 22, "max": 28,
             "label": "Severe Clinical Insomnia", "label_pt": "Insônia Clínica Grave",
             "color": "bright_red",
             "note":    "Severe clinical insomnia. Immediate evaluation and treatment are indicated.",
             "note_pt": "Insônia grave. Avaliação e intervenção imediata recomendadas."},
        ],

        "max_score": 28,

        "reference": (
            "Morin CM, Belleville G, Bélanger L, Ivers H. The Insomnia Severity Index: "
            "Psychometric indicators to detect insomnia cases and evaluate treatment response. "
            "Sleep. 2011;34(5):601–608."
        ),

        "special_alerts": {},
    },
}
