#!/bin/bash
# This script takes a URL, sends a POST request with specific parameters, and displays the body of the response.
curl -sX POST "$1" -d "email=test@gmail.com&subject=I will always be here for PLD"
