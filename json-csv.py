import json
import csv

# Load the JSON array from the file
with open("data_aug/output-referral-reproduced.json", "r") as json_file:
    data_array = json.load(json_file)

# Specify the CSV file name
csv_file_name = "output.csv"

# Extract the header (keys from the first dictionary)
header = data_array[0].keys()

# Write the data to the CSV file
with open(csv_file_name, "w", newline="") as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=header)
    
    # Write the header
    writer.writeheader()
    
    # Write the data rows
    for item in data_array:
        writer.writerow(item)

print(f"CSV data saved to '{csv_file_name}'.")
