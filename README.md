# House Price Prediction using Linear Regression

This project demonstrates how to predict house prices based on two features: the number of rooms and the size of the house (in square feet). The model is implemented using Python's **scikit-learn** library and uses a **Linear Regression** algorithm to predict prices. The dataset is assumed to contain information about various houses, including the number of rooms, size, and price.

## Requirements

To run this project, you'll need to have the following Python libraries installed:

- `numpy` (for numerical operations)
- `pandas` (for data manipulation)
- `matplotlib` (for data visualization)# File and Directory Information Script

This repository contains Python scripts that help gather information about files and directories in a specified path. The scripts work by recursively traversing directories and extracting details such as name, size, type (File/Directory), and absolute path. The scripts can be customized to scan any path, defaulting to the current working directory if no path is provided.

## Contents
1. **`gather_file_details.py`** - A script that recursively scans a directory and its subdirectories to collect file and directory information.
2. **`file_info.py`** - A script that gathers details about files and directories in the current working directory only.

## Requirements
- Python 3.x
- No external dependencies

## How to Run the Scripts

### 1. **`gather_file_details.py`**

This script recursively gathers details about files and directories within the specified path.

### Features:
- Scans a directory and all its subdirectories.
- Gathers file information: name, size, type (File or Directory), and absolute path.
- Allows the user to specify a directory path (defaults to the current working directory if not provided).

### Example:

```python
import os

def get_file_info(file_path):
    return {
        'name': os.path.basename(file_path),
        'size': os.path.getsize(file_path),
        'type': 'Directory' if os.path.isdir(file_path) else 'File',
        'path': os.path.abspath(file_path)
    }

def gather_file_details(path=os.getcwd()):
    file_details = []
    if not os.path.exists(path):
        print(f"Error: The path '{path}' does not exist.")
        return file_details
    
    for item in os.listdir(path):
        item_path = os.path.join(path, item)
        if os.path.isdir(item_path):
            file_details.append(get_file_info(item_path))
            file_details.extend(gather_file_details(item_path))
        elif os.path.isfile(item_path):
            file_details.append(get_file_info(item_path))
    
    return file_details

path = r'C:\Users\alexa\OneDrive\Documents\GitHub\luit_feb_2025'  # Specify your directory
files = gather_file_details(path)

for file_info in files:
    print(file_info)

- `scikit-learn` (for building and evaluating the machine learning model)

You can install the necessary libraries by running:

```bash
pip install numpy pandas matplotlib scikit-learn
