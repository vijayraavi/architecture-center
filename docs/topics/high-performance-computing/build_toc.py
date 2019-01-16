#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import codecs

input_file = open('index.md', 'r')
count_lines = 0

def getname(line):
    pattern = re.compile('.*# (.*)')
    name = pattern.match(line)
    return name.group(1)

def overviewlink(name):
    shortname = name.lower()
    return str(shortname).replace(" ", "-")

toc = ""

toc_list = []
toc_list.append({'level': 1, 'name': "High Performance Computing on Azure", 'href':"index.md"})

for line in input_file:
    # Look for an inline link
    inline_match = re.compile('.*\[(.*)\]\((.*)\).*')
    inline_link = inline_match.match(line)

    # Look for an html link
    href_match = re.compile('.*href=\"(.*)\" .*')
    href_link = href_match.match(line)

    # Look for an h3 title
    h3_match = re.compile('.*<h3>(.*)</h3>.*')
    h3_title = h3_match.match(line)

    if line.startswith("## "):
        name = getname(line)
        level = 2
        toc_list.append({'level': level, 'name': name})
    elif line.startswith("### "):
        name = getname(line)
        level = 3
        toc_list.append({'level': level, 'name': name})
    elif inline_link:
        # Skip internal links
        if re.match('^#.*', inline_link.group(2)):
            continue

        toc_list.append({'level': level + 1, 'name': inline_link.group(1), 'href': inline_link.group(2)})
    elif href_link:
        url = href_link.group(1)
        continue
    elif h3_title:
        toc_list.append({'level': level + 1, 'name': h3_title.group(1), 'href': url})
    else:
        continue

# Build the TOC

for i in range(0,len(toc_list)):
    item_level = toc_list[i].get('level')
    item_name = toc_list[i]['name']

    if item_level == 1:
        indent = ""
    else:
        indent = "  " * (item_level - 1)

    # If there are multiple items below a heading, provide an overview link
    if i+1 != len(toc_list):
        if toc_list[i+1].get('level') > item_level:
            toc += indent + "- name: " + item_name + '\n'
            toc += indent + "  items:" + "\n"
            if item_level != 1:
                toc += indent + "  " + "- name: Overview\n"
                toc += indent + "  " + "  href: index.md#" + overviewlink(item_name) + "\n"
        elif toc_list[i].get('href'):
            if ".com" in toc_list[i].get('href'):
                if re.match('^(.(?<!docs.microsoft.com))*?$', toc_list[i].get('href')):
                    item_name = item_name + u" ↗"
            toc += indent + "- name: " + item_name + '\n'
            toc += indent + "  href: " + toc_list[i].get('href') + "\n"
        else:
            toc += indent + "- name: " + item_name + '\n'
            toc += indent + "  href: index.md#" + overviewlink(item_name) + "\n"

output_file = codecs.open('TOC.yml', 'w', "utf-8")
output_file.write(toc)
output_file.close()