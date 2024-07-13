import json
import os

from github import Github


class VishCommitChecker: 
    def __init__(self, repo_owner, repo_name, github_token, history_file='commit_history.json'):
        self.repo_owner = repo_owner
        self.repo_name = repo_name
        self.history_file = history_file
        self.github = Github(github_token)
        self.repo = self.github.get_repo(f'{repo_owner}/{repo_name}')
    
    def fetch_latest_commits(self):
        return self.repo.get_commits()
    
    def load_commit_history(self):
        if os.path.exists(self.history_file):
            with open(self.history_file, 'r') as file:
                return json.load(file)
        return []

    def save_commit_history(self, history):
        with open(self.history_file, 'w') as file:
            json.dump(history, file, indent=2)

    def check_new_commits(self):
        latest_commits = self.fetch_latest_commits()
        commit_history = self.load_commit_history()
        
        # Extract the SHAs of the new commits
        new_commit_shas = {commit.sha for commit in latest_commits}
        existing_commit_shas = {commit['sha'] for commit in commit_history}
        
        # Find the new commits by comparing SHAs
        new_commits = [
            {
                'sha': commit.sha,
                'message': commit.commit.message,
                'author': commit.commit.author.name,
                'date': commit.commit.author.date.isoformat()
            }
            for commit in latest_commits if commit.sha not in existing_commit_shas
        ]
        
        if new_commits:
            print(f"Found {len(new_commits)} new commits.")
            # Append new commits to the commit history
            commit_history.extend(new_commits)
            self.save_commit_history(commit_history)
        else:
            print("No new commits found.")