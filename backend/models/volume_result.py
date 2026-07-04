from dataclasses import dataclass


@dataclass
class VolumeResult:
    current_volume: float
    average_volume: float
    relative_volume: float
    status: str
    score: int