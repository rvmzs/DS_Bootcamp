#!/bin/sh

# checkin : argument is exist 
if [ -z "$1" ];then
    echo "Usage: $0 <vacancy>"
    exit 1
fi    

vacancy=$(echo "$1" | jq -sRr @uri)
# vacancy=$(jq -sRr @uri <<< "$1")

url="https://api.hh.ru/vacancies?text=${vacancy}&per_page=20"

curl -o hh.json "$url"

# format
jq '.' hh.json > hh_temp.json && mv hh_temp.json hh.json

# success querry ?
if [ $? -ne 0 ]; then
  echo "Failed to fetch data from HeadHunter API"
  exit 1
fi

