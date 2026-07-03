import yfinance as yf
from .provider import DataProvider


class YahooProvider(DataProvider):

    def get_data(self, symbol):
        ticker = yf.Ticker(symbol)
        return ticker.history(period="1y")