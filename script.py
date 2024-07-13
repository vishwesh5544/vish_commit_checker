from vish_commit_checker import VishCommitChecker


if __name__ == "__main__":
    repo_owner = "vishwesh5544"
    repo_name = "devops-cicd"
    
    checker = VishCommitChecker(repo_owner, repo_name)
    checker.check_new_commits()