import json

def count_top_level_keys(json_data):
    if isinstance(json_data, dict):
        return len(json_data.keys())
    return 0

# Replace 'your_file.json' with the actual JSON file's path
json_file_path = 'cleaned.json'

with open(json_file_path, 'r') as json_file:
    try:
        data = json.load(json_file)
        keys_count = count_top_level_keys(data)
        print(f"Number of top-level keys in the JSON file: {keys_count}")
    except json.JSONDecodeError as e:
        print("Error decoding JSON:", e)
