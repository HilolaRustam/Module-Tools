#!/usr/bin/env python3

import sys 
import glob

def main():
    args = sys.argv[1:]
    
    if not args:
        print("Usage: cat [-n|-b] file...", file=sys.stderr)
        sys.exit(1)
        
    number_all = False
    number_nonempty = False
    paths = []
    
    for a in args:
        if a == "-n":
            number_all = True
        elif a == "-b":
            number_nonempty = True
        else:
            paths.append(a)
            
    if number_nonempty:
        number_all = False        
            
    files = expand_paths(paths)
    
    had_error = print_lines(
        files, 
        number_all=number_all,
        number_nonempty=number_nonempty,
        )

    if had_error:
        sys.exit(1)

    
def expand_paths(paths):
    """Expand glob patterns and return sorted unique file list."""
    files = []
    for p in paths:
        matches = glob.glob(p)
        if matches:
            files.extend(matches)
        else: 
            files.append(p) # keep as-is (will error later if missing)
    return sorted(files)

def read_lines(file):
    with open(file, "r", encoding="utf-8") as f:
        return f.readlines()
       
def print_lines(files, number_all=False, number_nonempty=False):
    had_error = False
    line_no = 1     
    for file in files:
        try:
            lines = read_lines(file)
        except FileNotFoundError:
            print(f"cat: {file}: No such file or directory", file=sys.stderr)
            had_error = True
            continue
        
        for line in lines:
            is_empty = (line.strip() == "")
            
            if number_nonempty:
                if not is_empty:
                    prefix = f"{line_no:6}\t"
                    line_no += 1
                else:
                    prefix = "" 
            elif number_all:
                prefix = f"{line_no:6}\t"
                line_no += 1
            else:
                prefix = ""
                
            # avoid double newlines: line already includes '\n'
            sys.stdout.write(prefix + line)
            
    return had_error        
            
if __name__ == "__main__":
    main()      
                                                
                    