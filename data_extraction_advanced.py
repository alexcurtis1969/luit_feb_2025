import os  # Importing the os module to interact with the operating system

# Function to get file details
def get_file_info(file_path):
    return {
        'name': os.path.basename(file_path),  # Extracting the file/directory name from the full path
        'size': os.path.getsize(file_path),   # Getting the size of the file or directory
        'type': 'Directory' if os.path.isdir(file_path) else 'File',  # Checking if it's a directory or file
        'path': os.path.abspath(file_path)   # Getting the absolute path of the file/directory
    }

# Function to gather file details from a given path (recursive)
def gather_file_details(path=os.getcwd()):
    file_details = []  # Initialize an empty list to store file details
    
    # Check if the given path exists
    if not os.path.exists(path):
        print(f"Error: The path '{path}' does not exist.")  # Print error message if path doesn't exist
        return file_details  # Return the empty list in case of invalid path
    
    # Loop through the items in the given directory
    for item in os.listdir(path):  # os.listdir() lists all items in the directory
        item_path = os.path.join(path, item)  # Combine the path and item name to get the full path
        
        # If it's a directory, recurse into it
        if os.path.isdir(item_path):  # Check if the item is a directory
            file_details.append(get_file_info(item_path))  # Add directory details to the list
            file_details.extend(gather_file_details(item_path))  # Recurse into the directory and add its contents
        elif os.path.isfile(item_path):  # Check if the item is a file
            file_details.append(get_file_info(item_path))  # Add file details to the list
    
    return file_details  # Return the list of file details

# Correct path to your directory (replace with the actual directory path)
path = r'C:\Users\alexa\OneDrive\Documents\GitHub\luit_feb_2025'  # Using a raw string to handle the Windows path
files = gather_file_details(path)  # Call the function to gather details for the specified path

# Print the list of file details
for file_info in files:  # Loop through the list of file details
    print(file_info)  # Print each file/directory details
