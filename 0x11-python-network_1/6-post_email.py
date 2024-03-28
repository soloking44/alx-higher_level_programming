#!/usr/bin/python3
"""This code to:
- GET a URL with email address
- Transmites a POST request to URL and email as a data
- Shows the body of the outcome.
"""
Usage: ./6-post_email.py <URL> <email>
  - Prints the body of the output.
"""
import requests
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    value = {"email": argv[2]}
    req = requests.post(url, data=value)

    print(req.text)
