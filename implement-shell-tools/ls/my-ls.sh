  #!/bin/bash
 set -euo pipefail

show_all=false

# handle -a
if [ "${1:-}" = "-a" ]; then
  show_all=true
  shift
fi 

# directory (default current)
 dir="."

 if [ "${1:-}" != "" ]; then
   dir="$1"
 fi 

 #choose pattern
 if [ "$show_all" = true ]; then 
   files="$dir"/.*
 else
   files="$dir"/*
 fi
 # loop      
 for file in $files
 do 
   name="$(basename "$file")"

   if [ "$name" = "." ] || [ "$name" = ".." ]; then 
   continue
   fi
   echo "$name"
  done  