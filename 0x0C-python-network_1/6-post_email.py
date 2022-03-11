#!/usr/bin/python3
"""Sends email as post request"""


if __name__ == "__main__":
    """Uses the requests post method to send an email to a server"""
    from requests import post
    import sys

    email = {'email': sys.argv[2]}
    post_req = post(sys.argv[1], email)
    print(post_req.text)
