from project.climbers.base_climber import BaseClimber
from project.peaks.arctic_peak import ArcticPeak
from project.peaks.summit_peak import SummitPeak


class SummitClimber(BaseClimber):
    INITIAL_STRENGTH = 150
    MINIMUM_STRENGTH = 75

    def __init__(self, name):
        super().__init__(name, strength=self.INITIAL_STRENGTH)

    def can_climb(self):
        return self.strength >= self.MINIMUM_STRENGTH

    def climb(self, peak: ArcticPeak or SummitPeak):
        if peak.difficulty_level == "Advanced":
            self.strength -= 39
        else:
            self.strength -= 75
        self.conquered_peaks.append(peak.name)


