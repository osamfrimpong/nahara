import json

def reproduce_objects(input_file_path, output_file_path):
    try:
        with open(input_file_path, 'r') as json_file:
            data = json.load(json_file)
            
            if isinstance(data, list):
                reproduced_objects = []
                
                for obj in data:
                    for _ in range(500):
                        reproduced_objects.append(obj.copy())
                
                with open(output_file_path, 'w') as output_json_file:
                    json.dump(reproduced_objects, output_json_file, indent=4)
                
                print(f"Reproduction completed. Output saved to {output_file_path}")
            else:
                print("The JSON data is not an array.")
    except FileNotFoundError:
        print("Input file not found.")

if __name__ == "__main__":
    input_file_path = "output-referral.json"
    output_file_path = "data_aug/output-referral-reproduced.json"
    
    reproduce_objects(input_file_path, output_file_path)
