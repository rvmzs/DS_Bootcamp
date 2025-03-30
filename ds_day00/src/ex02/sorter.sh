#!/bin/sh


if [ -z "$1" ];then
    echo "Usage: $0 <csv_file>"
    exit 1
fi

csv_file="$1"

#existing file
if [ ! -f "$csv_file" ];then
    echo "File "$csv_file" is not exist"
    exit 1
fi

head -n 1 "$csv_file" > hh_sorted.csv
tail -n +2 "$csv_file" | sort -t, -k2,2 -k1,1n >> hh_sorted.csv





