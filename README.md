# {{ league_name }}: Umpire Coordinator (UIC) Handbook

This repository serves as the single source of truth for the {{ league_name }} Umpire Coordinator role. It is designed to ensure continuity and excellence in the umpire program for any Little League or youth baseball organization.

## Key Documents
- **[UIC_HANDBOOK.md](UIC_HANDBOOK.md):** The primary manual covering philosophy, RefTown mastery, pitch count mandates, and field mechanics.
- **[templates/](templates/):** A folder containing HTML sources and final PDF versions of tactical cheat sheets and field guides.

## Core Philosophy
The UIC serves as the **shield** for the umpire pool, protector of arm safety via **Pitch Count Mandates**, and the architect of a respectful, volunteer-driven community.

## Developer Notes
- **Operating System:** This project was developed and is optimized for a **Linux environment**.
- Documentation is maintained in Markdown for version control parity.
- Complex tactical guides are built in HTML/CSS for premium aesthetics and converted to PDF via localized browser-print services (see `templates/README.md`).
- **Local Logs:** Procedural changes are logged in `MISSION_LOG.md` (maintained locally, excluded from Git).

## 🚀 Quick Start (Board Members / Non-Technical)

If you just want to get the documents without using any code:
1. **Browse the [distribution/](distribution/) folder.**
2. **Handbook:** Copy the text from `GENERIC_HANDBOOK.md` into a new **Google Doc**.
3. **Customization:** Use "Find & Replace" in your document to replace placeholders like `[League Name]`.
4. **Print:** Export your Google Doc as a PDF.

No terminal, Git, or Python required!

## ⚙️ Advanced Customization & Rendering (For Tech UICs)

### 1. Configure Your League
1. Copy `league_info.yaml.template` to `league_info.yaml`.
2. Open `league_info.yaml` and fill in your league-specific details (ID, rates, contact info).

### 2. Render Documents
If you have Python and `PyYAML` installed, you can automatically inject your data into the documents:
```bash
python3 render_guides.py
```
This will create a **`rendered/`** folder containing:
- `UIC_HANDBOOK.rendered.md`: Branded handbook.
- `handbook-template.rendered.html`: Branded HTML (Best for Google Docs import).
- `ump-guide-cheat-sheet.rendered.html`: Branded tactical cheat sheet.

### 3. Generate PDFs
1. Open any `.rendered.html` file from the `rendered/` folder in your browser.
2. Press `Ctrl + P` (Print) -> Select **Save as PDF**.

---
3. **Template Parity:** The handbook uses placeholders like `[League Name]` which correspond to the keys in your configuration file.

---
*Template Version. Dedicated to Volunteer Excellence.*
