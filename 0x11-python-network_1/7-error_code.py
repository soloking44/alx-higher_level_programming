#!/usr/bin/python3
"""This code to
- Accept a URL
- Tranfers a request into URL
- Shows the body of the output.
"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]

    r = requests.get(url)
    if r.status_code >= 400:
        print("Error code: {}".format(r.status_code))
    else:
        print(r.text)
