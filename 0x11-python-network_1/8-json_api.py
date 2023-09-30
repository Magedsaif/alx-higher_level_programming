#!/usr/bin/python3
""" Python script that takes in a letter and sends
    a POST request to http://0.0.0.0:5000/search_user with
    the letter as a parameter.
"""
if __name__ == "__main__":
    import requests
    import sys
    url = 'http://0.0.0.0:5000/search_user'
    if len(sys.argv) > 1:
        q = sys.argv[1]
    else:
        q = ""
    payload = {'q': q}
    response = requests.post(url, data=payload)
    try:
        json = response.json()
        if json:
            id = json.get('id')
            name = json.get('name')
            print("[{}] {}".format(id, name))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
