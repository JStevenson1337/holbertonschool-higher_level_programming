#!/usr/bin/python3
"""
    Write a Python script that takes in
    a letter and sends a POST request
    to http://0.0.0.0:5000/search_user
    with the letter as a parameter.
"""

if __name__ == '__main__':
    import requests
    from sys import argv

    url = 'http://0.0.0.0:5000/search_user'
    q = argv[1]
    if not q or len(q) == 0:
        q = ""
    r = requests.post(url, data={'q': q})
    if r is None:
        print("No Result")
    else:
        try:
            print(r.json()['name'])
        except:  # noqa
            print("Not a valid JSON")
