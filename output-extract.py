import json

# Load the input JSON file
with open("output.json", "r") as input_file:
    data_list = json.load(input_file)

output_values = []

# Extract the "output" values from each dictionary in the list
for item in data_list:
    output_value = item.get("output")
    if output_value is not None:
        output_values.append(output_value)

# Save the extracted output values to a new JSON file
with open("extracted-output.json", "w") as output_file:
    json.dump(output_values, output_file, indent=4)

print("Output values extracted and saved to 'output.json'.")
