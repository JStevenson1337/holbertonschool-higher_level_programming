#!/usr/bin/python3
"""
    Write a Python script that takes in a URL and an
    email address, sends a POST request to the passed
    URL with the email as a parameter, and finally displays
    the body of the response.
"""

if __name__ == '__main__':

    import urllib.request
    import urllib.parse
    import sys

    url_arg = sys.argv[1]
    email_arg = sys.argv[2]

    data = {'email': email_arg}
    data = urllib.parse.urlencode(data)
    data = data.encode('ascii')
    req = urllib.request.Request(url_arg, data)
    with urllib.request.urlopen(req) as response:
        the_page = response.read()
        print(the_page.decode('utf-8'))
