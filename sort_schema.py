import json

# Replace 'your_file.json' with the path to your JSON file.
file_path = './datasets/ICT_schema.json'
schema_list = []
try:
    with open(file_path, 'r') as json_file:
        for line in json_file:
            try:
                # Load and process each line as JSON data
                schema = json.loads(line)
                # Now 'data' contains the JSON object from the current line
                schema_list.append(schema)
            except json.JSONDecodeError as e:
                print(f"Error decoding JSON from line: {line.strip()}")
except FileNotFoundError:
    print(f"File not found: {file_path}")
except Exception as e:
    print(f"An error occurred: {str(e)}")


# Sort the dictionary by values in ascending order
sorted_list = sorted(schema_list, key=lambda x: x['event_type'])
print(sorted_list)


# File path where you want to save the JSON data
file_path = './datasets/ICT_schema1.json'

try:
    with open(file_path, 'w',encoding="utf-8") as json_file:
        for data_dict in sorted_list:
            # Convert the dictionary to a JSON string
            json_string = json.dumps(data_dict,ensure_ascii=False)
            # Write the JSON string followed by a newline character
            json_file.write(json_string + '\n')
except Exception as e:
    print(f"An error occurred: {str(e)}")