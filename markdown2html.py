import sys
import markdown

def convert_markdown_to_html(markdown_file, output_file):
    try:
        # Read the content of the Markdown file
        with open(markdown_file, 'r') as f:
            markdown_content = f.read()
        
        # Convert Markdown to HTML
        html_content = markdown.markdown(markdown_content)

        # Write the HTML content to the output file
        with open(output_file, 'w') as f:
            f.write(html_content)

        print("HTML file generated successfully.")
        return 0

    except FileNotFoundError:
        print(f"Missing {markdown_file}", file=sys.stderr)
        return 1

if __name__ == "__main__":
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 3:
        print("Usage: ./markdown2html.py <Markdown file> <Output file>", file=sys.stderr)
        sys.exit(1)

    markdown_file = sys.argv[1]
    output_file = sys.argv[2]

    # Convert Markdown to HTML
    exit_code = convert_markdown_to_html(markdown_file, output_file)
    sys.exit(exit_code)