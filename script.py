from command_runner import CommandRunner
from vish_commit_checker import VishCommitChecker
import time


if __name__ == "__main__":
    repo_owner = "vishwesh5544"
    repo_name = "devops-cicd"
    working_dir = "/var/www/html/awesomeweb"
    
    checker = VishCommitChecker(repo_owner, repo_name)
    runner = CommandRunner(working_dir)
    
    if checker.check_new_commits():
        print("New commits found. Pulling changes and reloading Nginx.")
        runner.pull_and_reload()
        print("Deployment complete.")
    else: 
        print("No new commits found.")

