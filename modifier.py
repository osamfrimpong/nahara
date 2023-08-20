# import os
# from lxml.html import fromstring
# import requests
# import json
# import re

# curr_dir = os.getcwd()
# output_dir = os.path.join(curr_dir,"files")
# files = os.listdir(os.path.join(curr_dir,'html'))
# files.sort()

# def get_file_content(file_name):
#     fileHandle = open(os.path.join(curr_dir,"html",file_name),"r")
#     content = fileHandle.read()
#     fileHandle.close()
#     return content

# def strip_html(file_contents):
#     return fromstring(file_contents).text_content()

# # Function to do splitting
# # Modify
# def split_into_sections(content):
#     return content.split("INVESTIGATIONS")

# def parse_table_of_contents(table_of_contents_raw):
#     table_of_contents = json.loads(table_of_contents_raw)
#     addresses = []
#     for chapter in table_of_contents:
#         sub_items = chapter['subitems']
#         for sub_item in sub_items:
#             address = sub_item['address']
#             addresses.append(address)
#     return addresses

# # Just testing with first file in files array
# # Loop through files lis
# raw_text = strip_html(get_file_content(files[0]))
# print(re.split("TREATMENT", raw_text))

import os
from lxml.html import fromstring
import requests
import json
import re

curr_dir = os.getcwd()
output_dir = os.path.join(curr_dir, "files")
files = os.listdir(os.path.join(curr_dir, 'html'))
files.sort()

def get_file_content(file_path):
    with open(file_path, "r") as fileHandle:
        content = fileHandle.read()
    return content

def strip_html(file_contents):
    return fromstring(file_contents).text_content()

# Combine stripped HTML content into a single string
combined_content = ""

# Loop through files in the folder
for file_name in files:
    file_path = os.path.join(curr_dir, "html", file_name)
    raw_text = strip_html(get_file_content(file_path))
    combined_content += raw_text + "\n\n"  # Add a separator between contents

# Write the combined content to a file.txt
output_file_path = os.path.join(curr_dir, "file.txt")
with open(output_file_path, "w") as output_file:
    output_file.write(combined_content)

print("Combined content written to file.txt")
