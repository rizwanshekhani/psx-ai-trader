from dataclasses import dataclass


@dataclass
class SwingPoint:
    index: int
    price: float
    kind: str   # HIGH or LOW


@dataclass
class SwingResult:
    highs: list
    lows: list