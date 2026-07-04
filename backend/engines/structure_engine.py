from models.structure_result import StructureResult


class StructureEngine:

    def analyze(self, structure_result_dict):

        last_highs = structure_result_dict["last_highs"]
        last_lows = structure_result_dict["last_lows"]

        hh = False
        hl = False

        last_high = previous_high = None
        last_low = previous_low = None

        if len(last_highs) >= 2:
            previous_high = last_highs[-2][1]
            last_high = last_highs[-1][1]
            hh = last_high > previous_high

        if len(last_lows) >= 2:
            previous_low = last_lows[-2][1]
            last_low = last_lows[-1][1]
            hl = last_low > previous_low

        if hh and hl:
            structure = "BULLISH STRUCTURE"
            score = 10
        elif hh:
            structure = "HIGHER HIGHS"
            score = 8
        elif hl:
            structure = "HIGHER LOWS"
            score = 8
        else:
            structure = "SIDEWAYS / WEAK"
            score = 5

        return StructureResult(
            structure=structure,
            score=score,
            higher_highs=hh,
            higher_lows=hl,
            last_swing_high=last_high,
            previous_swing_high=previous_high,
            last_swing_low=last_low,
            previous_swing_low=previous_low,
        )