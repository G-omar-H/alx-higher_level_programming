#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to the URL and displays
"""
import urllib.request
import sys


url = sys.argv[1]
if __name__ == "__main__":
    try:
        with urllib.request.urlopen(url) as response:
            print(response.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")
