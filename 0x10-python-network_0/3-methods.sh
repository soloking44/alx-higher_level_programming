#!/bin/bash
# Show each HTTP methods to server of specified URL will take.
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
