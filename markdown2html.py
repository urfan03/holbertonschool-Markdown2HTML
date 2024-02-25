#!/usr/bin/python3
"""Convert Markdown to HTML"""

import sys
import os
import markdown

def convert_markdown_to_html(md_file, html_file):
    """Convert Markdown file to HTML file."""
    if not os.path.exists(md_file):
        sys.stderr.write(f"Missing {md_file}\n")
        sys.exit(1)

    with open(md_file, 'r') as md:
        markdown_text = md.read()

    html_text = markdown.markdown(markdown_text)

    with open(html_file, 'w') as html:
        html.write(html_text)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.stderr.write("Usage: ./markdown2html.py README.md README.html\n")
        sys.exit(1)

    md_file = sys.argv[1]
    html_file = sys.argv[2]

    convert_markdown_to_html(md_file, html_file)

    sys.exit(0)