from project.animals.animal import Bird
from project.food import Meat, Vegetable, Fruit, Food, Seed


class Owl(Bird):

    @property
    def sound(self):
        return "Hoot Hoot"

    @property
    def type_of_food_eaten(self):
        return Meat

    @property
    def weight_gain(self):
        return 0.25


class Hen(Bird):

    @property
    def sound(self):
        return "Cluck"

    @property
    def type_of_food_eaten(self):
        return Vegetable, Meat, Fruit, Seed

    @property
    def weight_gain(self):
        return 0.35
