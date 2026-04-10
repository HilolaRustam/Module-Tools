#!/bin/bash

set -euo pipefail

number_lines=false 
number_non_empty=false

# check for flags
if [ "${1:-}" = "-n" ]; then 
  number_lines=true
  shift
elif [ "${1:-}" = "-b" ]; then
  number_non_empty=true
  shift
fi

count=1

# Loop through all files

for file in "$@"
do
  while IFS= read -r line
  do
    if [ "$number_lines" = true ]; then
    echo "$count $line"
    count=$((count+1))

    else if [ "$number_non_empty" = true ]; then
      if [ -n "$line" ]; then
        echo "$count $line"
        count=$((count+1))
      else
        echo ""
       fi

     else
       echo "$line"
     fi   
   fi
  done < "$file" 
done