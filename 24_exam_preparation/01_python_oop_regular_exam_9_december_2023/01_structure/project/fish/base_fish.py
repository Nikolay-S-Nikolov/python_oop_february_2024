from abc import ABC, abstractmethod


class BaseFish(ABC):
    def __init__(self, name: str, points: float):
        self.name = name
        self.points = points

    @property
    @abstractmethod
    def time_to_catch(self):
        ...

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value.strip() == '':
            raise ValueError("Fish name should be determined!")
        self.__name = value

    @property
    def points(self):
        return self.__points

    @points.setter
    def points(self, value):
        if not (1 <= value <= 10):
            raise ValueError("Points should be a value ranging from 1 to 10!")
        self.__points = value

    def fish_details(self) -> str:
        return f"{self.__class__.__name__}: {self.name} " \
               f"[Points: {self.points}, Time to Catch: {self.time_to_catch} seconds]"
