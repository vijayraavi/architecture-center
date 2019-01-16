#!/usr/bin/env python
import re

input_file = open('index.md', 'r')
count_lines = 0

# Work on the previous line
prev_line = ""
next_indent = ""

def getname(line):
    pattern = re.compile('.*# (.*)')
    name = pattern.match(line)
    return name.group(1)

for line in input_file:
    name = ""
    contains = ""
    contents = ""
    indent = next_indent
    count_lines += 1

    # Look for a link
    pattern = re.compile('.*\[(.*)\]\((.*)\).*')
    link = pattern.match(line)

    if prev_line == "":
        toc = "- name: High Performance Computing on Azure\n"
        toc += "  href: index.md\n"
        #continue
    elif line.startswith("## "):
        name = getname(line)
        indent = ""
        contains = "  items: "
        next_indent = "  "
    elif line.startswith("### "):
        name = getname(line)
        indent = "  "
        contains = "  items: "
        next_indent = "      "
    elif link:
        contains = "  href: "
        name = link.group(1)
        contents = link.group(2)
    else:
        continue

    #toc += line
    toc += indent + "- name: " + name + "\n"
    toc += indent + contains + contents + "\n"
    prev_line = line

#print('number of lines:', count_lines)
print(toc)