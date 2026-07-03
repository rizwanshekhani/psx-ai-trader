def analyze_trend(latest):
    """
    Analyze trend using moving averages.
    """

    if (
        latest["Close"] > latest["EMA20"]
        and latest["EMA20"] > latest["EMA50"]
        and latest["EMA50"] > latest["EMA100"]
        and latest["EMA100"] > latest["SMA200"]
    ):
        return "STRONG BULLISH", 10

    if (
        latest["Close"] > latest["EMA20"]
        and latest["EMA20"] > latest["EMA50"]
    ):
        return "BULLISH", 8

    if latest["Close"] > latest["SMA200"]:
        return "NEUTRAL", 5

    return "BEARISH", 2