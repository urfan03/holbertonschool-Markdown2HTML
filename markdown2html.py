#!/usr/bin/python3
"""
Converts a Markdown file to HTML.

Usage: ./markdown2html.py <markdown_file> <output_html>

Args:
    markdown_file: Path to the Markdown file.
    output_html: Path to the output HTML file.
"""


import os
import sys


def main():
    """
    Main function for converting Markdown to HTML.
    """

    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py <markdown_file> <output_html>", file=sys.stderr)
        sys.exit(1)

    markdown_file = sys.argv[1]
    output_html = sys.argv[2]

    if not os.path.isfile(markdown_file):
        print(f"Missing file: {markdown_file}", file=sys.stderr)
        sys.exit(1)

    with open(markdown_file, "r") as f:
        markdown_content = f.read()

    html_content = convert_markdown_to_html(markdown_content)

    with open(output_html, "w") as f:
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
