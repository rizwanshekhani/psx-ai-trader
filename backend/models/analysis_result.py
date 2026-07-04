from dataclasses import dataclass
from models.trend_result import TrendResult
from models.structure_result import StructureResult
from models.volume_result import VolumeResult


@dataclass
class AnalysisResult:
    symbol: str
    trend: TrendResult
    structure: StructureResult
    volume: VolumeResult