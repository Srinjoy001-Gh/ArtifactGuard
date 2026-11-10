import argparse
import os
from tabulate import tabulate
from jinja2 import Template
from parser import parse_chrome_history

# Professional HTML Report Template
HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>ArtifactGuard Forensic Report</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 40px; background-color: #f4f6f9; color: #333; }
        h1 { color: #2c3e50; }
        table { width: 100%; border-collapse: collapse; background: #fff; margin-top: 20px; box-shadow: 0 2px 5px rgba(0,0,0,0.1); }
        th, td { padding: 12px 15px; border: 1px solid #ddd; text-align: left; font-size: 14px; }
        th { background-color: #2c3e50; color: white; }
        tr:nth-child(even) { background-color: #f9f9f9; }
    </style>
</head>
<body>
    <h1>ArtifactGuard Forensic Report</h1>
    <p><strong>Generated Artifact:</strong> Browser History Triage</p>
    {{ table_html | safe }}
</body>
</html>
"""

def main():
    parser = argparse.ArgumentParser(description="ArtifactGuard - Automated Browser Artifact Triage")
    parser.add_argument("--input", required=True, help="Path to Chrome History SQLite file")
    args = parser.parse_args()

    if not os.path.exists(args.input):
        print(f"[!] Error: File '{args.input}' not found.")
        return

    print(f"[*] Parsing artifact: {args.input}...")
    df = parse_chrome_history(args.input)

    if df is not None and not df.empty:
        print("\n--- Forensics Summary (Top 10 Entries) ---")
        print(tabulate(df.head(10), headers='keys', tablefmt='psql', showindex=False))

        # Generate HTML Report
        table_html = df.to_html(index=False, classes='artifact-table')
        rendered_html = Template(HTML_TEMPLATE).render(table_html=table_html)
        
        report_filename = "artifact_guard_report.html"
        with open(report_filename, "w", encoding="utf-8") as f:
            f.write(rendered_html)
            
        print(f"\n[+] Success! HTML report saved successfully as '{report_filename}'.")
    else:
        print("[!] No data found or failed to parse the history database.")

if __name__ == "__main__":
    main()