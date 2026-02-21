from bs4 import BeautifulSoup
import requests
from urllib.parse import urljoin

# STEP 1: Get all forms from the page
def get_forms(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        return soup.find_all("form")
    except:
        return []

# STEP 2: Extract form details
def get_form_details(form):
    details = {}
    action = form.attrs.get("action")
    method = form.attrs.get("method", "get").lower()
    inputs = []

    for input_tag in form.find_all("input"):
        input_name = input_tag.get("name")
        input_type = input_tag.get("type", "text")
        inputs.append({"name": input_name, "type": input_type})

    details["action"] = action
    details["method"] = method
    details["inputs"] = inputs

    return details

# STEP 3: Submit payload into form
def submit_form(form_details, url, payload):
    target_url = urljoin(url, form_details["action"])
    data = {}

    for input in form_details["inputs"]:
        if input["type"] == "text" and input["name"]:
            data[input["name"]] = payload

    if form_details["method"] == "post":
        return requests.post(target_url, data=data)
    else:
        return requests.get(target_url, params=data)
