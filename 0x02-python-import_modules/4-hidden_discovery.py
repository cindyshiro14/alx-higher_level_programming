#!/usr/bin/python3.8
import uncompyle6
import sys

if __name__ == "__main__":
    with open("hidden_4.pyc", "rb") as pyc_file:
        source_code = uncompyle6.decompile(3.8, pyc_file.read())

    # Extract variable names
    names = [line.split(" = ")[0] for line in source_code.splitlines() if "=" in line]

    # Filter and print the names
    for name in names:
        if not name.startswith("__"):
            print(name)
