#!/bin/bash

# Check if the number of arguments is correct
if [ "$#" -ne 2 ]; then
    echo "Usage: $0 <URL> <JSON_FILE>"
    exit 1
fi

# Check if the JSON file exists
if [ ! -f "$2" ]; then
    echo "Error: JSON file not found"
    exit 1
fi

# Send a JSON POST request to the URL with the contents of the JSON file
curl -sX POST "$1" -H "Content-Type: application/json" -d @"$2"
