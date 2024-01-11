#!/usr/bin/env python3
"""
Python script that takes your Github credentials (username and password) and
"""
import requests
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]

    url = "https://api.github.com/user"
    response = requests.get(url, auth=(username, password))

    if response.status_code == 200:
        user_data = response.json()
        user_id = user_data["id"]
        print(f"Your GitHub id is: {user_id}")
    else:
        print("Failed to retrieve GitHub id")
