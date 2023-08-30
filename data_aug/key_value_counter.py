import json

def count_keys_values(json_list):
    num_keys = 0
    num_values = 0
    
    for item in json_list:
        if isinstance(item, dict):
            num_keys += len(item)
            num_values += sum(1 if isinstance(value, (dict, list)) else 1 for value in item.values())
        elif isinstance(item, list):
            sublist_keys, sublist_values = count_keys_values(item)
            num_keys += sublist_keys
            num_values += sublist_values
        else:
            num_values += 1
    
    return num_keys, num_values

def main():
    json_file_path = "holding_area.json"  # Replace with the path to your JSON file
    
    try:
        with open(json_file_path, 'r') as json_file:
            json_list = json.load(json_file)
            num_keys, num_values = count_keys_values(json_list)
            
            print(f"Number of keys: {num_keys}")
            print(f"Number of values: {num_values}")
    except FileNotFoundError:
        print("JSON file not found.")
    except json.JSONDecodeError:
        print("Invalid JSON format.")

if __name__ == "__main__":
    main()
