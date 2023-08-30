import json
import csv

def clean_fieldname(fieldname):
    # Clean up the fieldname (remove spaces, convert to lowercase, etc.)
    cleaned = fieldname.lower().replace(" ", "_")
    return cleaned

# Load the JSON array from the file
with open("output-referral.json", "r") as json_file:
    data_array = json.load(json_file)

# Specify the CSV file name
csv_file_name = "output.csv"

# Extract all unique field names from the JSON data
all_fieldnames = set()
for item in data_array:
    all_fieldnames.update(item.keys())

# Clean and prepare the fieldnames for CSV writing
cleaned_fieldnames = [clean_fieldname(fieldname) for fieldname in all_fieldnames]

# Write the data to the CSV file
with open(csv_file_name, "w", newline="") as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=cleaned_fieldnames)
    
    # Write the header
    writer.writeheader()
    
    # Write the data rows
    for item in data_array:
        cleaned_item = {clean_fieldname(key): value for key, value in item.items()}
        writer.writerow(cleaned_item)

print(f"CSV data saved to '{csv_file_name}'.")
