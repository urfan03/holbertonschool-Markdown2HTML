#!/usr/bin/python3
""" Write a script markdown2html.py that takes an argument 2 strings:

First argument is the name of the Markdown file
Second argument is the output file name """
import sys
from mistletoe import markdown

def markdown_to_html(markdown_text):
  """
  Converts Markdown text to HTML using the mistletoe library.

  Args:
      markdown_text: The Markdown text to be converted.

  Returns:
      The converted HTML string.
  """
  html = markdown(markdown_text)
  return html

def main():
  """
  Reads Markdown from a file, converts it to HTML, and saves it to another file.

  Args:
      None.

  Returns:
      None.
  """
  if len(sys.argv) < 3:
    sys.stderr.write("Usage: ./markdown2html.py README.md README.html\n")
    sys.exit(1)

  with open(sys.argv[1], "r") as markdown_file:
    markdown_text = markdown_file.read()

  html_content = markdown_to_html(markdown_text)

  with open(sys.argv[2], "w") as output_file:
    output_file.write(html_content)

  sys.exit(0)

if __name__ == "__main__":
  main()