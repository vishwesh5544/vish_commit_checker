#!/bin/bash

# Store the directory of this script
SCRIPT_DIR="$(dirname "$0")"

# Change to the script's directory
cd "$SCRIPT_DIR" || { echo "Failed to change directory to $SCRIPT_DIR"; exit 1; }

echo "Current working directory: $(pwd)"

# Check if the GitHub package is installed and its details
pip install -r requirements.txt

# Run script.py
python3 script.py
