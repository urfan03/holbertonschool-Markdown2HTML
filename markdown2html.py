#!/usr/bin/python3
'''This script takes two arguments: first is a markdown file name and the
    second is an html output filename
'''


import sys
import os
import hashlib
import re


def find_lines(lines, index, type):
    selected = []

    if type == "p":
        for i in range(index, len(lines)):
            lines[i] = bold(italic(hash_case_ins(lines[i])))
            if lines[i] and not lines[i].startswith("#") and not lines[i].startswith("- ") and not lines[i].startswith("* "):
                selected.append(lines[i])
            else:
                break
        return selected

    if type in ["ul", "ol"]:
        symbol = "-" if type == "ul" else "*"
        for i in range(index, len(lines)):
            lines[i] = bold(italic(hash_case_ins(lines[i])))
            if lines[i] and lines[i].startswith(f"{symbol} "):
                selected.append(lines[i])
            else:
                break
        return selected


def heading(line):
    count = line.count("#")
    return f"<h{count}>{line[count + 1:]}</h{count}>\n"


def listing(lines, type):
    html = f"<{type}>\n"
    for line in lines:
        html += f"<li>{line[2:]}</li>\n"
    html += f"</{type}>\n"
    return html


def paragraph(lines):
    html = "<p>\n"
    for index, line in enumerate(lines):
        html += f"{line}\n"
        if index == len(lines) - 1:
            continue
        html += "<br />\n"
    html += "</p>\n"
    return html


def bold(line):
    line = line.replace("**", "<b>", 1).replace("**", "</b>", 1)
    return line


def italic(line):
    line = line.replace("__", "<em>", 1).replace("__", "</em>", 1)
    return line


def hash_case_ins(line):
    match = re.search(r'\[\[(.*?)\]\]', line)
    while match:
        hashed = hashlib.md5(match.group(1).encode()).hexdigest()
        line = line.replace(line[match.start():match.end()], hashed)
        match = re.search(r'\[\[(.*?)\]\]', line)
    return line


def case_ins(line):
    match = re.search(r'\(\((.*?)\)\)', line)
    while match:
        text = re.sub("c", "", match.group(1), flags=re.IGNORECASE)
        line = line.replace(line[match.start():match.end()], text)
        match = re.search(r'\(\((.*?)\)\)', line)
    return line


if __name__ == "__main__":
    if len(sys.argv) < 3:
        sys.stderr.write("Usage: ./markdown2html.py README.md README.html\n")
        sys.exit(1)
    if not os.path.exists(sys.argv[1]):
        sys.stderr.write("Missing " + sys.argv[1] + "\n")
        sys.exit(1)

    with open(sys.argv[1]) as read_file:
        with open(sys.argv[2], "w") as html_file:
            lines = read_file.read().splitlines()
            content = ""

            for index, line in enumerate(lines):
                line = bold(italic(hash_case_ins(line)))
                if not line:
                    continue
                elif line.startswith("#"):
                    content += heading(line)
                elif line.startswith("- ") or line.startswith("* "):
                    type = "ul" if line.startswith("- ") else "ol"
                    selected = find_lines(lines, index, type)
                    del lines[index:index + len(selected)]
                    content += listing(selected, type)
                else:
                    selected = find_lines(lines, index, "p")
                    del lines[index:index + len(selected)]
                    content += paragraph(selected)
            html_file.write(content)

    sys.exit(0)
