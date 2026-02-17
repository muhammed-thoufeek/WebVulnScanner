import requests

def test_sqli(url):
    payload = "'"
    test_url = url + payload

    try:
        response = requests.get(test_url)
        errors = ["sql", "syntax", "mysql", "error"]

        for error in errors:
            if error in response.text.lower():
                return True
    except:
        pass

    return False
