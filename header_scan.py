def check_headers(url):
    import requests
    r = requests.get(url)

    headers = r.headers

    if "X-Frame-Options" not in headers:
        print("[!] Clickjacking protection missing")

