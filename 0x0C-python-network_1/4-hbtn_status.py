#!/usr/bin/python3
"""
    Write a Python script that fetches
    https://intranet.hbtn.io/status
"""


if __name__ == '__main__':
    import requests

    r = requests.get('https://intranet.hbtn.io/status')
    print(f"Body response:\n\t- type: {type(r.text)}\n\t- content: {r.text}")
