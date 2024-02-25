#!/usr/bin/python3
''' Markdown to HTML '''
import sys
import markdown
from os import path


def convert_markdown_to_html(markdown_file, html_output_file):
    '''convert Markdown to HTML'''
    with open(markdown_file, 'r') as md_file:
        content = md_file.read()
    html = markdown.markdown(content)
    with open(html_output_file, 'w') as html_file:
        html_file.write(html)


if __name__ == "__main__":
    '''the number of arguments is less than 2'''
    if len(sys.argv) != 3:
        print('Usage: ./markdown2html.py README.md README.html' ,file=sys.stderr)
        exit(1)
    '''Markdown file doesn’t exist'''
    if not path.exists(sys.argv[1]):
        print('Missing {}'.format(sys.argv[1]), file=sys.stderr)
        exit(1)
    '''convert Markdown to HTML'''
    convert_markdown_to_html(sys.argv[1], sys.argv[2])
    sys.exit(0)