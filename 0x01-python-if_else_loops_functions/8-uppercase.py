#!/usr/bin/python3

def uppercase(s):
    for char in s:
        # Check if the character is a lowercase letter
        if ord('a') <= ord(char) <= ord('z'):
            # Convert the lowercase letter to uppercase and print it
            print(chr(ord(char) - 32), end='')
        else:
            # Print the character as is
            print(char, end='')

    # Print a newline character at the end
    print()
