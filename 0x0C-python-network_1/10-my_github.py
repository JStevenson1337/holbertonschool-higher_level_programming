#!/usr/bin/python3
"""
    Write a Python script that takes your
    GitHub credentials (username and password)
    and uses the GitHub API to display your id
"""
import urllib.request as requests
from sys import argv


if __name__ == "__main__":
    url = 'https://api.github.com/user'
    url_auth = 'https://api.github.com/user/emails'
    try:
        username = argv[1]
        password = argv[2]
    except IndexError:
        print("Please provide your credentials")
        exit()
    else:
        pass
    try:
        with requests.Session() as s:
            s.auth = (username, password)
            r = s.get(url)
            r_auth = s.get(url_auth)
            print(r.json()['id'])
            for email in r_auth.json():
                print(email)
    except requests.exceptions.HTTPError as e:
        print("Unauthorized")
        exit()