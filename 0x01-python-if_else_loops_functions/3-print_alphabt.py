#!/usr/bin/python3

for letter in range(ord('a'), ord('z') + 1):
    if letter != ord('e') and letter != ord('q'):
        print("{}".format(chr(letter)), end='')

# Print a newline character to end the line
print()
