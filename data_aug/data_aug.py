import json

# Read the original JSON file
with open('original.json', 'r') as file:
    data = json.load(file)

# Get the first object from the list
first_object = data[0]

# Reproduce the object 500 times
reproduced_data = [first_object] * 500

# Write the reproduced data to a new JSON file
with open('reproduced.json', 'w') as file:
    json.dump(reproduced_data, file, indent=4)

print("Reproduction and storage complete.")
