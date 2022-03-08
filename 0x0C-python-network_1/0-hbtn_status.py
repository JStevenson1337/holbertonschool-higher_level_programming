#! /usr/bin/env python3

import urllib.request


req = urllib.request.Request('https://intranet.hbtn.io/status')
with urllib.request.urlopen(req) as response:
    the_page = response.read()
    print('Body response:')
    print('\t- type:', type(the_page))
    print('\t- content:', the_page)
    print('\t- utf8 content:', the_page.decode('utf-8'))

if __name__ == "__main__":
    pass
