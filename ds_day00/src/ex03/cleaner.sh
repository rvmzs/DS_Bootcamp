#!/bin/sh

if [ -z "$1" ]; then
    echo "Usage: $0 <csv_file>"
    exit 1
fi

input_file="$1"
output_file="hh_positions.csv"


head -n 1 "$input_file" > "$output_file"


tail -n +2 "$input_file" | while IFS= read -r line; do
    
    if [ "$line" != '"id","created_at","name","has_test","alternate_url"' ]; then
        id=$(echo "$line" | awk -F '"' '{print $2}')
        created_at=$(echo "$line" | awk -F '"' '{print $4}')
        name=$(echo "$line" | awk -F '"' '{print $6}')
        has_test=$(echo "$line" | awk -F ',' '{print $(NF-1)}')
        alternate_url=$(echo "$line" | awk -F ',' '{print $NF}'| tr -d '"')

        cleaned_name=""

        if echo "$name" | grep -q "Junior"; then
            cleaned_name="Junior"
        fi
        if echo "$name" | grep -q "Middle"; then
            cleaned_name="${cleaned_name:+$cleaned_name/}Middle"
        fi
        if echo "$name" | grep -q "Senior"; then
            cleaned_name="${cleaned_name:+$cleaned_name/}Senior"
        fi

        if [ -z "$cleaned_name" ]; then
            cleaned_name="-"
        fi

        echo "\"$id\",\"$created_at\",\"$cleaned_name\",$has_test,\"$alternate_url\"" >> "$output_file"
    fi
done < "$input_file"