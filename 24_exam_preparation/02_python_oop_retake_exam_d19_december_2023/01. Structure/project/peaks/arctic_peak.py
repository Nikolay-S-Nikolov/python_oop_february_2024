from project.peaks.base_peak import BasePeak


class ArcticPeak(BasePeak):
    RECOMMENDED_GEAR = ["Ice axe", "Crampons", "Insulated clothing", "Helmet"]

    def get_recommended_gear(self):
        return self.RECOMMENDED_GEAR

    def calculate_difficulty_level(self) -> str:
        if self.elevation > 3000:
            return "Extreme"
        if 2_000 <= self.elevation <= 3_000:
            return "Advanced"



