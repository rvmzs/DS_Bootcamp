#!/bin/sh

if [ -z "$1" ];then
    echo "Usage: $0 <csv_file>"
    exit 1
fi


input_file="$1"  
output_file="hh_uniq_positions.csv"


echo '"name","count"' > "$output_file"

awk -F '"' 'NR > 1 {print $6}' "$input_file" | sort | uniq -c | sort -nr | \
    awk '{print "\"" $2 "\"," $1}' >> "$output_file"