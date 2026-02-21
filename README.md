# 🚀 WebVulnScanner v2.0

A Python-based educational web vulnerability scanner that performs:

- SQL Injection Detection (Form-based)
- XSS Detection (Basic reflection)
- Sensitive File Checking
- Severity Classification
- HTML Report Generation
- Progress Bar Tracking

---

## ⚠️ Disclaimer

This tool is created strictly for:

- Educational purposes
- Testing applications you own
- Authorized security testing only

Do NOT use this tool on websites without permission.

---

# 📥 Installation

## 1️⃣ Clone the Repository

Using SSH:

```bash
git clone git@github.com:thoufeektr30-create/WebVulnScanner.git
cd WebVulnScanner
```

Or using HTTPS:

```bash
git clone https://github.com/thoufeektr30-create/WebVulnScanner.git
cd WebVulnScanner
```

---

## 2️⃣ Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
pip install tqdm
```

---

# ▶️ Usage

Run the scanner:

```bash
python main.py --target http://testphp.vulnweb.com
```

Example:

```bash
python main.py --target http://localhost/dvwa
```

---

# 📊 Example Output

```
Collecting links...

Total URLs to scan: 25

Starting scan...

Scanning: 100%|████████████████████| 25/25

===== Scan Summary =====
Total forms tested: 12
SQL Injection found: 2
XSS found: 1

Report saved as report_20260221_223015.html
```

---

# 📄 HTML Report

After scanning completes, a report file is generated automatically:

```
report_YYYYMMDD_HHMMSS.html
```

Open it using:

```bash
xdg-open report_YYYYMMDD_HHMMSS.html
```

---

# 🧠 Features

- Multi-page crawling
- Form detection & submission
- SQL error pattern detection
- Reflected XSS detection
- Severity classification (HIGH / MEDIUM)
- Progress bar using tqdm
- HTML report generation

---

# 🏗 Project Structure

```
WebVulnScanner/
│
├── main.py
├── crawler.py
├── form_scanner.py
├── detectors/
│   ├── sqli_detector.py
│   ├── xss_detector.py
├── reporting/
│   ├── reporter.py
├── utils/
│   ├── severity.py
├── requirements.txt
└── README.md
```

---

# 🔮 Future Improvements

- Threaded scanning with CLI control
- JSON report export
- Logging system
- Directory brute-force module
- Security header scanning
- Rate limiting

---

# 👨‍💻 Author

Thoufeek T R  
GitHub: https://github.com/thoufeektr30-create

---

# ⭐ Support

If you found this project useful:

- Star the repository
- Fork it
- Improve it
- Contribute

Happy Ethical Hacking 🚀
