#!/usr/bin/python3
"""
    Write a Python script that takes your
    GitHub credentials (username and password)
    and uses the GitHub API to display your id
"""


if __name__ == '__main__':
    import requests
    from sys import argv

    url = 'https://api.github.com/user'
    username = argv[1]
    password = argv[2]

    r = requests.get(url, auth=(username, password))
    try:
        print(r.json()['id'])
    except:  # noqa
        print("None")
