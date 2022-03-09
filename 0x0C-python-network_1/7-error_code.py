#!/usr/bin/python3
"""
    Write a Python script that takes in a URL,
    sends a request to the URL and displays
    the body of the response.
"""

if __name__ == '__main__':
    import requests
    from sys import argv

    url = argv[1]
    r = requests.get(url)
    if r.status_code == 400:
        print(f"Error code: {r.status_code}")
