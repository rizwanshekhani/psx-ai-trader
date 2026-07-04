from models.trend_result import TrendResult


class TrendEngine:

    def analyze(self, latest):

        if (
            latest["Close"] > latest["EMA20"]
            and latest["EMA20"] > latest["EMA50"]
            and latest["EMA50"] > latest["EMA100"]
            and latest["EMA100"] > latest["SMA200"]
        ):
            return TrendResult(
                trend="STRONG BULLISH",
                score=10,
                confidence=95,
                ema20=latest["EMA20"],
                ema50=latest["EMA50"],
                ema100=latest["EMA100"],
                sma200=latest["SMA200"],
            )

        return TrendResult(
            trend="NEUTRAL",
            score=5,
            confidence=50,
            ema20=latest["EMA20"],
            ema50=latest["EMA50"],
            ema100=latest["EMA100"],
            sma200=latest["SMA200"],
        )