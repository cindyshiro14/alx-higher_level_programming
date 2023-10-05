#!/usr/bin/python3
import py_compile
import os
import sys
import re

if __name__ == "__main__":
    # Compile the .pyc file if it exists
    pyc_file = "hidden_4.pyc"
    if not os.path.isfile(pyc_file):
        print("File {} not found.".format(pyc_file))
        sys.exit(1)

    try:
        py_compile.compile(pyc_file)
    except py_compile.PyCompileError:
        print("Compilation of {} failed.".format(pyc_file))
        sys.exit(1)

    # Import the compiled module and list its attributes (names)
    compiled_module_name = re.sub(r'\.pyc$', '', pyc_file)
    compiled_module = __import__(compiled_module_name)

    names = [name for name in dir(compiled_module) if not name.startswith('__')]
    names.sort()

    for name in names:
        print(name)
