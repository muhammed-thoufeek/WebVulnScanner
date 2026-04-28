# 🔍 WebVulnScanner

A Python-based web vulnerability scanner designed to detect common security flaws such as **SQL Injection (SQLi)**, **Cross-Site Scripting (XSS)**, insecure HTTP headers, and weak form handling.

> ⚠️ This tool is developed for **educational and ethical testing purposes only**.

---

## 🚀 Features

* 🔎 **Website Crawling** – Automatically discovers links and forms
* 💉 **SQL Injection Detection** – Identifies vulnerable input fields
* ⚡ **XSS Detection** – Detects reflected XSS vulnerabilities
* 🧾 **Form Analysis** – Extracts and tests form inputs
* 🛡️ **Header Security Scan** – Checks for missing security headers
* 📊 **Report Generation** – Displays scan results clearly

---

## 🛠️ Tech Stack

* **Language:** Python
* **Libraries:**

  * `requests`
  * `beautifulsoup4`

---

## 📦 Installation

```bash
git clone https://github.com/muhammed-thoufeek/WebVulnScanner.git
cd WebVulnScanner
pip install -r requirements.txt
```

---

## ▶️ Usage

```bash
python main.py http://example.com
```

---

## 🧪 Example Output

```
[+] Crawling target...
[+] Found 5 forms

[!] SQL Injection vulnerability detected in form: login.php
[!] XSS vulnerability detected in search field

[+] Missing Security Headers:
    - Content-Security-Policy
    - X-Frame-Options
```

---

## 📁 Project Structure

```
WebVulnScanner/
│
├── crawler.py          # Handles website crawling
├── form_scanner.py     # Extracts and tests forms
├── form_sqli.py        # SQL Injection detection
├── xss.py              # XSS detection module
├── header_scan.py      # Security header analysis
├── report.py           # Displays results
├── main.py             # Entry point
├── requirements.txt    # Dependencies
└── README.md
```

---

## ⚙️ Requirements

* Python 3.x
* Internet connection

---

## ⚠️ Disclaimer

This project is intended for **educational purposes only**.
Do not use this tool on websites without **proper authorization**.
The developer is not responsible for any misuse.

---

## 👨‍💻 Author

**Muhammed Thoufeek**

* 💻 Cybersecurity Enthusiast
* 🔐 Interested in Ethical Hacking & AI Security Tools

---

## ⭐ Support

If you find this project useful, consider giving it a ⭐ on GitHub!

---
