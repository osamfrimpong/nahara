from lxml.html import fromstring
import requests
import json

table_of_contents_req = requests.get("https://osamfrimpong.github.io/stg_app_web/json/table_of_contents.json")

def get_file_content(file_url):
    file_req = requests.get("https://osamfrimpong.github.io/stg_app_web/html/"+file_url)
    return file_req.text

def strip_html(file_contents):
    return fromstring(file_contents).text_content()

def split_into_sections(content):
    return content.split("INVESTIGATIONS")


def parse_table_of_contents(table_of_contents_raw):
    table_of_contents = json.loads(table_of_contents_raw)
    addresses = []
    for chapter in table_of_contents:
        sub_items = chapter['subitems']
        for sub_item in sub_items:
            address = sub_item['address']
            addresses.append(address)
    return addresses
            


counter = 0
file_addresses = parse_table_of_contents(table_of_contents_req.text)

for address in file_addresses:
    counter += 1
    if (counter == 1):     
        file_content = get_file_content(address)
        split_into_sections(strip_html(file_content))

    

