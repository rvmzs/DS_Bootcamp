#!/usr/bin/env python3

import sys
import requests
from bs4 import BeautifulSoup
import time, cProfile, pstats


def fetch_financial_data(ticker, field):
    ticker_upper = ticker.upper()
    url = f"https://finance.yahoo.com/quote/{ticker_upper}/financials?p={ticker_upper}"

    time.sleep(5)
    headers = {
        # place for header
    }
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        raise Exception(f"Error: Unable to access the page. Status code: {response.status_code}")

    soup = BeautifulSoup(response.text, 'html.parser')

    # 'tableBody yf-9ft13'
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
        print("Usage: ./financial.py <ticker> <field>")
        sys.exit(1)

    ticker_symbol = sys.argv[1]
    field_name = sys.argv[2]
    pr = cProfile.Profile()
    pr.enable()

    try:
        result = fetch_financial_data(ticker_symbol, field_name)
        pr.disable()
        print(result)  
    except Exception as e:
        print(e)
        sys.exit(1)
    
    with open("pstats-cumulative.txt", "w") as f:
        f.write(str(result)+ '\n')
        ps = pstats.Stats(pr, stream=f)
        ps.sort_stats('cumulative')  # Сортировка 
        ps.print_stats(5)