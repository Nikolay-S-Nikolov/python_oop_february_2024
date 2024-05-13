from typing import List

from project.divers.base_diver import BaseDiver
from project.divers.free_diver import FreeDiver
from project.divers.scuba_diver import ScubaDiver
from project.fish.base_fish import BaseFish
from project.fish.deep_sea_fish import DeepSeaFish
from project.fish.predatory_fish import PredatoryFish


class NauticalCatchChallengeApp:
    def __init__(self):
        self.divers: List[BaseDiver] = []
        self.fish_list: List[BaseFish] = []

    def dive_into_competition(self, diver_type: str, diver_name: str):
        valid_types = {'FreeDiver': FreeDiver, 'ScubaDiver': ScubaDiver}
        if diver_type not in valid_types.keys():
            return f"{diver_type} is not allowed in our competition."
        try:
            next(filter(lambda d: d.name == diver_name, self.divers))
            return f"{diver_name} is already a participant."
        except StopIteration:
            pass
        new_diver = valid_types[diver_type](diver_name)
        self.divers.append(new_diver)
        return f"{diver_name} is successfully registered for the competition as a {diver_type}."

    def swim_into_competition(self, fish_type: str, fish_name: str, points: float):
        valid_types = {"PredatoryFish": PredatoryFish, "DeepSeaFish": DeepSeaFish}
        if fish_type not in valid_types.keys():
            return f"{fish_type} is forbidden for chasing in our competition."

        try:
            next(filter(lambda f: f.name == fish_name, self.fish_list))
            return f"{fish_name} is already permitted."
        except StopIteration:
            pass
        new_fish = valid_types[fish_type](fish_name, points)
        self.fish_list.append(new_fish)
        return f"{fish_name} is allowed for chasing as a {fish_type}."

    def chase_fish(self, diver_name: str, fish_name: str, is_lucky: bool):

        try:
            diver = next(filter(lambda d: d.name == diver_name, self.divers))
        except StopIteration:
            return f"{diver_name} is not registered for the competition."

        try:
            fish = next(filter(lambda f: f.name == fish_name, self.fish_list))
        except StopIteration:
            return f"The {fish_name} is not allowed to be caught in this competition."

        if diver.has_health_issue:
            return f"{diver_name} will not be allowed to dive, due to health issues."

        if diver.oxygen_level < fish.time_to_catch:
            diver.miss(fish.time_to_catch)
            if diver.oxygen_level == 0:
                diver.update_health_status()
            return f"{diver_name} missed a good {fish_name}."
        if diver.oxygen_level == fish.time_to_catch:
            if is_lucky:
                diver.hit(fish)
                if diver.oxygen_level == 0:
                    diver.update_health_status()
                return f"{diver_name} hits a {fish.points}pt. {fish_name}."
            else:
                diver.miss(fish.time_to_catch)
                if diver.oxygen_level == 0:
                    diver.update_health_status()
                return f"{diver_name} missed a good {fish_name}."
        if diver.oxygen_level > fish.time_to_catch:
            diver.hit(fish)
            return f"{diver_name} hits a {fish.points}pt. {fish_name}."

    def health_recovery(self):
        recovered_divers = 0
        for diver in self.divers:
            if diver.has_health_issue:
                diver.update_health_status()
                diver.oxygen_level = diver.initial_oxygen_level
                recovered_divers += 1
        # if recovered_divers:  # Not exactly specified what if recovered_divers == 0
        return f"Divers recovered: {recovered_divers}"

    def diver_catch_report(self, diver_name: str):
        diver = next(filter(lambda d: d.name == diver_name, self.divers))
        fish_details = ''
        for fish in diver.catch:
            fish_details += '\n' + fish.fish_details()
        return f"**{diver_name} Catch Report**{fish_details}"

    def competition_statistics(self):
        result = "**Nautical Catch Challenge Statistics**"
        drivers_dict = {}
        for k in self.divers:
            if not k.has_health_issue:
                drivers_dict[k] = [-k.competition_points, -len(k.catch), k.name]

        sorted_divers = sorted(drivers_dict.items(), key=lambda x: (x[1][0], x[1][1], x[1][2]))
        for diver, info in sorted_divers:
            result += '\n' + str(diver)
        return result
