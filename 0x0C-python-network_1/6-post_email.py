#!/usr/bin/python3
"""
    Write a Python script that takes in a URL and an
    email address, sends a POST request to the passed
    URL with the email as a parameter, and finally displays
    the body of the response.
"""

if __name__ == '__main__':

    import requests
    from sys import argv

    url = argv[1]
    email = argv[2]

    r = requests.post(url, data={'email': email})
    if r.status_code == 400:
        print(f"Error code: {r.status_code}")
    else:
        print(r.text)
