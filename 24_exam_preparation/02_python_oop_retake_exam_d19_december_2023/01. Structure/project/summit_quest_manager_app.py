from typing import List

from project.climbers.arctic_climber import ArcticClimber
from project.climbers.summit_climber import SummitClimber
from project.peaks.arctic_peak import ArcticPeak
from project.peaks.summit_peak import SummitPeak


class SummitQuestManagerApp:
    VALID_CLIMBER_TYPE = {"ArcticClimber": ArcticClimber, "SummitClimber": SummitClimber}
    VALID_PEAK_TYPE = {"ArcticPeak": ArcticPeak, "SummitPeak": SummitPeak}

    def __init__(self):
        self.climbers: List[ArcticClimber or SummitClimber] = []
        self.peaks: List[ArcticPeak or SummitPeak] = []

    def register_climber(self, climber_type: str, climber_name: str) -> str:

        if climber_type not in self.VALID_CLIMBER_TYPE.keys():
            return f"{climber_type} doesn't exist in our register."

        if climber_name in [c.name for c in self.climbers]:
            return f"{climber_name} has been already registered."

        new_climber = self.VALID_CLIMBER_TYPE[climber_type](climber_name)
        self.climbers.append(new_climber)
        return f"{climber_name} is successfully registered as a {climber_type}."

    def peak_wish_list(self, peak_type: str, peak_name: str, peak_elevation: int):

        if peak_type not in self.VALID_PEAK_TYPE.keys():
            return f"{peak_type} is an unknown type of peak."

        # if peak_name not in [p.name for p in self.peaks]: # check if peak is already in the list was not required
        new_peak = self.VALID_PEAK_TYPE[peak_type](peak_name, peak_elevation)
        self.peaks.append(new_peak)
        return f"{peak_name} is successfully added to the wish list as a {peak_type}."

    def check_gear(self, climber_name: str, peak_name: str, gear: List[str]):
        """
        The method is responsible for verifying if every climber has the required gear for each peak
        :param climber_name: str
        :param peak_name: str
        :param gear: List[str]
        :return: str
        """
        peak = [p for p in self.peaks if p.name == peak_name][0]
        climber = [c for c in self.climbers if c.name == climber_name][0]
        missing_gear = [g for g in peak.get_recommended_gear() if g not in gear]

        if not missing_gear:
            return f"{climber_name} is prepared to climb {peak_name}."

        climber.is_prepared = False
        return f"{climber_name} is not prepared to climb {peak_name}. " \
               f"Missing gear: {', '.join(sorted(missing_gear))}."

    def perform_climbing(self, climber_name: str, peak_name: str):

        try:
            climber = next(filter(lambda c: c.name == climber_name, self.climbers))
        except StopIteration:
            return f"Climber {climber_name} is not registered yet."

        try:
            peak = next(filter(lambda p: p.name == peak_name, self.peaks))
        except StopIteration:
            return f"Peak {peak_name} is not part of the wish list."

        if climber.can_climb() and climber.is_prepared:
            climber.climb(peak)
            # if climber.climb(peak) need to be updated
            return f"{climber_name} conquered {peak_name} whose difficulty level" \
                   f" is {peak.calculate_difficulty_level()}."

        if not climber.is_prepared:
            return f"{climber_name} will need to be better prepared next time."
        # TO DO check if method climber.rest() should be inserted
        climber.rest()
        return f"{climber_name} needs more strength to climb {peak_name} and is therefore taking some rest."

    def get_statistics(self):
        climbers_with_conquered_peaks = [c for c in self.climbers if c.conquered_peaks]
        climbers_dict = {}
        how_many_peaks_were_conquered = []

        for c in climbers_with_conquered_peaks:
            climbers_dict[c] = [sorted(c.conquered_peaks), c.name]
            how_many_peaks_were_conquered.extend(c.conquered_peaks)

        sorted_dict = dict(sorted(climbers_dict.items(), key=lambda x: (-len(x[1][0]), x[1][1])))

        climbers = '\n'.join([str(c) for c in sorted_dict.keys()])
        return f"Total climbed peaks: {len(set(how_many_peaks_were_conquered))}\n" \
               f"**Climber's statistics:**\n{climbers}"

    def climber_is_in_the_list(self, name: str) -> bool:
        return True if name in [c.name for c in self.climbers] else False
