#!/usr/bin/env python3

import cProfile
import pstats
import httpx
import sys
from bs4 import BeautifulSoup
import time

def fetch_financial_data(ticker, field):
    ticker_upper = ticker.upper()
    url = f"https://finance.yahoo.com/quote/{ticker_upper}/financials/"

    #time.sleep(5)
    headers = {
        # place for header
    }

    response = httpx.get(url, headers=headers)
    response.raise_for_status()

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


def main(ticker, field):
    result = fetch_financial_data(ticker, field)
    return result

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: ./financial_enhanced.py <ticker> <field>")
        sys.exit(1)

    ticker_symbol = sys.argv[1]
    field_name = sys.argv[2]

    pr = cProfile.Profile()
    pr.enable()

    
    result = main(ticker_symbol, field_name)
    print(result)

   
    pr.disable()

    with open("profiling-ncalls.txt", "w") as f:

        f.write(str(result) + "\n")  

        # Профилирование
        ps = pstats.Stats(pr, stream=f)
        ps.sort_stats('ncalls')  # Сортировка 
        ps.print_stats()
