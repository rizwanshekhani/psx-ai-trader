import pandas as pd


def find_swing_highs(df, window=2):
    swings = []

    for i in range(window, len(df) - window):
        current = df["High"].iloc[i]

        left = df["High"].iloc[i - window:i]
        right = df["High"].iloc[i + 1:i + window + 1]

        if current > left.max() and current > right.max():
            swings.append((i, current))

    return swings


def find_swing_lows(df, window=2):
    swings = []

    for i in range(window, len(df) - window):
        current = df["Low"].iloc[i]

        left = df["Low"].iloc[i - window:i]
        right = df["Low"].iloc[i + 1:i + window + 1]

        if current < left.min() and current < right.min():
            swings.append((i, current))

    return swings


def analyze_structure(df):

    swing_highs = find_swing_highs(df)
    swing_lows = find_swing_lows(df)

    if len(swing_highs) < 2 or len(swing_lows) < 2:
        return {
            "structure": "NOT ENOUGH DATA",
            "score": 0,
            "last_highs": [],
            "last_lows": []
        }

    last_highs = swing_highs[-2:]
    last_lows = swing_lows[-2:]

    hh = last_highs[-1][1] > last_highs[-2][1]
    hl = last_lows[-1][1] > last_lows[-2][1]

    if hh and hl:
        structure = "HIGHER HIGHS + HIGHER LOWS"
        score = 10
    elif hh:
        structure = "HIGHER HIGHS"
        score = 8
    elif hl:
        structure = "HIGHER LOWS"
        score = 8
    else:
        structure = "WEAK / SIDEWAYS"
        score = 5

    return {
        "structure": structure,
        "score": score,
        "last_highs": last_highs,
        "last_lows": last_lows
    }