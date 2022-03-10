#!/usr/bin/python3
"""Uses requests to ping a url and display X-Request-Id"""


if __name__ == "__main__":
    """Displays content of X-Request-Id"""
    from requests import get
    import sys

    url = get(sys.argv[1])
    header = url.headers.get('X-Request-Id')
    print(header)
