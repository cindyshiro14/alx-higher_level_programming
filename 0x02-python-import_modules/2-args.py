#!/usr/bin/python3
import sys

if __name__ == "__main__":
    argc = len(sys.argv) - 1  # Subtract 1 for the script name itself
    args = sys.argv[1:]  # Exclude the script name from the arguments

    print("{} {}{}.".format(argc, "argument" if argc == 1 else "arguments", ":" if argc > 0 else "."))

    for i, arg in enumerate(args, start=1):
        print("{}: {}".format(i, arg))
