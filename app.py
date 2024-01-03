import os
from github import Github

# GitHub repository information
repo_owner = 'Sombitpramanik'
repo_name = 'FINAL-RESUME'
repo_path = '/var/www/RESUME-FINAL/'  # Change this to the local path where you have cloned the repository

# GitHub username and personal access token
github_username = 'Sombitpramanik'
github_token = 'your_token'

# Command to be executed after pulling the changes
command_to_run = 'chown -R www-data:www-data /var/www/RESUME-FINAL/'

def check_and_update_repo():
    # Authenticate with GitHub using a personal access token
    g = Github(github_username, github_token)

    # Get the specified repository
    repo = g.get_user(repo_owner).get_repo(repo_name)

    # Get the local repository's current commit SHA
    local_commit_sha = os.popen(f'git --git-dir={repo_path}/.git rev-parse HEAD').read().strip()

    # Get the latest commit SHA from the GitHub repository
    latest_commit_sha = repo.get_commits()[0].sha

    # Check if there are any new commits
    if local_commit_sha != latest_commit_sha:
        print("Changes detected. Updating repository...")

        # Fetch and pull the latest changes
        os.system(f'git --git-dir={repo_path}/.git fetch origin')
        os.system(f'git --git-dir={repo_path}/.git pull origin master')

        print("Repository updated. Running the command...")

        # Run the specified command
        os.system(command_to_run)
        
        print("Command executed successfully.")
    else:
        print("No changes detected. Repository is up to date.")

if __name__ == "__main__":
    check_and_update_repo()
