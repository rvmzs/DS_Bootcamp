import sys

def main(company):
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
    if company.capitalize() not in COMPANIES:
        print("Unknown company")
        return 
    else:
        stock = COMPANIES.get(company.capitalize())
        print(STOCKS.get(stock))
        return


if __name__ == "__main__":
    if len (sys.argv) == 2:
        main(sys.argv[1])
