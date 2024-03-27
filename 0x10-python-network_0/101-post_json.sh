#!/bin/bash
# Transmit a JSON POST request into specified URL in actual JSON file.
curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
