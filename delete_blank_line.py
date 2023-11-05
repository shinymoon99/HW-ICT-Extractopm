import os

# Function to remove blank lines from a text file
def remove_blank_lines(input_file, output_file):
    try:
        with open(input_file, 'r') as file:
            with open(output_file, 'w') as output:
                for line in file:
                    if line.strip():  # Check if the line is not blank
                        output.write(line)
        print(f"Blank lines removed. Result saved to {output_file}")
    except FileNotFoundError:
        print(f"File '{input_file}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Function to process all text files in a folder
def process_folder(folder_path):
    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            input_file = os.path.join(folder_path, filename)
            output_file = os.path.join(folder_path, f"no_blank_{filename}")
            remove_blank_lines(input_file, output_file)

if __name__ == "__main__":
    folder_path = "./datasets/selected_4"  # Replace with the path to your folder
    process_folder(folder_path)
