import os
import json

def combine_json_files_in_folder(folder_path):
    combined_data = []

    for filename in os.listdir(folder_path):
        if filename.endswith(".json"):
            file_path = os.path.join(folder_path, filename)
            with open(file_path, 'r') as file:
                data = json.load(file)
                if isinstance(data, list):
                    combined_data.extend(data)

    return combined_data

def json_to_lines(input_file, output_file):
    try:
        with open(input_file, 'r') as json_file, open(output_file, 'w') as output:
            data = json.load(json_file)
            for item in data:
                output.write(json.dumps(item) + '\n')
        print(f"Conversion complete. Lines written to {output_file}")
    except Exception as e:
        print(f"Error: {str(e)}")

# Usage example
# input_file = 'input.json'
# output_file = 'output.txt'
# json_to_lines(input_file, output_file)

# Example usage:
# input_folder = "./path_to_folder_containing_json_files"
# combined_data = combine_json_files_in_folder(input_folder)

# Now combined_data is a list containing all dictionaries from the JSON files in the specified folder.
