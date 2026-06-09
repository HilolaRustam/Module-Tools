#!/usr/bin/env python3

import sys 
import glob
import os 

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
       
def print_lines(files, number_lines==False, number_nonempty=False):
    line_no = 1     
    for file in files:
              
        
            