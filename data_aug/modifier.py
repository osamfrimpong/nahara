import json

def update_reproduced_data(reproduced_data, holding_list):
    for obj, new_input in zip(reproduced_data, holding_list):
        obj['input'] += new_input

def main():
    # Load the content of holding_area.json
    with open('holding_area.json', 'r') as holding_file:
        holding_data = json.load(holding_file)

    # Load the content of reproduced.json
    with open('reproduced.json', 'r') as reproduced_file:
        reproduced_data = json.load(reproduced_file)

    # Extract the list from holding_data
    holding_list = holding_data['input']

    # Update the reproduced_data using holding_list
    update_reproduced_data(reproduced_data, holding_list)

    # Write the modified data to a new JSON file
    with open('modified_reproduced.json', 'w') as modified_file:
        json.dump(reproduced_data, modified_file, indent=4)

    print("Modification complete. Check modified_reproduced.json")

if __name__ == "__main__":
    main()
