#! /usr/bin/env python3
""" query the status of a given url """


def url_read():
    """ Function that reads the content of a URL """
    from urllib.request import urlopen, Request
    req = Request("http://intranet.hbtn.io/status")
    with urlopen(req) as response:
        site = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(site)))
        print("\t- content: {}".format(site))
        print("\t- utf8 content: {}".format(site.decode("utf-8")))


if __name__ == "__main__":
    url_read()
