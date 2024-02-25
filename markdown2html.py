#!/usr/bin/python3

import os
import sys
from markdown import markdown
""" Write a script markdown2html.py that takes an argument 2 strings:

First argument is the name of the Markdown file
Second argument is the output file name """

def markdown2html(markdown_file, html_file):
    """Converts a Markdown file to HTML using the markdown library.

    Args:
        markdown_file (str): The path to the Markdown file.
        html_file (str): The path to the output HTML file.

    Raises:
        ValueError: If the number of arguments is incorrect.
        FileNotFoundError: If the specified Markdown file doesn't exist.
    """

    if len(sys.argv) != 3:
        raise ValueError("Usage: ./markdown2html.py <markdown_file> <html_file>")

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