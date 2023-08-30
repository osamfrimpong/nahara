import json
import csv

# Path to the input JSON file
json_file_path = "output.json"

# Path to the output CSV file
csv_file_path = "output.csv"

# Load JSON data from the file
with open(json_file_path, "r") as json_file:
    data = json.load(json_file)

# Extract the keys from the first dictionary in the JSON data
keys = data[0].keys()

# Write the JSON data to a CSV file
with open(csv_file_path, "w", newline="", encoding="utf-8") as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames=keys)
    csv_writer.writeheader()
    csv_writer.writerows(data)

print("Conversion complete.")
