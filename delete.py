import os

# Define the root directory
root_directory = './data/'

# Recursively iterate through all directories and files
for root, dirs, files in os.walk(root_directory):
    for file in files:
        # Check if the file name does not contain 'new'
        if 'new' not in file:
            # Construct the full file path
            file_path = os.path.join(root, file)
            
            # Delete the file
            os.remove(file_path)
            print(f"Deleted file: {file_path}")
