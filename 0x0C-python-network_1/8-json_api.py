#!/usr/bin/python3
"""
Sends POST request to a url in the form of a search method
./8-json_api <query>
"""


if __name__ == "__main__":
    """
    Implementing the requests post method to query a server for a
    properly formatted json file. if the file is found, the requests get
    method is then called to return the matching parameters found
    within, if any.
    """
    from requests import post, get
    import sys

    q = sys.argv[1]
    if not q or len(q) == 0:
        q = ""

    url = 'http://0.0.0.0:5000/search_user'
    request = post(url, data={'q': q})

    if request is None:
        print('No Result')
    else:
        try:
            response = request.json()
            id = response.get('id')
            name = response.get('name')
            print(f'[{id}] {name}')
        except Exception:
            print('Not valid JSON')
