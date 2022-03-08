#!/usr/bin/python3
""" query the status of a given url """


if __name__ == "__main__":
    import urllib.request as rq
    req = rq.Request("https://intranet.hbtn.io/status")
    with rq.urlopen(req) as response:
        site = response.read()
        print("Body response:")
        print(f"\t- type: {type(site)}")
        print(f"\t- content: {site}")
        print(f"\t- utf8 content: {site.decode('utf-8')}")
