#!/usr/bin/python3
"""This is code to:
- Gets a URL,
- Transmites a request into URL then shows the output
- In X-Request-Id result seen in header of the outcome.
"""
import sys
import urllib.request

if __name__ == "__main__":
    url = sys.argv[1]

    request = urllib.request.Request(url)
    with urllib.request.urlopen(request) as response:
        print(dict(response.headers).get("X-Request-Id"))
