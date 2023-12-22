# stock.py

import requests

API_KEY = 'e593ddc3ddc048dabe121b25532ea3a1'

class Stock:
    def __init__(self, ticker:str):
        self._ticker = ticker
        self._price = 0

    def getResponse(self) -> float:
        url = f'https://api.twelvedata.com/price?symbol={self._ticker}&apikey={API_KEY}&source=docs'
        response = requests.get(url).json()
        return response


    def getTicker(self) -> str:
        """ Returns the ticker symbol of the stock """
        return self._ticker


    def getPrice(self) -> float :
        self.calculatePrice()
        return self._price


    def setPrice(self, price:float) -> None :
        self._price = price

    def calculatePrice(self) -> None :
        response = self.getResponse()
        price = float(response['price'])
        self.setPrice(price)

    def getQuote(self) -> dict :
        url = f'https://api.twelvedata.com/quote?symbol={self._ticker}&apikey={API_KEY}&source=docs'
        response = requests.get(url).json()
        return response

    def getPreviousClosePrice(self,) -> float:
        quote = self.getQuote()
        previousClosePrice = float(quote['previous_close'])
        return previousClosePrice

    def getPercentageChange(self,) -> float:
        quote = self.getQuote()
        percentageChange = float(quote['percent_change'])
        return percentageChange
