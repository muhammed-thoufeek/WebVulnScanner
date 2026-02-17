import requests

def test_xss(url):
    payload = "<script>alert(1)</script>"
    test_url = url + payload

    try:
        response = requests.get(test_url)

        if payload in response.text:
            return True
    except:
        pass

    return False
