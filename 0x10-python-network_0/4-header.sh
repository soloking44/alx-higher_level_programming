#!/bin/bash
# Code to accept a URL for an argument, sends a GET request to the URL, then shows the body of the outcome
curl "$1" -sX GET -H "X-School-User-Id: 98"
