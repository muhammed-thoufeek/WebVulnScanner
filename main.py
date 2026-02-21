import argparse
from concurrent.futures import ThreadPoolExecutor
from crawler import get_links
from form_sqli import scan_form_sqli

parser = argparse.ArgumentParser()
parser.add_argument("--target", required=True)
args = parser.parse_args()

target = args.target

print("\nCollecting links...\n")

links = get_links(target)

if not links:
    links = [target]

print(f"Total URLs to scan: {len(links)}")

print("\nStarting threaded scan...\n")

with ThreadPoolExecutor(max_workers=5) as executor:
    executor.map(scan_form_sqli, links)

print("\nScan Completed.")
