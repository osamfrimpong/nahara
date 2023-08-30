import json

def format_values(values):
    formatted_strings = []
    
    for value in values:
        formatted_strings.append(f"- {value}")
    
    return formatted_strings

# Load the input JSON file
with open("extracted-output.json", "r") as input_file:
    values_list = json.load(input_file)

# Format the values into strings
formatted_value_strings = format_values(values_list)

# Save the formatted value strings to a new text file
with open("formatted_values.txt", "w") as output_file:
    for formatted_string in formatted_value_strings:
        output_file.write(formatted_string + "\n")

print("Formatted values saved to 'formatted_values.txt'.")
