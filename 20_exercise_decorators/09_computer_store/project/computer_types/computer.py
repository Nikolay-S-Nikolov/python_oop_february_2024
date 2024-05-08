from abc import ABC, abstractmethod
from math import log2, ceil, floor


class Computer(ABC):
    def __init__(self, manufacturer: str, model: str):
        self.manufacturer = manufacturer  # manufacturer's name
        self.model = model  # computer's model name
        self.processor: str or None = None  # computer's processor
        self.ram: int or None = None  # computer's RAM memory
        self.price: int = 0

    @property
    @abstractmethod
    def type(self):
        ...

    @property
    @abstractmethod
    def available_processors(self):
        ...

    @property
    @abstractmethod
    def max_ram(self):
        ...

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        if value.strip() == '':
            raise ValueError("Model name cannot be empty.")
        self.__model = value

    @property
    def manufacturer(self):
        return self.__manufacturer

    @manufacturer.setter
    def manufacturer(self, value):
        if value.strip() == '':
            raise ValueError("Manufacturer name cannot be empty.")
        self.__manufacturer = value

    @staticmethod
    def power_of_two(ram: int):
        result = log2(ram)
        return result.is_integer()

    def configure_computer(self, processor: str, ram: int):
        if processor not in self.available_processors:
            raise ValueError(f"{processor} is not compatible with "
                             f"{self.type} {self.manufacturer} {self.model}!")
        if not self.power_of_two(ram) or ram > self.max_ram:
            raise ValueError(f"{ram}GB RAM is not compatible with {self.type} {self.manufacturer} {self.model}!")

        self.set_parts(processor, ram)
        return f"Created {self} for {self.price}$."

    def set_parts(self, processor: str, ram: int):
        self.processor = processor
        self.ram = ram
        self.price += self.available_processors[processor]
        self.price += int(log2(ram)) * 100

    def __repr__(self):
        return f"{self.manufacturer} {self.model} with {self.processor} and {self.ram}GB RAM"
