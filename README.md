# ANIMA
### Clinical Psychological Scale Assessor

```
 █████╗ ███╗   ██╗██╗███╗   ███╗ █████╗
██╔══██╗████╗  ██║██║████╗ ████║██╔══██╗
███████║██╔██╗ ██║██║██╔████╔██║███████║
██╔══██║██║╚██╗██║██║██║╚██╔╝██║██╔══██║
██║  ██║██║ ╚████║██║██║ ╚═╝ ██║██║  ██║
╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝╚═╝     ╚═╝╚═╝  ╚═╝
```

> **Psychology meets technology.**  
> A professional CLI tool for applying validated clinical psychological scales,
> built as a portfolio project at the intersection of clinical psychology and software development.

---

## ⚕️ Ethical Notice

ANIMA is an **educational and research tool only**.  
It does **NOT** replace assessment, diagnosis, or treatment by a licensed mental health professional.  
If you or someone you know is in crisis, please contact a mental health professional or a crisis helpline immediately.

---

## 📋 Overview

ANIMA applies validated psychological screening scales interactively via the terminal,
scores responses automatically, and provides clinical interpretations based on established
severity ranges — all within a clean, professional CLI interface.

The project was developed to demonstrate how clinical psychology knowledge can be
systematically implemented using fundamental programming concepts.

---

## ✨ Features

| Feature | Description |
|---|---|
| 🧠 **3 validated scales** | PHQ-9, GAD-7, ISI — each with full clinical data |
| 🌐 **Bilingual** | Full English / Portuguese interface |
| 📊 **Auto-scoring** | Calculates total score and severity range automatically |
| ⚠️ **Clinical alerts** | Special alert for PHQ-9 item 9 (suicidal ideation) |
| 📈 **Reference ranges** | Visual table of all severity thresholds per scale |
| 📖 **Bibliographic reference** | Validated citations displayed with every result |
| 💾 **History** | Results saved locally in JSON |
| 📤 **CSV export** | One-command export compatible with Excel / LibreOffice |
| 🔒 **Ethical disclaimer** | Mandatory notice on every startup |
| 🖥️ **Cross-platform** | Linux · macOS · Windows |

---

## 🩺 Implemented Scales

### PHQ-9 — Patient Health Questionnaire-9
- **Area:** Depression
- **Items:** 9 · **Max score:** 27
- **Ranges:** Minimal / Mild / Moderate / Moderately Severe / Severe
- **Special:** Suicidal ideation alert on item 9
- **Reference:** Kroenke et al., J Gen Intern Med, 2001

### GAD-7 — Generalized Anxiety Disorder Scale-7
- **Area:** Anxiety
- **Items:** 7 · **Max score:** 21
- **Ranges:** Minimal / Mild / Moderate / Severe
- **Reference:** Spitzer et al., Arch Intern Med, 2006

### ISI — Insomnia Severity Index
- **Area:** Insomnia
- **Items:** 7 · **Max score:** 28
- **Ranges:** No Clinically Significant Insomnia / Subthreshold / Moderate Clinical / Severe Clinical
- **Reference:** Morin et al., Sleep, 2011

---

## 🖥️ Interface Preview

```
╔══════════════════════════════════════════════════════════╗
║                        A N I M A                        ║
║         Clinical Psychological Scale Assessor           ║
║              v1.0  ·  Educational & Research Use Only   ║
╚══════════════════════════════════════════════════════════╝

╭─────────────────── Available Scales ───────────────────╮
│  #  │ Code  │ Scale                        │ Area       │
├─────┼───────┼──────────────────────────────┼────────────┤
│  1  │ PHQ-9 │ Patient Health Questionnaire │ Depression │
│  2  │ GAD-7 │ Generalized Anxiety Disorder │ Anxiety    │
│  3  │ ISI   │ Insomnia Severity Index      │ Insomnia   │
╰─────────────────────────────────────────────────────────╯

Other options:  H History   E Export CSV   Q Quit
```

---

## 🚀 Installation

### Requirements
- Python **3.10+**
- pip

### 1 — Clone the repository

```bash
git clone https://github.com/ChaoticNoodley/anima.git
cd anima
```

