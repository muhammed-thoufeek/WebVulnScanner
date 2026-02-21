from form_scanner import get_forms, get_form_details, submit_form

def scan_form_sqli(url):
    payload = "'"
    forms = get_forms(url)

    for form in forms:
        details = get_form_details(form)
        response = submit_form(details, url, payload)

        if "sql" in response.text.lower():
            print(f"[!] SQL Injection possible in form at {url}")
