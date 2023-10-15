import os
import time
import subprocess

# List of scripts to run
scripts_to_run = ['pinDownloader.py', 'imageCrop.py', 'instagramUploader.py']  # Replace with your script filenames

# Function to run a script
def run_script(script):
    print(f"Running script: {script}")
    subprocess.run(['python', script])

# Run each script and wait for 3 seconds between each
for script in scripts_to_run:
    run_script(script)
    time.sleep(3)  # Wait for 3 seconds

print("All scripts completed.")
