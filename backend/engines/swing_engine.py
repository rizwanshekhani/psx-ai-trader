from models.swing_result import SwingPoint, SwingResult


class SwingEngine:

    def analyze(self, df, window=3):

        highs = []
        lows = []

        for i in range(window, len(df) - window):

            current_high = df["High"].iloc[i]
            current_low = df["Low"].iloc[i]

            left_high = df["High"].iloc[i-window:i]
            right_high = df["High"].iloc[i+1:i+window+1]

            left_low = df["Low"].iloc[i-window:i]
            right_low = df["Low"].iloc[i+1:i+window+1]

            if current_high > left_high.max() and current_high > right_high.max():
                highs.append(
                    SwingPoint(i, current_high, "HIGH")
                )

            if current_low < left_low.min() and current_low < right_low.min():
                lows.append(
                    SwingPoint(i, current_low, "LOW")
                )

        return SwingResult(
            highs=highs,
            lows=lows,
        )