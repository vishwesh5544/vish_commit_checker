#!/bin/bash

SCRIPT_DIR=$(pwd)
echo "Current working directory: $SCRIPT_DIR"

# Check if the github package is installed and its details

pip install -r requirements.txt

# Check if the Github class can be imported
# python3 -c "from github import Github" || { echo "ImportError: Cannot import 'Github' from 'github'"; exit 1; }

python3 ./script.py