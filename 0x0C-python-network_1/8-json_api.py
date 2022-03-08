#!/usr/bin/python3
"""
    Write a Python script that takes in
    a letter and sends a POST request
    to http://0.0.0.0:5000/search_user
    with the letter as a parameter.
"""

if __name__ == '__main__':
    import urllib.request as request
    import sys

    if len(sys.argv) == 2:
        q = sys.argv[1]
        url = 'http://0.0.0.0:5000/search_user'
        q = {'q': q}
        post = request.Request(url, data=q)
        with request.urlopen(post) as response:
            data = response.read()
            print(data.decode('utf-8'))
    else:
        print('No result')
