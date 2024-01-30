#!/usr/bin/python3
"""
Script that takes GitHub credentials (username and personal access token)
and uses the GitHub API to display your id.
"""

import requests
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    token = sys.argv[2]

    url = "https://api.github.com/user"
    headers = {'Authorization': f'token {token}'}

    response = requests.get(url, headers=headers)

    try:
        user_data = response.json()
        user_id = user_data.get('id')
        print(user_id)
    except ValueError:
        print(None)
