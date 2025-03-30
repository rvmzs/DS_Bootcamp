import sys

def get_key(dict, value):
    value = str(value).lower()
    for key, val in dict.items():
        if value == str(val).lower():
            return key

def get_value(dict, k):
    k = str(k).lower()
    for key, val in dict.items():
        if str(key).lower() == k:
            return val
 
def main(ticker):
    COMPANIES = {
    'Apple': 'AAPL',
    'Microsoft': 'MSFT',
    'Netflix': 'NFLX',
    'Tesla': 'TSLA',
    'Nokia': 'NOK'
    }

    STOCKS = {
    'AAPL': 287.73,
    'MSFT': 173.79,
    'NFLX': 416.90,
    'TSLA': 724.88,
    'NOK': 3.37
    }
    
    if ticker.lower() not in (key.lower() for key in STOCKS.keys()):
        print("Unknown ticker")
    else:
        print(f"{get_key(COMPANIES, ticker)} {get_value(STOCKS, ticker)}")
    
if __name__ == "__main__":
    if len (sys.argv) == 2:
        main(sys.argv[1])

