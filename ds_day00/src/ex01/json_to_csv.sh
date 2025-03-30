#!/bin/sh

if [ -z "$1" ];then
    echo "Usage: $0 <path_to_file>"
    exit 1
fi

file="$1"

jq -r -f filter.jq "$file" > hh.csv

# success ?
if [ $? -ne 0 ]; then
  echo "Failed"
  exit 1
fi

