#!/usr/bin/python3

import sys
import os

def convert_markdown_to_html(input_file, output_file):
    # Check if the Markdown file exists
    if not os.path.exists(input_file):
        sys.stderr.write(f"Missing {input_file}\n")
        sys.exit(1)

    # Perform the conversion from Markdown to HTML here
    # You can use a Markdown-to-HTML library like "markdown2" or "mistune"
    # Example: import markdown2; html = markdown2.markdown_path(input_file)

    # In this example, we'll just create a simple HTML file from the Markdown file
    with open(input_file, 'r') as md_file, open(output_file, 'w') as html_file:
        html_file.write("<html><body>\n")
        for line in md_file:
            html_file.write(line)
        html_file.write("</body></html>\n")

if __name__ == "__main__":
    # Check the number of arguments
    if len(sys.argv) < 3:
        sys.stderr.write("Usage: ./markdown2html.py README.md README.html\n")
        sys.exit(1)

    # Get the input and output file names from command line arguments
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    # Convert Markdown to HTML
    convert_markdown_to_html(input_file, output_file)

    # Exit with success status
    sys.exit(0)
