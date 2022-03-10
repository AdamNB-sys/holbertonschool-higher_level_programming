#!/usr/bin/python3
"""Sends request to url and returns correct error code"""


if __name__ == "__main__":
    """Requests url and returns error codes"""
    from urllib.request import Request, urlopen
    from urllib.error import HTTPError
    import sys

    url = Request(sys.argv[1])
    try:
        with urlopen(url) as response:
            print(response.read().decode('utf-8'))
    except HTTPError as error:
        print('Error code: {}'.format(error.code))