### 2 — Create a virtual environment (recommended)

```bash
# Linux / macOS
python -m venv .venv
source .venv/bin/activate

# Fish shell (Arch Linux)
source .venv/bin/activate.fish

# Windows
.venv\Scripts\activate
```

### 3 — Install dependencies

```bash
pip install -r requirements.txt
```

### Alternative: system-wide via package manager (Arch Linux)

```bash
sudo pacman -S python-rich
```

---

## ▶️ Running ANIMA

```bash
python main.py
```

The first screen will ask you to select a language (English or Portuguese).

---

## 📁 Project Structure

```
anima/
│
├── main.py                  ← Entry point · application flow controller
│
├── data/
│   ├── scales.py            ← Scale definitions (questions, options, ranges)
│   └── i18n.py              ← All UI strings (EN + PT) · translation function t()
│
├── core/
│   └── engine.py            ← Business logic: scoring, interpretation, alerts
│
├── utils/
│   ├── display.py           ← Terminal UI layer (Rich) · presentation only
│   └── history.py           ← Persistence: JSON storage + CSV export
│
├── requirements.txt
└── README.md

# Generated at runtime:
├── anima_history.json       ← Local assessment history
└── anima_history.csv        ← Exported when using the E option
```

---

## 🧩 Architecture

ANIMA follows a layered architecture with strict separation of concerns:

```
┌─────────────────────────────────┐
│           main.py               │  Application flow (orchestration)
├─────────────────────────────────┤
│         utils/display.py        │  Presentation layer (Rich UI)
├──────────────┬──────────────────┤
│  core/       │  data/           │
│  engine.py   │  scales.py       │  Business logic + Data
│              │  i18n.py         │
├──────────────┴──────────────────┤
│         utils/history.py        │  Persistence layer (JSON/CSV)
└─────────────────────────────────┘
```

**Key design decisions:**
- `engine.py` never imports from `display.py` — logic is fully decoupled from UI
- All user-facing strings live in `i18n.py` — zero hardcoded text elsewhere
- Scale data in `scales.py` is bilingual — adding a new language requires only new keys
- `build_result()` returns a plain dict — the display layer receives finished data, never computes

---

## 🔭 Roadmap

### Near-term
- [ ] Add more scales: BDI-II, BAI, PCL-5, AUDIT, DASS-21, EPDS
- [ ] PDF report generation with `reportlab`
- [ ] Score trend chart with `matplotlib`
- [ ] SQLite database replacing JSON (`sqlite3`)

### Medium-term
- [ ] Desktop GUI with PyQt6 or CustomTkinter
- [ ] Multi-user support with hashed login (`bcrypt`)
- [ ] Clinical dashboard with patient management
- [ ] Local data encryption (Fernet/AES)

### Long-term
- [ ] REST API with FastAPI — interoperability with external systems
- [ ] Web application (Django or Flask)
- [ ] HL7/FHIR integration for hospital systems
- [ ] PostgreSQL multi-user database

---

## 🛠️ Tech Stack

| Component | Technology |
|---|---|
| Language | Python 3.10+ |
| Terminal UI | [Rich](https://github.com/Textualize/rich) |
| Data storage | JSON (stdlib) |
| CSV export | csv (stdlib) |
| Date/time | datetime (stdlib) |

---

## 📚 References

**PHQ-9:**
Kroenke K, Spitzer RL, Williams JBW. The PHQ-9: Validity of a brief depression severity measure. *J Gen Intern Med.* 2001;16(9):606–613.

**GAD-7:**
Spitzer RL, Kroenke K, Williams JBW, Löwe B. A brief measure for assessing generalized anxiety disorder. *Arch Intern Med.* 2006;166(10):1092–1097.

**ISI:**
Morin CM, Belleville G, Bélanger L, Ivers H. The Insomnia Severity Index: Psychometric indicators to detect insomnia cases and evaluate treatment response. *Sleep.* 2011;34(5):601–608.

---

## 👤 Author

Developed as a portfolio project demonstrating clinical psychology applied to software development.

> *"The goal is not to replace the clinician — it is to give the clinician better tools."*

---

## 📄 License

MIT License — see [LICENSE](LICENSE) for details.
