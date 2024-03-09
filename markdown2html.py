#!/usr/bin/python3


'''Script that takes an argument 2 strings:
First argument is the name of the Markdown file
Second argument is the output file name
script converts the markdown file to HTML
The script will convert the following markdown syntax:
- Headers: Any number of #s at the start of a line
- Unordered listing: Lines that start with a dash (-)
- Ordered listing: Lines that start with a star (*)
- Text in double asterisks (**) is bold
- Text in double underscores (__) is italic
- Text in double brackets (()) is hashed
- Text in double parentheses (()) is case insensitive
The script will convert the markdown file to HTML and write it to the output file
If the markdown file does not exist, the script will print Missing <filename> and exit with a status code of 1
If the output file already exists, it will be overwritten
The script will exit with a status code of 0 upon success

Usage: ./markdown2html.py README.md README.html 
'''

import sys
import markdown

def convert_markdown_to_html(markdown_file, output_file):
    try:
        with open(markdown_file, 'r') as f:
            markdown_text = f.read()
    except FileNotFoundError:
        print(f"Missing {markdown_file}", file=sys.stderr)
        sys.exit(1)

    html_text = markdown.markdown(markdown_text)

    with open(output_file, 'w') as f:
        f.write(html_text)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py <markdown_file> <output_file>", file=sys.stderr)
        sys.exit(1)

    markdown_file = sys.argv[1]
    output_file = sys.argv[2]
    convert_markdown_to_html(markdown_file, output_file)
    sys.exit(0)