from abc import ABC, abstractmethod


class FormulaTeam(ABC):
    def __init__(self, budget: int):
        self.budget = budget

    @property
    def budget(self):
        return self.__budget

    @budget.setter
    def budget(self, value):
        if value < 1000000:
            raise ValueError("F1 is an expensive sport, find more sponsors!")
        self.__budget = value

    def calculate_revenue_after_race(self, race_pos: int):
        revenue = 0
        if race_pos in self.sponsor_money_per_position:
            revenue = self.sponsor_money_per_position[race_pos]
        revenue -= self.expenses_per_race
        self.budget += revenue
        return f"The revenue after the race is {revenue}$. Current budget {self.budget}$"

    @property
    @abstractmethod
    def sponsor_money_per_position(self):
        ...

    @property
    @abstractmethod
    def expenses_per_race(self):
        ...
