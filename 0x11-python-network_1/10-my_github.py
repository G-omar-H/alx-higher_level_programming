#!/usr/bin/python3
"""
Python script that takes your Github credentials (username and password) and
"""
import requests
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]

    url = "https://api.github.com/user"
    headers = {'Authorization': f'Bearer {password}'}
    res = requests.get("https://api.github.com/user", headers=headers)
    if (res.status_code >= 400):
        print("None")
        exit()
    print(res.json()["id"])
