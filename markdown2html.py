#!/usr/bin/python3

import os
import sys
import markdown

"""
Converts a Markdown file to HTML.

Usage: ./markdown2html.py <input_file.md> <output_file.html>

Example: ./markdown2html.py README.md readme.html
"""

def main():
    """
    Parses arguments, performs Markdown conversion, and handles errors.
    """

    # Ensure correct number of arguments
    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py <input_file.md> <output_file.html>", file=sys.stderr)
        sys.exit(1)

    # Extract input and output filenames
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    # Check if input file exists
    if not os.path.exists(input_file):
        print(f"Missing {input_file}", file=sys.stderr)
        sys.exit(1)

    # Read Markdown content
    try:
        with open(input_file, 'r') as file:
            markdown_content = file.read()
    except IOError as e:
        print(f"Error reading file: {e}", file=sys.stderr)
        sys.exit(1)

    # Convert Markdown to HTML
    try:
        html_content = markdown.markdown(markdown_content)
    except Exception as e:
        print(f"Error converting Markdown: {e}", file=sys.stderr)
        sys.exit(1)

    # Write HTML content to output file
    try:
        with open(output_file, 'w') as file:
            file.write(html_content)
    except IOError as e:
        print(f"Error writing to file: {e}", file=sys.stderr)
        sys.exit(1)

    # Success
    print(f"Converted {input_file} to {output_file}")

if __name__ == "__main__":
    main()
