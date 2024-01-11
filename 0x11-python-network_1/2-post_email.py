#!/usr/bin/env python3
"""
Python script that takes in a URL and an email address, sends a POST request
"""
import urllib.parse
import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    data = urllib.parse.urlencode({'email': email}).encode('utf-8')
    req = urllib.request.Request(url, data=data, method='POST')
    
    with urllib.request.urlopen(req) as response:
        print(response.read().decode('utf-8'))
