# !/usr/bin/python3
"""
    Write a Python script that fetches
    https://intranet.hbtn.io/status
"""

if __name__ == '__main__':
    import urllib.request

    r = urllib.request.urlopen('https://intranet.hbtn.io/status')

    print("Body response:")
    print("\t- type: {}".format(type(r.text)))
    print("\t- content: {}".format(r.text))
