#!/usr/bin/python3
"""Fetches url using requests"""


if __name__ == "__main__":
    """Gets url"""
    from requests import get

    url = get('https://intranet.hbtn.io/status')
    html = url.text
    print('Body response:')
    print('\t- type: {}'.format(type(html)))
    print('\t- content: {}'.format(html))
