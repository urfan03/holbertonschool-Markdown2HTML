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
    sys.exit(0)
if __name__ == "__main__":
    main()
