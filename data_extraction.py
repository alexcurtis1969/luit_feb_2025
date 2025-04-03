import os  # Importing the os module to interact with the operating system

# Function to get file details
def get_file_info(file_path):
    return {
        'name': os.path.basename(file_path),  # Extract the name of the file/directory from the full path
        'size': os.path.getsize(file_path),   # Get the size of the file or directory
        'type': 'Directory' if os.path.isdir(file_path) else 'File',  # Check if it's a directory or file and set the type
        'path': os.path.abspath(file_path)   # Get the absolute path of the file or directory
    }

# Get the current working directory using os.getcwd()
working_directory = os.getcwd()  # Store the current working directory path in the variable

# List to store file details
file_details = []  # Initialize an empty list to store details of files and directories

# Loop through the items in the current working directory
for item in os.listdir(working_directory):  # os.listdir() returns a list of items in the directory
    item_path = os.path.join(working_directory, item)  # Combine the directory path and item name to get the full path
    
    # If the item is a file or a directory, get its details and add it to the file_details list
    if os.path.isfile(item_path) or os.path.isdir(item_path):  # Check if the item is a file or directory
        file_details.append(get_file_info(item_path))  # Call get_file_info to get details and add it to the list

# Print the list of file details
for file_info in file_details:  # Loop through each file detail in the file_details list
    print(file_info)  # Print the details of the current file/directory
