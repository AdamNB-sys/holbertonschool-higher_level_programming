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

    if len(sys.argv) <= 1:
        q = ""
    else:
        q = sys.argv[1]

    url = 'http://0.0.0.0:5000/search_user'
    request = post(url, data={'q': q})

    try:
        response = request.json()
        if len(response) == 0:
            print('No result')
        else:
            id = response.get('id')
            name = response.get('name')
            print(f'[{id}] {name}')
    except Exception:
        print('Not valid JSON')
