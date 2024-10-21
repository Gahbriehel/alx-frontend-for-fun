#!/usr/bin/python3
import os
import sys

""" Markdown to html converter """

if len(sys.argv) < 3:
    print("Usage: ./markdown2html.py README.md README.html")
    sys.exit(1)

input_file = sys.argv[1]

if not os.path.isfile(input_file):
    print(f"Missing {input_file}", file=sys.stderr)
    sys.exit(1)

sys.exit(0)
