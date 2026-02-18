# 🔎 WebVulnScanner

A basic Python-based Web Vulnerability Scanner built for educational and authorized security testing purposes.

---

## ⚠️ Disclaimer

This tool is created for:

- Educational purposes
- Testing websites you own
- Authorized security testing only

Do NOT use this tool on websites without permission. Unauthorized scanning may be illegal.

---

## 🚀 Features

- 🔗 Website Link Crawling
- 🛠 SQL Injection Detection (Basic)
- ⚡ Cross-Site Scripting (XSS) Detection (Basic)
- 📊 Simple Report Generation
- 🐍 Built using Python

---

## 🏗 Project Structure

```
WebVulnScanner/
│
├── main.py
├── crawler.py
├── sqli.py
├── xss.py
├── report.py
├── requirements.txt
└── README.md
```

---

## 🧠 How It Works

1. Takes a target URL
2. Crawls all links from the page
3. Tests each link for:
   - SQL Injection patterns
   - Reflected XSS patterns
4. Displays possible vulnerabilities

---

## ⚙️ Installation

### 1️⃣ Clone the Repository

```bash
git clone git@github.com:thoufeektr30-create/WebVulnScanner.git
cd WebVulnScanner
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Usage

Run the scanner:

```bash
python main.py
```

Enter the target URL when prompted.

Example:

```
Enter target URL: http://example.com
```

---

## 🔐 Technologies Used

- Python 3
- requests
- BeautifulSoup4

---

## 📌 Future Improvements

- Add threading for faster scanning
- Add form input testing
- Add CLI arguments (--target)
- Add JSON & HTML reporting
- Add severity levels
- Add logging system

---

## 👨‍💻 Author

Thoufeek T R  
GitHub: https://github.com/thoufeektr30-create

---

## ⭐ Support

If you found this project useful:

- Star the repository
- Fork it
- Improve it
- Contribute

Happy Learning 🚀
