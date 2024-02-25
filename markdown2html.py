#!/usr/bin/python3
""" Write a script markdown2html.py that takes an argument 2 strings:

First argument is the name of the Markdown file
Second argument is the output file name """

import os
import sys
from markdown import markdown

def markdown2html(markdown_file, html_file):
   
    if len(sys.argv) != 3:
        raise ValueError("Usage: ./markdown2html.py README.md README.html")

    if not os.path.exists(markdown_file):
        raise FileNotFoundError(f"Missing file: {markdown_file}")

    with open(markdown_file, "r") as f_in, open(html_file, "w") as f_out:
        html = markdown(f_in.read())
        f_out.write(html)

    print(f"Markdown file '{markdown_file}' converted to HTML file '{html_file}' successfully!")

if __name__ == "__main__":
    try:
        markdown2html(*sys.argv[1:])
    except (ValueError, FileNotFoundError) as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    sys.exit(0)