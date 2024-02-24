#!/usr/bin/python3
import sys
import os
import markdown


def convert_markdown_to_html(md_file, html_file):
    
    if not os.path.exists(md_file):
        print(f"Missing {md_file}", file=sys.stderr)
        sys.exit(1)

    with open(md_file, 'r') as f:
        markdown_text = f.read()

    html_text = markdown.markdown(markdown_text)

    with open(html_file, 'w') as f:
        f.write(html_text)


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py <Markdown file> <HTML output file>", file=sys.stderr)
        sys.exit(1)

    md_file = sys.argv[1]
    html_file = sys.argv[2]

    convert_markdown_to_html(md_file, html_file)

    sys.exit(0)