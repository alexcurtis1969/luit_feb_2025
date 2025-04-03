# Pull Request Template

## Description

Please include a summary of the changes and what functionality is being added or modified in the pull request. Include any relevant context, such as fixes, improvements, or new features.

### Changes:
1. **`gather_file_details.py`**:
   - Added a function to gather file details recursively from a given directory and its subdirectories.
   - Includes file name, size, type (file or directory), and absolute path.

2. **`file_info.py`**:
   - Added functionality to gather file details for the current working directory only (non-recursive).
   - Includes file name, size, type (file or directory), and absolute path.

## Type of Change

Please select the type of change being made:

- [ ] Bug fix (non-breaking change which fixes an issue)
- [ ] New feature (non-breaking change which adds functionality)
- [ ] Breaking change (fix or feature that would cause existing functionality to not work as expected)
- [ ] Documentation update

## How Has This Been Tested?

- [ ] I have tested the functionality locally by running both scripts in different directories to verify the expected output.
- [ ] Both scripts were executed on different paths, including recursive directory scans for `gather_file_details.py` and non-recursive for `file_info.py`.
- [ ] Outputs were verified for both files and directories, ensuring that all information was correctly gathered.

## Checklist

- [ ] I have reviewed the code and tested it on my local machine.
- [ ] I have updated the `README.md` with instructions or clarifications related to the changes.
- [ ] I have added inline comments to explain the logic of the code.
- [ ] My changes require updates to the documentation, and I have updated the documentation accordingly.
- [ ] I have ensured that all new functionality is covered by tests.

## Additional Notes

Please provide any additional information or context here that might be helpful for the reviewer (e.g., special considerations, edge cases, etc.).

---

**End of Pull Request**
