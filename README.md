# stalebranchcheck
The Python script (repoCleaner_no_auth.py) does the following:

Reads Repositories: 
The script reads a list of repositories from the masterRepoList.txt file.

Fetches Branches: 
It retrieves the list of branches for each repository using GitHub’s REST API.

Identifies Stale Branches: 
It checks the latest commit date of each branch and compares it to the current date to determine if the branch is stale (older than 1 year).

Prompts for Deletion: 
For stale branches, the script asks the user if they want to delete the branch.

Deletes Selected Branches: 
After the user confirms, the script deletes the stale branches.

Generates a Summary: 
The script outputs an executive summary of deleted branches and recommends deleting the repository if all branches are stale.

Following will be the output:

Processing repository: nivikrish/docs
Stale branches in repository nivikrish/docs:
- cmwilson21-patch-1
- dependabot/docker/node-19.1.0-alpine
- dependabot/docker/node-19.7-alpine
- dependabot/docker/node-19.9-alpine
- dependabot/docker/node-20.4-alpine
- dependabot/docker/node-20.5-alpine
- dependabot/docker/node-20.8-alpine
- dependabot/github_actions/actions/cache-4.0.0
- dependabot/github_actions/actions/github-script-98814c53be79b1d30f795b907e553d8679345975
- dependabot/github_actions/juliangruber/approve-pull-request-action-2
- dependabot/npm_and_yarn/change-case-5.0.1
- dependabot/npm_and_yarn/follow-redirects-1.15.4
- dependabot/npm_and_yarn/jest-environment-puppeteer-8.0.5
- dependabot/npm_and_yarn/jest-environment-puppeteer-8.0.6
- dependabot/npm_and_yarn/lint-staged-15.0.1
- dependabot/npm_and_yarn/liquidjs-10.4.0
- dependabot/npm_and_yarn/liquidjs-10.6.0
- dependabot/npm_and_yarn/liquidjs-10.6.1
- dependabot/npm_and_yarn/liquidjs-10.6.2
Enter comma-separated list of branches to delete (or 'none' to skip): none
No branches will be deleted.
Summary for nivikrish/docs:
Stale branches: 19



### **How to Use:**

1. **Clone or download this repository** to your local machine.
2. **Create the `masterRepoList.txt` file** and populate it with the repositories you want to clean.
3. **Run the script** using Python, and follow the prompts to manage stale branches.

By following these instructions, you should be able to use the `repoCleaner` utility to manage your GitHub repositories and clean up stale branches efficiently.
