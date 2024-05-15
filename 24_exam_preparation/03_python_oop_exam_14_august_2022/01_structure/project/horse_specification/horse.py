from abc import ABC, abstractmethod


class Horse(ABC):
    def __init__(self, name: str, speed: int):
        self.name = name
        self.speed = speed
        self.is_taken: bool = False  # Keep in mind that one horse can have only one rider

    @property
    @abstractmethod
    def maximum_speed(self):
        ...

    @property
    @abstractmethod
    def speed_increased_when_trained(self):
        ...

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value) < 4:
            raise ValueError(f"Horse name {value} is less than 4 symbols!")
        self.__name = value

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, value):
        if value > self.maximum_speed:
            raise ValueError("Horse speed is too high!")
        self.__speed = value

    def train(self):
        """"
        When a horse is trained, it increases its speed by a value
        depending on its type. During training, a horse cannot exceed its
        maximum speed (just set its speed to the maximum one without raising
         an error).
         """
        if self.speed + self.speed_increased_when_trained > self.maximum_speed:
            self.speed = self.maximum_speed
        else:
            self.speed += self.speed_increased_when_trained


