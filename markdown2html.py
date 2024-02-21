#!/usr/bin/python3

import sys
import markdown

if len(sys.argv) < 3:
    print("Usage: ./markdown2html.py <markdown_file> <output_file>", file=sys.stderr)
    sys.exit(1)

markdown_file = sys.argv[1]
output_file = sys.argv[2]

if not os.path.exists(markdown_file):
    print(f"Missing {markdown_file}", file=sys.stderr)
    sys.exit(1)

with open(markdown_file, 'r') as input_file:
    markdown_text = input_file.read()
    html_content = markdown.markdown(markdown_text)

with open(output_file, 'w') as output_file:
    output_file.write(html_content)

sys.exit(0)