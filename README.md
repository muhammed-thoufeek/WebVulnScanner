# 🛡 WebVulnScanner v3.0

WebVulnScanner v3.0 is a modular Python-based web security assessment tool designed for educational and authorized testing environments.

It performs form-based SQL Injection detection, reflected XSS detection, safe directory enumeration, multi-threaded scanning, and generates structured HTML and JSON reports.

---

## ⚠️ Disclaimer

This tool is created strictly for:

- Educational purposes
- Testing applications you own
- Authorized security assessments only

Do NOT use this tool against websites without explicit permission.

---

# 🚀 Features

- ✅ Form-based SQL Injection detection
- ✅ Reflected XSS detection
- ✅ Multi-threaded scanning engine
- ✅ CLI-configurable threads, timeout, and delay
- ✅ HTML report generation
- ✅ JSON report export
- ✅ Logging system (scanner.log)
- ✅ Safe directory enumeration module
- ✅ Severity classification system
- ✅ Progress bar with tqdm

---

# 🧱 Project Structure

```
WebVulnScanner/
│
├── main.py
├── crawler.py
├── form_scanner.py
│
├── detectors/
│   ├── sqli_detector.py
│   ├── xss_detector.py
│
├── web_modules/
│   ├── directory_enum.py
│
├── reporting/
│   ├── reporter.py
│   ├── json_reporter.py
│
├── utils/
│   ├── banner.py
│   ├── severity.py
│
├── wordlists/
│   ├── common_dirs.txt
│
├── scanner.log
└── README.md
```

---

# 📥 Installation

## 1️⃣ Clone the Repository

### Using SSH
```bash
git clone git@github.com:thoufeektr30-create/WebVulnScanner.git
cd WebVulnScanner
```

### Using HTTPS
```bash
git clone https://github.com/thoufeektr30-create/WebVulnScanner.git
cd WebVulnScanner
```

---

## 2️⃣ Create Virtual Environment (Recommended)

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 3️⃣ Install Required Packages

```bash
pip install requests beautifulsoup4 tqdm
```

---

# ▶️ Usage

## Basic Scan

```bash
python main.py --target http://testphp.vulnweb.com
```

---

## Advanced Scan Example

```bash
python main.py \
    --target http://testphp.vulnweb.com \
    --threads 8 \
    --timeout 3 \
    --delay 0.5 \
    --json \
    --dirscan
```

---

# 🛠 CLI Options

| Option | Description |
|--------|-------------|
| `--target` | Target URL (Required) |
| `--threads` | Number of concurrent threads (Default: 5) |
| `--timeout` | HTTP request timeout in seconds (Default: 5) |
| `--delay` | Delay between requests (Default: 0.5) |
| `--json` | Generate JSON report |
| `--dirscan` | Enable directory enumeration |

---

# 📊 Example Output

```
WebVulnScanner v3.0
Educational Security Scanner

Collecting links...

Total URLs to scan: 25

Starting scan...

100%|████████████████████████████████| 25/25

===== Scan Summary =====
Total forms tested: 18
SQL Injection found: 0
XSS found: 11

Report saved as report_20260222_100614.html
Scan completed successfully.
```

---

# 📄 Reports

After scan completion:

- HTML report is generated automatically:
  ```
  report_YYYYMMDD_HHMMSS.html
  ```

- If `--json` flag is used:
  ```
  report_YYYYMMDD_HHMMSS.json
  ```

---

# 📝 Logging

All vulnerability detections and errors are logged in:

```
scanner.log
```

---

# 🔐 Educational Scope

This project demonstrates:

- HTTP request automation
- Form parsing & payload injection
- Vulnerability detection logic
- Concurrent execution (ThreadPoolExecutor)
- CLI tool engineering
- Logging and reporting systems
- Modular software architecture

---

# 🧠 Future Improvements

- Nmap integration module
- Authentication handling
- Deeper crawling logic
- Response diff engine
- Subdomain discovery
- Export to PDF reports

---

# 👨‍💻 Author

Thoufeek T R  
GitHub: https://github.com/thoufeektr30-create

---

# ⭐ Support

If you found this project useful:

- Star ⭐ the repository
- Fork it
- Improve it
- Contribute

Happy Ethical Hacking 🚀
