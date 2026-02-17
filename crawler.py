import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def get_links(url):
    links = []
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")

        for a_tag in soup.find_all("a", href=True):
            full_url = urljoin(url, a_tag["href"])
            links.append(full_url)

    except:
        pass

    return links
