#!/usr/bin/python3
"""Requests URL and displays value of X-Request-Id"""


if __name__ == "__main__":
    """Method to fetch and return request id"""
    import urllib.request
    import sys

    with urllib.request.urlopen(sys.argv[1]) as response:
        header = response.headers.get('X-Request-Id')
        print(header)
