from services.analysis_service import AnalysisService


def main():

    print("=" * 50)
    print("PSX AI Institutional Analyzer")
    print("=" * 50)

    symbol = input("Enter Symbol: ").upper()

    try:

        result = AnalysisService().analyze(symbol)

        print()
        print("=" * 50)
        print(f"Ticker : {result.symbol}")
        print("=" * 50)

        print("\nTREND")
        print("-" * 30)

        print(f"Trend       : {result.trend.trend}")
        print(f"Score       : {result.trend.score}/10")
        print(f"Confidence  : {result.trend.confidence}%")

        print()
        print(f"EMA20   : {result.trend.ema20:.2f}")
        print(f"EMA50   : {result.trend.ema50:.2f}")
        print(f"EMA100  : {result.trend.ema100:.2f}")
        print(f"SMA200  : {result.trend.sma200:.2f}")

        print("\nPRICE STRUCTURE")
        print("-" * 30)

        print(f"Structure : {result.structure.structure}")
        print(f"Score     : {result.structure.score}/10")

        print(f"Higher Highs : {result.structure.higher_highs}")
        print(f"Higher Lows  : {result.structure.higher_lows}")

        print("\nVOLUME")
        print("-" * 30)

        print(f"Status : {result.volume.status}")
        print(f"Score  : {result.volume.score}/10")
        print(f"RVOL   : {result.volume.relative_volume:.2f}")

    except Exception as e:
        print(f"\nError: {e}")


if __name__ == "__main__":
    main()  