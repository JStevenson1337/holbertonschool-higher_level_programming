#!/usr/bin/python3
"""
     Python script that takes in a URL and an email,
     sends a POST request to the passed URL with the
     email as a parameter, and displays the body of the
     response (decoded in utf-8)
"""

if __name__ == "__main__":
    import urllib.request as request
    import sys

    url = sys.argv[1]
    email = sys.argv[2]
    payload = {'email': email}
    r = request.Request(url, data=str(payload).encode('utf-8'))
    print(request.urlopen(r).read().decode('utf-8'))
