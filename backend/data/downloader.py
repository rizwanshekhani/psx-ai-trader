import yfinance as yf
import pandas as pd


def download_stock(symbol: str, period="1y"):
    """
    Download historical stock data.
    """
    stock = yf.Ticker(symbol)
    data = stock.history(period=period)

    return data


if __name__ == "__main__":
    df = download_stock("AAPL")

    print(df.tail())