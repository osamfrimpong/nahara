import os
from lxml.html import fromstring
import requests
import json
import re

curr_dir = os.getcwd()
output_dir = os.path.join(curr_dir,"files")
files = os.listdir(os.path.join(curr_dir,'html'))
files.sort()

def get_file_content(file_name):
    fileHandle = open(os.path.join(curr_dir,"html",file_name),"r")
    content = fileHandle.read()
    fileHandle.close()
    return content

def strip_html(file_contents):
    return fromstring(file_contents).text_content()

# Function to do splitting
# Modify
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

# Just testing with first file in files array
# Loop through files lis
raw_text = strip_html(get_file_content(files[0]))
print(re.split("TREATMENT", raw_text))
