from abc import ABC, abstractmethod
from typing import List

from project.fish.base_fish import BaseFish


class BaseDiver(ABC):

    def __init__(self, name: str):
        self.name = name
        self.oxygen_level = self.initial_oxygen_level
        self.catch: List[BaseFish] = []
        self.competition_points: float = 0
        self.has_health_issue: bool = False

    @property
    @abstractmethod
    def initial_oxygen_level(self):
        ...

    @property
    @abstractmethod
    def consumed_oxygen_percentage(self):
        ...

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value.strip() == '':
            raise ValueError("Diver name cannot be null or empty!")
        self.__name = value

    @property
    def oxygen_level(self):
        return self.__oxygen_level

    @oxygen_level.setter
    def oxygen_level(self, value):
        if value < 0:
            raise ValueError("Cannot create diver with negative oxygen level!")
        self.__oxygen_level = value

    @property
    def competition_points(self):
        return self.__competition_points

    @competition_points.setter
    def competition_points(self, value):
        self.__competition_points = round(value, 1)

    def miss(self, time_to_catch: int):
        consumed_oxygen = round(self.consumed_oxygen_percentage * time_to_catch)
        if self.oxygen_level - consumed_oxygen < 0:
            self.oxygen_level = 0
        else:
            self.oxygen_level -= consumed_oxygen

    def renew_oxy(self):
        self.oxygen_level = self.initial_oxygen_level

    def hit(self, fish: BaseFish):
        if self.oxygen_level < fish.time_to_catch:
            self.oxygen_level = 0
        else:
            self.oxygen_level -= fish.time_to_catch
            self.catch.append(fish)
            self.competition_points += round(fish.points, 1)  # diver's competition_points increase by the value
            # of the points property of the caught fish, rounded to one decimal place

    def update_health_status(self):
        self.has_health_issue = not self.has_health_issue

    def __str__(self):
        return f"{self.__class__.__name__}: [Name: {self.name}, Oxygen level left: {self.oxygen_level}, " \
               f"Fish caught: {len(self.catch)}, Points earned: {self.competition_points:.1f}]"
