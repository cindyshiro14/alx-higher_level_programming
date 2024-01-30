#!/usr/bin/python3
"""
Script that takes the repository name and owner name as command-line arguments,
uses the GitHub API to retrieve the 10 most recent commits from the specified repository,
and prints them with the format <sha>: <author name>.
"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: ./100-github_commits.py <repository name> <owner name>")
        sys.exit(1)

    repo_name = sys.argv[1]
    owner_name = sys.argv[2]
    url = f"https://api.github.com/repos/{owner_name}/{repo_name}/commits"

    response = requests.get(url)

    try:
        commits_data = response.json()[:10]

        for commit in commits_data:
            sha = commit.get('sha')
            author_name = commit.get('commit').get('author').get('name')
            print(f"{sha}: {author_name}")
    except ValueError:
        print(None)
