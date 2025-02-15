## Overview

### What does this pull request do?

- Adds a Python script for downloading and setting up **Assetto Corsa Dedicated Server** on a local machine.
- Automates the installation of required dependencies and the server files via **steamcmd**.

### Purpose

- Simplifies the process of setting up an **Assetto Corsa** dedicated server.
- Ensures the correct installation of the necessary files and configurations.

---

## Changes Made

### Summary of Key Changes:
- **Installation Automation**: The script now automates the process of downloading the **steamcmd** utility and uses it to install the **Assetto Corsa Dedicated Server**.
- **Configuration**: The script prepares the required folders, downloads necessary files, and configures the environment to run the server.

---


## New Features

- **Download SteamCMD**: Automatically downloads the **steamcmd** tool and all required dependencies.
- **Assetto Corsa Server Setup**: Installs the dedicated server files for **Assetto Corsa** using **steamcmd**.
- **Automatic Folder Creation**: The script creates necessary folders for the server installation and configuration.
- **Log Output**: Displays progress logs for better tracking.

---

## Testing the Script

### Steps to Test the Changes:
1. Ensure that Python is installed on your local machine.
2. Clone the repository or download the script to your machine.
3. Run the script by executing:
   ```bash
   python3 assetto_corsa_server_setup.py
The script should:
Download steamcmd if it’s not already installed.
Download the Assetto Corsa Dedicated Server files.
Configure and set up the required folders.
Once completed, check the directory where the server is installed to verify the files.
Launch the server to ensure everything is set up correctly.
Dependencies
Python 3.x
steamcmd (automatically installed by the script)
Checklist
 The script installs steamcmd and Assetto Corsa Dedicated Server correctly.
 The script runs without errors and completes successfully.
 All necessary folders are created and configured.
 Documentation in README is up-to-date.
 No sensitive information (e.g. passwords or keys) is exposed in the script.
 The script is cross-platform (Linux, Windows, macOS, if applicable).
Related Issues
Issue #XX: Description of the issue related to the script.
Additional Notes
Please ensure you have an active Steam account before running the script to download the Assetto Corsa Dedicated Server.
If any issues are encountered, the log output will provide detailed information to help diagnose problems.
Screenshots or Logs (if applicable)
Provide any relevant logs, screenshots, or terminal output demonstrating that the server has been set up successfully.

