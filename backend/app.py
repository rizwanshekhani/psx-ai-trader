from data.downloader import download_stock
from indicators.moving_average import add_moving_averages
from analysis.trend import analyze_trend


def main():
    print("=" * 50)
    print("PSX AI Institutional Analyzer")
    print("=" * 50)

    symbol = input("Enter Symbol: ")

    # Download stock data
    df = download_stock(symbol)

    # Calculate indicators
    df = add_moving_averages(df)

    # Latest candle
    latest = df.iloc[-1]

    # Analyze trend
    trend, score = analyze_trend(latest)

    print()
    print(f"Ticker        : {symbol}")
    print(f"Current Price : {latest['Close']:.2f}")

    print("\nTrend")
    print("-" * 30)
    print(f"EMA20   : {latest['EMA20']:.2f}")
    print(f"EMA50   : {latest['EMA50']:.2f}")
    print(f"EMA100  : {latest['EMA100']:.2f}")
    print(f"SMA200  : {latest['SMA200']:.2f}")

    print()
    print(f"Trend : {trend}")
    print(f"Score : {score}/10")


if __name__ == "__main__":
    main()