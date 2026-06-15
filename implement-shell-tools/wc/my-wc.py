#!/usr/bin/env python3

import sys


def count_file(path):
    with open(path, "rb") as f:
        content = f.read()

    byte_count = len(content)
    text = content.decode("utf-8", errors="ignore")

    line_count = text.count("\n")
    word_count = len(text.split())

    return line_count, word_count, byte_count



def main():
    args = sys.argv[1:]

    show_l = False
    show_w = False
    show_c = False

    paths = []
    
    
    # parse args
    for a in args:
        if a == "-l":
            show_l = True
        elif a == "-w":
            show_w = True
        elif a == "-c":
            show_c = True
        else:
            paths.append(a)

    # default: show all
    if not (show_l or show_w or show_c):
        show_l = show_w = show_c = True

    files = paths

    total_l = 0
    total_w = 0
    total_c = 0
    
    results = []
    had_error = False
    
    for file in files:
        try:
            l, w, c = count_file(file)
        except FileNotFoundError:
            print(
                f"wc: {file}: No such file or directory",
                file=sys.stderr,
            )
            had_error = True
            continue
        
        total_l += l
        total_w += w
        total_c += c
        
        results.append((l,w,c, file))
        
     # print per-file results (GNU-aligned formatting)
    for l, w, c, file in results:

        parts = []
        if show_l:
            parts.append(f"{l:3}")
        if show_w:
            parts.append(f"{w:4}")
        if show_c:
            parts.append(f"{c:4}")


        print("".join(parts) + " " + file)
        
    # print total if multiple files
    if len(results) > 1:
        parts = []

        if show_l:
            parts.append(f"{total_l:3}")
        if show_w:
            parts.append(f"{total_w:4}")
        if show_c:
            parts.append(f"{total_c:4}")

        
        print("".join(parts) + " total")
        
    if  had_error:
        sys.exit(1)   


if __name__ == "__main__":
    main()