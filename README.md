# 🛡️ ArtifactGuard

**ArtifactGuard** is an automated digital forensics triage tool designed to parse, analyze, and report on browser artifacts. Built for incident responders and forensic analysts, it extracts key user activity from SQLite-based browser history databases and generates clean, professional HTML audit reports.

---

## 🚀 Key Features
* **Automated SQLite Parsing:** Connects directly to Chromium/Chrome `History` databases without requiring commercial forensic suites.
* **Timestamp Normalization:** Automatically converts cryptic Webkit/Chrome microsecond epochs into readable UTC timestamps.
* **Terminal & HTML Reporting:** Displays a quick ASCII preview in the terminal using `tabulate` while exporting a responsive HTML report for case documentation.
* **Modular Design:** Clean separation of concerns between database parsing logic and CLI execution/reporting.

---

## 📁 Project Architecture
```text
ArtifactGuard/
│
├── parser.py          # Core forensic parsing engine & timestamp converter
├── main.py            # CLI controller, display engine, & HTML report generator
├── requirements.txt   # Project dependencies
└── README.md          # Project documentation