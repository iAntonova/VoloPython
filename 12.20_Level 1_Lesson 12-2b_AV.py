# Lesson 12 - 2
# Write a program that will print a sorted list of all environment variables.
# Sorting by a variable name should be either direct or reversed.
# Sorting mode should be defined as a command line argument. Default is the direct mode.

import os
import sys
import argparse


if __name__ == "__main__":

    try:

        parser = argparse.ArgumentParser(prog=sys.argv[0],
                                         description="Print environment variables")
        parser.add_argument("-r", "--reversed",
                            help="reverse sort order",
                            action="store_true",
                            default=False)

        args = parser.parse_args()

        for var in sorted(os.environ, reverse=args.reversed):
            print(f"{var}: {os.environ[var]}")

    except (argparse.ArgumentError, argparse.ArgumentTypeError) as x:
        sys.stderr.write(str(x) + "\n")
        sys.exit(1)
    else:
        sys.exit(0)