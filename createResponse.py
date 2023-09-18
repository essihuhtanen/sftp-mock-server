import json
import sys
import os

def read_and_parse_json(filepath):
    try:
        with open(filepath, 'r') as file:
            content = file.read()
            parsed_data = json.loads(content)
            return parsed_data
    except FileNotFoundError:
        print(f"File not found: {filepath}")
    except json.JSONDecodeError:
        print(f"Error decoding JSON in file: {filepath}")
    except Exception as e:
        print(f"An error occurred: {e}")

def create_response(jsondata):
    jsondata["requestHandled"] = 'True'

if __name__ == "__main__":
    file_path = sys.argv[1]
    jsondata = read_and_parse_json(file_path)
    create_response(jsondata)

    input_dir, input_filename = os.path.split(file_path)
    output_filename = f"Response_{input_filename}"
    output_file_path = os.path.join(input_dir, output_filename)
    
    with open(output_file_path, "w") as output_file:
        json.dump(jsondata, output_file, indent=None)
