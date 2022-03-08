#!/usr/bin/python3
"""
    Python script that takes in a URL, sends a request to the URL
    and displays the value of the X-Request-Id
    variable found in the header of the response.
"""


if __name__ == "__main__":
    import urllib.request as request
    from sys import argv

    url = argv[1]
    r = request.Request(url)
    with request.urlopen(r) as response:
        print(response.headers.get('X-Request-Id'))
