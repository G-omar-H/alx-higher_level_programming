#!/usr/bin/python3
"""
Python script that takes in a letter and sends a POST request to http://
"""
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) > 1:
        q = sys.argv[1]
    else:
        q = ""

    try:
        response = requests.post("http://0.0.0.0:5000/search_user",
                                 data={"q": q})
        json_data = response.json()

        if json_data:
            print("[{}] {}".format(json_data.get("id"), json_data.get("name")))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
