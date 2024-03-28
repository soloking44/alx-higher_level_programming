#!/usr/bin/python3
"""
A code which accept URL with email address, transfer a POST request to
given URL and the email as a data, and shows the body
of the output.
Usage: ./6-post_email.py <URL> <email>
  - Shows the body of the outcome.
"""
import requests
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    value = {"email": argv[2]}
    req = requests.post(url, data=value)

    print(req.text)
