# import json

# def count_top_level_keys(json_data):
#     if isinstance(json_data, dict):
#         return len(json_data.keys())
#     return 0

# # Replace 'your_file.json' with the actual JSON file's path
# json_file_path = 'output.json'

# with open(json_file_path, 'r') as json_file:
#     try:
#         data = json.load(json_file)
#         keys_count = count_top_level_keys(data)
#         print(f"Number of top-level keys in the JSON file: {keys_count}")
#     except json.JSONDecodeError as e:
#         print("Error decoding JSON:", e)


import json

def count_objects_in_json_array(file_path):
    try:
        with open(file_path, 'r') as json_file:
            data = json.load(json_file)
            
            if isinstance(data, list):
                object_count = len(data)
                return object_count
            else:
                return "The JSON data is not an array."
    except FileNotFoundError:
        return "File not found."

if __name__ == "__main__":
    file_path = "path/to/your/json/file.json"
    object_count = count_objects_in_json_array("output-referral.json")
    
    if isinstance(object_count, int):
        print(f"Number of objects in the JSON array: {object_count}")
    else:
        print(object_count)
