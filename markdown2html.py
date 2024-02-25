#!/usr/bin/python3
'''This script takes two arguments: first is a markdown file name and the
    second is an html output filename
'''


import sys
import os


def main():
    """
    Converts a Markdown file to HTML.

    Args:
        sys.argv[1]: Path to the Markdown file.
        sys.argv[2]: Path to the output HTML file.
    """

    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py <markdown_file> <output_html>", file=sys.stderr)
        sys.exit(1)

    markdown_file = sys.argv[1]
    if not os.path.isfile(markdown_file):
        print(f"Missing file: {markdown_file}", file=sys.stderr)
        sys.exit(1)

    with open(markdown_file, "r") as f:
        markdown_content = f.read()

    html_content = convert_markdown_to_html(markdown_content)

    with open(sys.argv[2], "w") as f:
        f.write(html_content)

    sys.exit(0)


def convert_markdown_to_html(markdown_content):
    """
    Converts Markdown content to HTML.

    Args:
        markdown_content: The Markdown content as a string.

    Returns:
        The converted HTML content as a string.

    Raises:
        NotImplementedError: The implementation for this function is missing.
    """

    raise NotImplementedError("Please implement the markdown_to_html function with your chosen library")


if __name__ == "__main__":
    main()
