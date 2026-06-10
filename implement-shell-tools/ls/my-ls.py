#!/usr/bin/env python3

import sys
import os

def list_dir(path, show_all=False, one_per_line = False):
    try:
        entries = os.listdir(path)
    except FileNotFoundError:
        print(f"ls: cannot access '{path}': No such file or directory", file=sys.stderr)
        return
    
    entries = sorted(entries)
    
    if show_all:
        normal = sorted([e for e in entries if not e.startswith('.')])
        hidden = sorted([e for e in entries if e.startswith('.')])
        
        entries = [".", ".."] + normal + hidden
    else:    
        entries = sorted([e for e in entries if not e.startswith('.')])

    for entry in entries:
        print(entry)

def main():
    args = sys.argv[1:]

    show_all = False
    one_per_line = False
    paths = []

    for a in args:
        if a == "-a":
            show_all = True
        elif a == "-1":
            one_per_line = True    
        else:
            paths.append(a)

    if not paths:
        paths = ["."]

    for path in paths:
        list_dir(path, show_all, one_per_line)

if __name__ == "__main__":
    main()