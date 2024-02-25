#!/usr/bin/python3
""" Write a script markdown2html.py that takes an argument 2 strings:

First argument is the name of the Markdown file
Second argument is the output file name """

import sys
import os
if __name__ == "__main__":
    if len(sys.argv) <= 2:
        sys.stderr.write("Usage: ./markdown2html.py README.md README.html\n")
        exit(1)
    if not os.path.exists(sys.argv[1]):
        sys.stderr.write("Missing " + sys.argv[1] + "\n")
        exit(1)
    with open(sys.argv[1]) as IN:
        with open(sys.argv[2], 'w') as OUT:
            lines = IN.read().splitlines()
            html = ""
    exit(0)