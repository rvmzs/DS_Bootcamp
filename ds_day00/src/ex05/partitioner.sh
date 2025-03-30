#!/bin/sh

if [ -z "$1" ]; then
    echo "Usage: $0 <csv_file>"
    exit 1
fi

input_file="$1"

mkdir -p partitions

header=$(head -n 1 "$input_file")

tail -n +2 "$input_file" | while IFS= read -r line; do
    date=$(echo "$line" | cut -d',' -f2 | cut -d'T' -f1 | tr -d '"')

    output_file="partitions/${date}.csv"
    if [ ! -f "$output_file" ]; then
        echo "$header" > "$output_file"
    fi

    echo "$line" >> "$output_file"
done