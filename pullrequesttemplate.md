# Pull Request Template

## Description
This PR introduces a Python script for generating random names, where the user specifies their name, selects a department, and chooses the number of EC2 instances to generate. The script outputs random names in a specified format and writes them to a CSV file.

## Changes Made
- Added a function `generate_random_name` that generates random names by combining a user’s name, department, and randomly generated characters.
- Integrated input validation for department selection.
- Implemented CSV file writing to store the generated names.

## How to Test
1. Run the script.
2. Provide the necessary inputs:
   - Your name.
   - Select a department from the list (`Cloud Engineering`, `Sales`, `Marketing`, `Logistics`, `Support`, `Development`).
   - Specify the number of EC2 instances (random names to be generated).
3. The generated names will be printed to the console and saved in `generated_names.csv`.

## CSV Output Format
The CSV file will have the following columns:
- `User Name`: The name provided by the user.
- `Generated Name`: The generated random name.
- `Department`: The selected department.
- `Unique ID`: A unique random identifier for each generated name.

## Example


## Notes
- Ensure the script is run in an environment with appropriate permissions to write to the file system.
- The random generation relies on the `random` module for randomness, and the output is designed for simplicity and example purposes.
- This script does not perform advanced error handling for edge cases such as invalid input or missing file permissions.
  
## Related Issues
- N/A

## Checklist
- [ ] Code compiles correctly.
- [ ] Added relevant tests.
- [ ] Documentation has been updated accordingly (if applicable).
