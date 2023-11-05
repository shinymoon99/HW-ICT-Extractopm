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

# Example usage:
# input_folder = "./path_to_folder_containing_json_files"
# combined_data = combine_json_files_in_folder(input_folder)

# Now combined_data is a list containing all dictionaries from the JSON files in the specified folder.
