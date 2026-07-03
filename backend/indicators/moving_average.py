import pandas as pd


def add_moving_averages(df: pd.DataFrame):
    """
    Add moving averages to dataframe.
    """

    df["EMA20"] = df["Close"].ewm(span=20).mean()
    df["EMA50"] = df["Close"].ewm(span=50).mean()
    df["EMA100"] = df["Close"].ewm(span=100).mean()
    df["SMA200"] = df["Close"].rolling(200).mean()

    return df