from typing import List
import re

from project.equipment.base_equipment import BaseEquipment
from project.equipment.elbow_pad import ElbowPad
from project.equipment.knee_pad import KneePad
from project.teams.base_team import BaseTeam
from project.teams.indoor_team import IndoorTeam
from project.teams.outdoor_team import OutdoorTeam


class Tournament:
    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.equipment: List[BaseEquipment] = []
        self.teams: List[BaseTeam] = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        # regex = r'[^a-zA-Z\d*]'
        # result = re.findall(regex, value)
        if not value.isalnum():
            raise ValueError("Tournament name should contain letters and digits only!")
        self.__name = value

    def add_equipment(self, equipment_type: str):
        valid_type = {"KneePad": KneePad, "ElbowPad": ElbowPad}

        if equipment_type not in valid_type:
            raise Exception("Invalid equipment type!")

        new_equipment = valid_type[equipment_type]()
        self.equipment.append(new_equipment)
        return f"{equipment_type} was successfully added."

    def add_team(self, team_type: str, team_name: str, country: str, advantage: int):
        valid_types = {"OutdoorTeam": OutdoorTeam, "IndoorTeam": IndoorTeam}

        if team_type not in valid_types:
            raise Exception("Invalid team type!")

        if len(self.teams) >= self.capacity:
            return "Not enough tournament capacity."

        new_team = valid_types[team_type](team_name, country, advantage)
        self.teams.append(new_team)
        return f"{team_type} was successfully added."

    def sell_equipment(self, equipment_type: str, team_name: str):
        equipment = [e for e in self.equipment if type(e).__name__ == equipment_type][-1]
        team = [t for t in self.teams if t.name == team_name][0]

        if equipment.price > team.budget:
            raise Exception("Budget is not enough!")

        self.equipment.remove(equipment)
        team.equipment.append(equipment)
        team.budget -= equipment.price
        return f"Successfully sold {equipment_type} to {team_name}."

    def remove_team(self, team_name: str):
        try:
            team = next(filter(lambda t: t.name == team_name, self.teams))
        except StopIteration:
            raise Exception("No such team!")

        if team.wins:
            raise Exception(f"The team has {team.wins} wins! Removal is impossible!")

        self.teams.remove(team)
        return f"Successfully removed {team_name}."

    def increase_equipment_price(self, equipment_type: str):
        equipments_list = [e for e in self.equipment if type(e).__name__ == equipment_type]
        for equipment in equipments_list:
            equipment.increase_price()
        return f"Successfully changed {len(equipments_list)}pcs of equipment."

    def play(self, team_name1: str, team_name2: str):

        first_team = [t for t in self.teams if t.name == team_name1][0]
        second_team = [t for t in self.teams if t.name == team_name2][0]

        if type(first_team) != type(second_team):
            raise Exception("Game cannot start! Team types mismatch!")

        first_team_points = first_team.advantage + sum(e.protection for e in first_team.equipment)
        second_team_points = second_team.advantage + sum(e.protection for e in second_team.equipment)

        if first_team_points > second_team_points:
            first_team.win()
            return f"The winner is {first_team.name}."

        if second_team_points > first_team_points:
            second_team.win()
            return f"The winner is {second_team.name}."

        return "No winner in this game."

    def get_statistics(self):
        sorted_teams = list(sorted(self.teams, key=lambda t: -t.wins))
        result = [f"Tournament: {self.name}", f"Number of Teams: {len(self.teams)}", "Teams:"]
        result.extend([t.get_statistics() for t in sorted_teams])
        return '\n'.join(result)
