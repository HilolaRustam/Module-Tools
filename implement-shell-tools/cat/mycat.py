#!/usr/bin/env python3

import sys 

def main():
    args = sys.argv[1:]
    
    if not args:
        print("Usage: cat [-n|-b] file...", file=sys.stderr)
        sys.exit(1)
        
    number_mode = "none"
    paths = []
    
    for a in args:
        if a == "-n":
            number_mode = "all"
        elif a == "-b":
            number_mode = "non_empty"
        else:
            paths.append(a)
    
 
    
    had_error = print_lines(
        paths, 
        number_mode=number_mode,
        )

    if had_error:
        sys.exit(1)


def read_lines(file):
    with open(file, "r", encoding="utf-8") as f:
        return f.readlines()
       
def print_lines(files, number_mode="none"):
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
            
            if number_mode == "non_empty":
                if not is_empty:
                    prefix = f"{line_no:6}\t"
                    line_no += 1
                else:
                    prefix = "" 
            elif number_mode=="all":
                prefix = f"{line_no:6}\t"
                line_no += 1
            else:
                prefix = ""
                
            # avoid double newlines: line already includes '\n'
            sys.stdout.write(prefix + line)
            
    return had_error        
            
if __name__ == "__main__":
    main()      
                                                
                    