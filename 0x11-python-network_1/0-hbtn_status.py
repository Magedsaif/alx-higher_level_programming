#!/usr/bin/python3
"""Script that fetches https://intranet.hbtn.io/status."""

import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        contents_read = response.read()
        print('Body response:')
        print("\t- type: {}".format(type(contents_read)))
        print("\t- content: {}".format(contents_read))
        print("\t- utf8 content: {}".format(contents_read.decode('utf-8')))
