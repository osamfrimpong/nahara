import json

def modify_json(input_filename, output_filename):
    with open(input_filename, "r", encoding="utf-8") as json_file:
        original_data = json.load(json_file)

    modified_data = {"output": {}, "input": {}}

    for key, value in original_data.items():
        if key in ["investigations", "intervention", "treatment", "causes"]:
            modified_data["output"][key] = value
        elif key in ["signs", "introduction", "symptoms"]:
            modified_data["input"][key] = value

    with open(output_filename, "w", encoding="utf-8") as output_file:
        json.dump(modified_data, output_file, indent=4, ensure_ascii=False)

if __name__ == "__main__":
    input_json_filename = "cleaned.json"  # Change this to your input JSON file
    output_json_filename = "output.json"  # Change this to the desired output JSON file

    modify_json(input_json_filename, output_json_filename)
    print(f"Modified JSON data saved to {output_json_filename}")
