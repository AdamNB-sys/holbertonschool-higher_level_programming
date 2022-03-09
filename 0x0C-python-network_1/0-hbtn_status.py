#!/usr/bin/python3
"""Fetches a url using urllib"""


import urllib.request


if __name__ == "__main__":
    """method to fetch url and print status"""
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        html = response.read()
        print('Body response:')
        print('\t- type: {}'.format(type(html)))
        print('\t- content: {}'.format(html))
        print('\t- utf-8 content: {}'.format(html.decode('utf-8')))
