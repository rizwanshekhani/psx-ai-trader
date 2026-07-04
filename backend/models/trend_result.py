from dataclasses import dataclass


@dataclass
class TrendResult:
    trend: str
    score: int
    confidence: int
    ema20: float
    ema50: float
    ema100: float
    sma200: float