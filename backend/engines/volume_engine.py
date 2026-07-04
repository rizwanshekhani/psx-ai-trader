from models.volume_result import VolumeResult


class VolumeEngine:

    def analyze(self, df):

        current_volume = df["Volume"].iloc[-1]
        average_volume = df["Volume"].tail(20).mean()

        relative_volume = current_volume / average_volume

        if relative_volume > 2:
            status = "VERY HIGH"
            score = 10

        elif relative_volume > 1.5:
            status = "HIGH"
            score = 8

        elif relative_volume > 1:
            status = "NORMAL"
            score = 6

        else:
            status = "LOW"
            score = 4

        return VolumeResult(
            current_volume=current_volume,
            average_volume=average_volume,
            relative_volume=relative_volume,
            status=status,
            score=score,
        )