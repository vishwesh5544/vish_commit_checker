# DevOps CICD

This project implements a CI/CD pipeline for deploying updates to a web application hosted in `/var/www/html/devops-cicd`. It periodically checks for new commits in the GitHub repository and pulls the latest changes if any new commits are found. After pulling the updates, it reloads Nginx to apply the changes.

## Features

- **Automatic Git Pull**: The script automatically pulls the latest changes from the GitHub repository if new commits are detected.
- **Nginx Reload**: After pulling the latest changes, the script reloads Nginx to apply the updates.
- **Periodic Checks**: The script continuously monitors the repository for new commits at a regular interval.

## Prerequisites

- **Python 3.x**: Ensure you have Python 3.x installed.
- **Nginx**: Nginx should be installed and properly configured on your server.
- **Git**: Git should be installed to pull updates from the repository.

## Installation

1. **Clone the Repository**:
    ```sh
    git clone https://github.com/vishwesh5544/vish_commit_checker.git
    ```

2. **Navigate to the Directory**:
    ```sh
    cd vish_commit_checker
    ```

3. **Set Up Environment Variables**:
    Create a `.env` file in the root directory and add your GitHub token:
    ```sh
    echo "GITHUB_TOKEN=your-github-token" > .env
    ```

4. **Install Dependencies**:
    Make sure you have the required Python libraries installed:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

To run the script, simply execute the following command:
```sh
python script.py
