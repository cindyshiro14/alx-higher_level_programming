#!/usr/bin/python3

output = ""
for letter in range(ord('a'), ord('z') + 1):
    if letter != ord('e') and letter != ord('q'):
        output += chr(letter)

print("{}".format(output), end='')
