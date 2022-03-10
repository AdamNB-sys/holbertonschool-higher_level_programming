#!/usr/bin/python3
"""Sends POST request to URL in the form of an email"""


from urllib.request import Request, urlopen
from urllib.parse import urlencode
import sys


if __name__ == "__main__":
    """Method to fetch and return request id"""
    email = {'email': sys.argv[2]}
    payload = urlencode(email).encode('utf-8')
    query = Request(sys.argv[1], payload)
    with urlopen(query) as response:
        print(response.read().decode('utf-8'))
