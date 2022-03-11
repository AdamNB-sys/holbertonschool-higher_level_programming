#!/usr/bin/python3
"""Pings a url and displays the response as an error code"""


if __name__ == "__main__":
    """Uses the requests get method"""
    from requests import get
    import sys

    status = get(sys.argv[1])
    if status.status_code >= 400:
        print('Error code: {}'.format(status.status_code))
    else:
        print(status.text)
