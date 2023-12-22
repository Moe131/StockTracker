# main.py

from stock import Stock
from watchlist import Watchlist

def main():

    mywatch = Watchlist('main')
    mywatch.add(Stock('AAPL'))
    mywatch.add(Stock('NIO'))
    mywatch.add(Stock('TSLA'))
    mywatch.add(Stock('SPY'))
    mywatch.printWatchlist()

if __name__ == '__main__':
    main()


# Sample Output
#
##        Stock       Price       Change
#---------------------------------------
#1        AAPL        194.68      -0.08
#2        NIO          8.28       4.67
#3        TSLA        254.50       2.98
#4        SPY        472.80       0.95
