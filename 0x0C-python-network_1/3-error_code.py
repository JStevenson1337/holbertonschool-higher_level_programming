#!/usr/bin/python3
"""
    Write a Python script that takes in
    a URL, sends a request to the URL and
    displays the body of the response
    (decoded in utf-8).
"""

if __name__ == "__main__":
    import urllib.request as request
    import urllib3 as error
    import sys

    url = sys.argv[1]
    try:
        with request.urlopen(url) as response:
            print(str(response.read(), 'utf-8'))
    except error as e:
        print("Error code: {}".format(e.code))
