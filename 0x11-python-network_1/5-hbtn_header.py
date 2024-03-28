#!/usr/bin/python3
"""Shows an X-Request-Id header data of a request to specified URL
"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]

    r = requests.get(url)
    print(r.headers.get("X-Request-Id"))
