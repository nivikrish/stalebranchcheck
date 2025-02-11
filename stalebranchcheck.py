import os
import json
import time
import requests
from datetime import datetime, timedelta

# Static variables
TIME_WINDOW = timedelta(days=365)
GITHUB_API_URL = "https://api.github.com"
MASTER_REPO_LIST_FILE = "masterRepoList.txt"

# Read masterRepoList.txt
def read_repo_list():
    with open(MASTER_REPO_LIST_FILE, 'r') as file:
        return [line.strip() for line in file.readlines()]

# Get list of branches from repos
def get_branches(repo):
    url = f"{GITHUB_API_URL}/repos/{repo}/branches"
    response = requests.get(url)
    response.raise_for_status()  # Raise error if response is not 200 OK
    return [branch['name'] for branch in response.json()]

# Get the code commit date from repos
def get_commit_date(repo, branch):
    url = f"{GITHUB_API_URL}/repos/{repo}/branches/{branch}"
    response = requests.get(url)
    response.raise_for_status()
    commit_date = response.json()['commit']['commit']['committer']['date']
    return datetime.strptime(commit_date, "%Y-%m-%dT%H:%M:%SZ")

# Check if a branch is stale which is older than 1 year
def is_stale(commit_date):
    return datetime.now() - commit_date > TIME_WINDOW

# Delete a branch
def delete_branch(repo, branch):
    url = f"{GITHUB_API_URL}/repos/{repo}/git/refs/heads/{branch}"
    response = requests.delete(url)
    response.raise_for_status()
    print(f"Branch {branch} has been deleted from {repo}.")

# User interaction for branch deletion
def prompt_for_deletion(stale_branches, repo):
    print(f"Stale branches in repository {repo}:")
    for branch in stale_branches:
        print(f"- {branch}")

    branches_to_delete = input("Enter comma-separated list of branches to delete (or 'none' to skip): ").strip()

    if branches_to_delete.lower() != 'none':
        branches_to_delete = [branch.strip() for branch in branches_to_delete.split(',')]
        for branch in branches_to_delete:
            if branch in stale_branches:
                delete_branch(repo, branch)
            else:
                print(f"Branch {branch} is not stale, skipping.")
    else:
        print("No branches will be deleted.")

# Clean up a repository
def clean_repo(repo):
    print(f"\nProcessing repository: {repo}")
    try:
        branches = get_branches(repo)
        stale_branches = []
        
        # Identify stale branches
        for branch in branches:
            commit_date = get_commit_date(repo, branch)
            if is_stale(commit_date):
                stale_branches.append(branch)

        # If there are stale branches, prompt for deletion
        if stale_branches:
            prompt_for_deletion(stale_branches, repo)

        # Executive summary
        print(f"Summary for {repo}:")
        print(f"Stale branches: {len(stale_branches)}")
        if len(stale_branches) == len(branches):
            print(f"Recommendation: Consider deleting the repository {repo} as all branches are stale.")
    except requests.exceptions.RequestException as e:
        print(f"Error processing repository {repo}: {e}")

# Main function to process all repositories
def main():
    repos = read_repo_list()

    for repo in repos:
        clean_repo(repo)
        time.sleep(2)  # Adding delay to avoid hitting rate limits

if __name__ == "__main__":
    main()
