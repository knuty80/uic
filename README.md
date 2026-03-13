# {{ league_name }}: Umpire Coordinator (UIC) Handbook
*Modern. Interactive. Fact-Focused.*

This repository is the **Single Source of Truth** for the {{ league_name }} Umpire Coordinator. It has been modernized with a "Zero-Terminal" interactive dashboard to ensure data integrity and ease of use for both tech-savvy and non-technical board members.

## 📁 Project Structure
- **[UIC_HANDBOOK.md](UIC_HANDBOOK.md)**: The master source file. All policy updates, links, and tactical guides are maintained here.
- **[index.html](index.html)**: The **UIC Studio Dashboard**. A client-side application that renders the handbook, handles variable replacement, and exports PDFs/Google Docs content.
- **[league_info.yaml](.gitignore)**: Your local, PII-sensitive configuration (ignored by Git to protect your privacy).

## 🚀 Quick Start (Browser-Based)
The handbook now runs entirely in your web browser. No Python or command line required.

1.  **Open the Studio**: Open `index.html` in Chrome or Edge.
2.  **Load Content**: 
    - Click **"Load Handbook Content"** and select `UIC_HANDBOOK.md`.
    - Click **"Import League YAML"** and select your `league_info.yaml` (or manually fill the sidebar).
3.  **Customize**: All variables (like `{{ league_name }}` or `{{ rate_solo }}`) are automatically detected and mapped to sidebar inputs.
4.  **Export**:
    - **PDF**: Use the "Export to PDF" button for high-fidelity printing.
    - **Google Docs**: Use "Copy for Google Docs" to paste perfectly formatted content into a cloud document for distribution.

## 🌐 Hosting on GitHub Pages
This repository is designed for zero-config hosting on GitHub Pages:

1.  **Enable Pages**: Go to **Settings** -> **Pages** in this GitHub Repo.
2.  **Select Branch**: Choose `main` (or your active branch) and the `/(root)` folder. Click **Save**.
3.  **Access Everywhere**: Your customized Studio will be live at `https://your-username.github.io/uic/`.

**Why this is better**: You can share the link with your successor or fellow board members. They can use the dashboard to generate documents instantly without downloading a single file.

## 🔒 Privacy & PII Protection
- **Client-Side Only**: Your league data (`league_info.yaml`) never touches a server. All rendering happens locally in your browser.
- **Git Protection**: The `league_info.yaml` file is automatically ignored by Git to prevent accidental leaks of payment rates or contact information to the public web.

## 🛠️ Maintenance & Updates
To update the handbook content or tactical guides:
1. Edit the master **[UIC_HANDBOOK.md](UIC_HANDBOOK.md)**.
2. The changes will automatically reflect in the Studio the next time you load the file.
3. No redundant folders or "templates" are required—the Markdown source *is* the template.

---
*Dedicated to Volunteer Excellence. Branded for {{ league_name }}.*
