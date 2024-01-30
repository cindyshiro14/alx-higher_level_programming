#!/bin/bash

# Check if the number of arguments is correct
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Get the URL from the command line argument
url=$1

# Send a request to the URL using curl and store the body in a temporary file
response=$(curl -sI "$url")
body_size=$(echo "$response" | grep -i Content-Length | awk '{print $2}')

# Display the size of the body in bytes
echo "$body_size"
