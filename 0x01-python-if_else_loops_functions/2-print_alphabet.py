#!/usr/bin/python3

alphabet = ""
for letter in range(ord('a'), ord('z') + 1):
    alphabet += chr(letter)

print("{}".format(alphabet), end="")
