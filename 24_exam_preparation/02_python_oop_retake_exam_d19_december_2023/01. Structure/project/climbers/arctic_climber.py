from project.climbers.base_climber import BaseClimber
from project.peaks.arctic_peak import ArcticPeak
from project.peaks.summit_peak import SummitPeak


class ArcticClimber(BaseClimber):
    INITIAL_STRENGTH = 200
    MINIMUM_STRENGTH = 100

    def __init__(self, name):
        super().__init__(name, strength=self.INITIAL_STRENGTH)

    def can_climb(self):
        return self.strength >= self.MINIMUM_STRENGTH

    def climb(self, peak: ArcticPeak or SummitPeak):
        self.strength -= 40 if peak.difficulty_level == "Extreme" else 30
        self.conquered_peaks.append(peak.name)


