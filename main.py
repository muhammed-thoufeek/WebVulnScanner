from crawler import get_links
from sqli import test_sqli
from xss import test_xss

target = input("Enter target URL: ")

links = get_links(target)

for link in links:
    print(f"\nScanning: {link}")

    if test_sqli(link):
        print("Possible SQL Injection detected!")

    if test_xss(link):
        print("Possible XSS detected!")
