# !/usr/bin/python3
"""
    Write a Python script that fetches
    https://intranet.hbtn.io/status
"""


if __name__ == '__main__':
    import urllib.request
    r = urllib.request.urlopen('https://intranet.hbtn.io/status')


