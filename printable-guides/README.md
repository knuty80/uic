# Printable Guides Workflow

This directory contains the assets used to generate high-fidelity, printable PDFs for the [League Name] Umpire Program.

## Directory Structure
- `/html`: Contains the source HTML files with CSS styling optimized for print.
- `/pdf`: Contains the final exported PDF documents ready for distribution.

## PDF Generation Process (Linux-Optimized)
This workflow was developed on a **Linux system** and assumes the presence of a terminal and Python 3. For users on other operating systems, these commands may require minor adjustments.

To maintain local resource integrity and ensure all styles load correctly, follow these steps:

1. **Serve the Files:** Use an ephemeral web service to serve the HTML directory. From within this directory, run:
   ```bash
   python3 -m http.server 8000
   ```
2. **Access via Browser:** Navigate to `http://localhost:8000/html/[filename].html`.
3. **Print to PDF:** Use the browser's "Print" function (Ctrl+P / Cmd+P) and select **"Save as PDF"**.
   - **Important:** Ensure "Background Graphics" is checked in the print settings to preserve the design aesthetics.

This workflow was established by the developer to ensure a premium look-and-feel that standard Markdown-to-PDF converters cannot achieve.
