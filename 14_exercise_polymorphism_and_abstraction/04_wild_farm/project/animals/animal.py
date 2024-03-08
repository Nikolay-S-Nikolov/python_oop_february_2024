from abc import ABC, abstractmethod


class Animal(ABC):

    def __init__(self, name: str, weight: float):
        self.name = name
        self.weight = weight
        self.food_eaten = 0

    @property
    @abstractmethod
    def weight_gain(self):
        ...

    @property
    @abstractmethod
    def sound(self):
        ...

    @property
    @abstractmethod
    def type_of_food_eaten(self):
        ...

    def make_sound(self):
        return self.sound

    def feed(self, food):
        if not isinstance(food, self.type_of_food_eaten):
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.weight += self.weight_gain * food.quantity
        self.food_eaten += food.quantity

    @abstractmethod
    def __repr__(self):
        ...


class Bird(Animal, ABC):
    def __init__(self, name: str, weight: float, wing_size: float):
        super().__init__(name, weight)
        self.wing_size = wing_size

    def __repr__(self):
        return f"{self.__class__.__name__} [{self.name}, {self.wing_size}, {self.weight}, {self.food_eaten}]"


class Mammal(Animal, ABC):
    def __init__(self, name: str, weight: float, living_region: str):
        super().__init__(name, weight)
        self.living_region = living_region

    def __repr__(self):
        return f"{self.__class__.__name__} [{self.name}, {self.weight}, {self.living_region}, {self.food_eaten}]"
