from data.downloader import download_stock
from indicators.moving_average import add_moving_averages

from engines.trend_engine import TrendEngine
from engines.structure_engine import StructureEngine
from engines.volume_engine import VolumeEngine

from analysis.structure import analyze_structure

from models.analysis_result import AnalysisResult


class AnalysisService:

    def analyze(self, symbol: str):

        # Download data
        df = download_stock(symbol)

        if df.empty:
            raise ValueError(f"No data found for {symbol}")

        # Calculate indicators
        df = add_moving_averages(df)

        latest = df.iloc[-1]

        # Run engines
        trend = TrendEngine().analyze(latest)

        structure_dict = analyze_structure(df)
        structure = StructureEngine().analyze(structure_dict)

        volume = VolumeEngine().analyze(df)

        return AnalysisResult(
            symbol=symbol,
            trend=trend,
            structure=structure,
            volume=volume,
        )