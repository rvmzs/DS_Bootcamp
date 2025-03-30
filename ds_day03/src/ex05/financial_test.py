#!/usr/bin/env python3

import sys
import requests
from bs4 import BeautifulSoup
import time

def fetch_financial_data(ticker, field):
    ticker_upper = ticker.upper()
    url = f"https://finance.yahoo.com/quote/{ticker_upper}/financials?p={ticker_upper}"

    time.sleep(5)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"
    }
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        raise Exception(f"Error: Unable to access the page. Status code: {response.status_code}")

    soup = BeautifulSoup(response.text, 'html.parser')

    table_body = soup.find('div', class_='tableBody yf-9ft13')

    if not table_body:
        raise Exception(f"Error: Financial data not found for {ticker}.")

    rows = table_body.find_all('div', class_='row lv-0 yf-t22klz')

    for row in rows:
        title_div = row.find('div', {'class': 'rowTitle'})
        if title_div:
            title = title_div.get_text(strip=True)
            if title.lower() == field.lower():
                field_data = [col.get_text(strip=True).replace('$', '').split('.')[0] for col in row.find_all('div', class_='column')]
                return tuple(field_data)

    raise Exception(f"Error: The field '{field}' does not exist for the ticker '{ticker}'.")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: ./financial_test.py <ticker> <field>")
        sys.exit(1)

    ticker_symbol = sys.argv[1]
    field_name = sys.argv[2]

    try:
        result = fetch_financial_data(ticker_symbol, field_name)
        print(result)
    except Exception as e:
        print(e)
        sys.exit(1)

# Тесты

import pytest

# 1 is a total revenue
def test_fetch_total_revenue():
    result = fetch_financial_data('MSFT', 'Total Revenue')  
    expected_revenue = 'Gross Profit'
    assert result[0] == expected_revenue, f"Expected {expected_revenue}, but got {result[0]}"
# 2 is a tuple
def test_fetch_financial_data_returns_tuple():
    result = fetch_financial_data("MSFT", "Total Revenue")
    assert isinstance(result, tuple), "The result should be a tuple"

# 3 invalid ticker name, do I get an exception
def test_ticker_not_found():
    with pytest.raises(Exception, match="Financial data not found for NONEXISTENTTICKER"):
        fetch_financial_data("NONEXISTENTTICKER", "Total Revenue")