#!/usr/bin/env python3
import os
import yaml
import re

def render_template(template_content, context):
    """
    Simple Jinja2-like renderer that replaces {{ key }} with value from context.
    Supports basic {% if key %}...{% else %}...{% endif %} blocks.
    """
    # Handle if/else blocks
    def handle_if(match):
        cond = match.group(1).strip()
        true_body = match.group(2)
        false_body = match.group(3) if match.group(3) else ""
        if context.get(cond) and context.get(cond) != f"[{cond.replace('_', ' ').title()}]":
            return true_body.strip()
        return false_body.strip()

    template_content = re.sub(r"\{%\s*if\s+(.*?)\s*%\}(.*?)(?:\{%\s*else\s*%\}(.*?))?\{%\s*endif\s*%\}", handle_if, template_content, flags=re.DOTALL)

    # Handle standard variables
    def replace_var(match):
        key = match.group(1).strip()
        return str(context.get(key, match.group(0)))
    
    return re.sub(r"\{\{\s*(.*?)\s*\}\}", replace_var, template_content)

def main():
    # 1. Load context
    config_path = "league_info.yaml"
    if not os.path.exists(config_path):
        print(f"Error: {config_path} not found. Copy league_info.yaml.template and fill it out.")
        return

    with open(config_path, "r") as f:
        context = yaml.safe_load(f)

    # 2. Files to process
    # Pairs of (source_template, output_filename)
    files_to_render = [
        ("README.md", "README.rendered.md"),
        ("UIC_HANDBOOK.md", "UIC_HANDBOOK.rendered.md"),
        ("templates/html/handbook-template.html", "handbook-template.rendered.html"),
        ("templates/html/ump-guide-cheat-sheet.html", "ump-guide-cheat-sheet.rendered.html"),
        ("templates/html/scorekeepers-cheat-sheet.html", "scorekeepers-cheat-sheet.rendered.html")
    ]

    print(f"--- {{ league_name if context.get('league_name') else 'League' }} Rendering Engine ---")
    
    # 3. Create output directory
    output_dir = "rendered"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # 4. Process files
    for src, dst in files_to_render:
        if not os.path.exists(src):
            print(f"[-] Skipping: {src} (not found)")
            continue
            
        dst_path = os.path.join(output_dir, dst)
        print(f"[+] Rendering: {src} -> {dst_path}")
        with open(src, "r") as f:
            template = f.read()
        
        rendered = render_template(template, context)
        
        with open(dst_path, "w") as f:
            f.write(rendered)

    print(f"\n[!] Success: All guides have been rendered in the '{output_dir}/' folder.")
    print(f"[!] Instruction: Open '{output_dir}/*.rendered.html' files in Chrome to 'Print to PDF'.")

if __name__ == "__main__":
    main()
