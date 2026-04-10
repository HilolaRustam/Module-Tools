#!/bin/bash

set -euo pipefail

flag="all"

if [ "${1:-}" = "-l" ]; then 
  flag="l"
  shift
elif [ "${1:-}" = "-w" ]; then
  flag="w"
  shift
elif [ "${1:-}" = "-c" ]; then
  flag="c"
  shift  
fi

for file in "$@"
do 
  if [ -d "$file" ]; then
    continue
  fi

   lines=0
   words=0
   chars=0

   while IFS= read -r line 
   do
     lines=$((lines + 1))
     words=$((words + $(echo "$line" | wc -w)))
     chars=$((chars + ${#line} + 1))
   done <"$file" 

   if [ "$flag" = "l" ]; then
    echo "$lines $file"
   elif [ "$flag" = "w" ]; then
    echo "$words $file"
   elif [ "$flag" = "c" ]; then
    echo "$chars $file"
   else 
    echo "$lines $words $chars $file" 
   fi    
done

