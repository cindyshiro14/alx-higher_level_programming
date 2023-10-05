#!/usr/bin/python3
import pyc

if __name__ == "__main__":
    with open("hidden_4.pyc", "rb") as pyc_file:
        code = pyc_file.read()

    code_object = pyc.compile(code)
    names = [name for name in dir(code_object) if not name.startswith('__')]
    names.sort()

    for name in names:
        print(name)
