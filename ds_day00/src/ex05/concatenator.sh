#!/bin/sh

if [ -z "$1" ];then
    echo "Usage: $0 <csv_file>"
    exit 1
fi

output_file="$1"

: > "$output_file"

first_partition=$(ls partitions/*.csv | head -n 1)
if [ -f "$first_partition" ]; then
    head -n 1 "$first_partition" >> "$output_file"
fi

for partition in partitions/*.csv; do
    tail -n +2 "$partition" >> "$output_file"
done
