#!/usr/bin/python3
""" query the status of a given url """


def hbtn_status():
    """ Function that reads the content of a URL """
    from urllib.request import urlopen, Request
    req = Request("http://intranet.hbtn.io/status")
    with urlopen(req) as response:
        site = response.read()
        print("Body response:")
        print(f"\t- type: {type(site)}")
        print(f"\t- content: {site}")
        print(f"\t- utf8 content: {site.decode('utf-8')}")


if __name__ == "__main__":
    hbtn_status()
