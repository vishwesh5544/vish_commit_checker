import json
import os
from github import Github
from dotenv import load_dotenv

class VishCommitChecker:
    def __init__(self, repo_owner, repo_name, history_file="commit_history.json"):
        self.repo_owner = repo_owner
        self.repo_name = repo_name
        self.history_file = history_file

        # Load environment variables from .env file
        load_dotenv()

        self.github_token = os.getenv("GITHUB_TOKEN")
        if not self.github_token:
            raise ValueError(
                "GitHub token not found. Please set the GITHUB_TOKEN environment variable."
            )
        self.github = Github(self.github_token)
        self.repo = self.github.get_repo(f"{repo_owner}/{repo_name}")

        # Ensure the commit history file is initialized
        self.ensure_history_file()

    def ensure_history_file(self):
        if not os.path.exists(self.history_file):
            with open(self.history_file, "w") as file:
                json.dump([], file, indent=2)

    def fetch_all_commits(self):
        commits = []
        for commit in self.repo.get_commits():
            commits.append(commit)
        return commits

    def load_commit_history(self):
        try:
            with open(self.history_file, "r") as file:
                return json.load(file)
        except (json.JSONDecodeError, FileNotFoundError):
            return []

    def save_commit_history(self, history):
        with open(self.history_file, "w") as file:
            json.dump(history, file, indent=2)

    def check_new_commits(self):
        latest_commits = self.fetch_all_commits()
        print(f"Found {len(latest_commits)} commits in the repository.")

        commit_history = self.load_commit_history()

        # Extract the SHAs of the new commits
        new_commit_shas = {commit.sha for commit in latest_commits}
        existing_commit_shas = {commit["sha"] for commit in commit_history}

        # Find the new commits by comparing SHAs
        new_commits = [
            {
                "sha": commit.sha,
                "message": commit.commit.message,
                "author": commit.commit.author.name,
                "date": commit.commit.author.date.isoformat(),
            }
            for commit in latest_commits
            if commit.sha not in existing_commit_shas
        ]

        if new_commits:
            print(f"Found {len(new_commits)} new commits.")
            # Append new commits to the commit history
            commit_history.extend(new_commits)
            self.save_commit_history(commit_history)
        else:
            print("No new commits found.")
