#!/usr/bin/python3
'''This script takes two arguments: first is a markdown file name and the
    second is an html output filename
'''


import sys

def main():
  # Check if enough arguments are provided
  if len(sys.argv) < 3:
    print("Usage: ./markdown2html.py <markdown_file> <output_html>", file=sys.stderr)
    sys.exit(1)

  # Check if the Markdown file exists
  if not os.path.isfile(sys.argv[1]):
    print(f"Missing file: {sys.argv[1]}", file=sys.stderr)
    sys.exit(1)

  # Read the Markdown file content
  with open(sys.argv[1], "r") as markdown_file:
    markdown_content = markdown_file.read()

  # Convert Markdown to HTML (replace with your preferred conversion method)
  html_content = convert_markdown_to_html(markdown_content)

  # Write HTML content to output file
  with open(sys.argv[2], "w") as output_file:
    output_file.write(html_content)

  # Exit with success
  sys.exit(0)

# Placeholder function for Markdown conversion. You need to implement this based on your chosen library
def convert_markdown_to_html(markdown_content):
  raise NotImplementedError("Please implement the markdown_to_html function with your chosen library")

if __name__ == "__main__":
  main()