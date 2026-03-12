#!/bin/bash

set -euo pipefail

# NOTE: This is a stretch exercise - it is optional.

# TODO: Write a command to output the total of adding together all players' first scores.
awk '{sum += $3} END {print sum}' scores-table.txt
# Your output should be exactly the number 54.
