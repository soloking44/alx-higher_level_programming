#!/bin/bash
# Fetch a byte size within HTTP response header in a specified URL.
curl -s "$1" | wc -c
