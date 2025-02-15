import os
import subprocess
import sys
import time
import urllib.request
import zipfile

def download_steamcmd():
    print("Downloading SteamCMD...")
    url = "https://steamcdn-a.akamaihd.net/client/installer/steamcmd.zip"
    zip_path = "steamcmd.zip"
    
    # Download steamcmd.zip
    urllib.request.urlretrieve(url, zip_path)
    print("Downloaded SteamCMD successfully.")
    
    # Extract steamcmd.zip
    print("Extracting SteamCMD...")
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall("steamcmd")
    
    print("SteamCMD extracted successfully.")
    
    # Clean up the zip file
    os.remove(zip_path)
    
def install_steamcmd():
    if not os.path.exists("steamcmd"):
        download_steamcmd()

def run_steamcmd(command):
    print(f"Running SteamCMD with command: {command}")
    
    # Run SteamCMD
    steamcmd_path = os.path.join(os.getcwd(), "steamcmd", "steamcmd.exe")
    subprocess.run([steamcmd_path, "+login", "anonymous", command, "+quit"], check=True)

def setup_assetto_corsa():
    # Install the Assetto Corsa Dedicated Server
    print("Setting up Assetto Corsa Dedicated Server...")
    install_steamcmd()
    print("Installing Assetto Corsa Server...")
    run_steamcmd("app_update 302550 validate")  # Assetto Corsa Dedicated Server ID is 302550
    print("Assetto Corsa Dedicated Server installed successfully.")

def start_server():
    # Path to Assetto Corsa dedicated server executable
    server_path = os.path.join(os.getcwd(), "steamcmd", "steamapps", "common", "assettocorsa", "server.exe")

    if not os.path.exists(server_path):
        print("Assetto Corsa Dedicated Server not found.")
        sys.exit(1)

    # Start the Assetto Corsa server
    print("Starting the Assetto Corsa server...")
    subprocess.run([server_path, "+server", "my_server", "+track", "magione", "+port", "9600"], check=True)

def main():
    setup_assetto_corsa()
    start_server()
    
if __name__ == "__main__":
    main()
