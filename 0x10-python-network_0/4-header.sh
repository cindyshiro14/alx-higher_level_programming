#!/bin/bash
# This script takes a URL, sends a GET request with a specific header, and displays the body of the response.
curl -sH "X-School-User-Id: 98" "$1"
