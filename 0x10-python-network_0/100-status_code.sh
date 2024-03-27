#!/bin/bash
# Transmit a GET request into specified URL and show the outcome status code.
curl -s -o /dev/null -w "%{http_code}" "$1"
