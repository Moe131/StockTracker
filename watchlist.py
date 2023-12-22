# watchlist.py

from stock import Stock

class Watchlist:
    """ Class watchlist represents a list of stocks that can be
     added, removed or modified"""

    def __init__(self, name:str):
        """ Initializes the watchlist with count of zero and a string name"""
        self._name = name
        self._count = 0
        self._stocksList = []


    def count(self) -> int :
        """ Returns the number of stocks in the watchlist """
        return self._count


    def add(self, stock:Stock):
        """ Adds a stock object to the watchlist """
        self._count += 1
        self._stocksList.append(stock)


    def get(self, ticker: str) -> Stock:
        """ returns the stock object using the ticker symbol as parameter"""
        for stock in self._stocksList:
            if stock.getTicker() == ticker:
                return stock


    def remove(self, ticker: str ) -> None:
        """ removes the ticker stock from the watchlist """
        for stock in self._stocksList:
            if stock.getTicker() == ticker:
                stockToRemove = stock
        self._count -= 1
        self._stocksList.remove(stockToRemove)


    def printWatchlist(self) -> None:
        """ Prints watchlist stocks and their prices """
        print(f'Printing Watchlist {self._name} :\n')
        counter = 1
        print("#        Stock       Price       Change")
        print("---------------------------------------" )

        for stock in self._stocksList:
            print(counter, end='        ')
            print(str.format(stock.getTicker(), '10'), end= '    ')
            print(format(stock.getPrice(), '10.2f'), end=' ')
            print(format(stock.getPercentageChange(), '10.2f'))
            counter += 1


