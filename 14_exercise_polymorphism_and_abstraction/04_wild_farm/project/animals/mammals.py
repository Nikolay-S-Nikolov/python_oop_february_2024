from project.animals.animal import Mammal
from project.food import Vegetable, Meat, Fruit, Food


class Mouse(Mammal):

    @property
    def sound(self):
        return "Squeak"

    @property
    def type_of_food_eaten(self):
        return Vegetable, Fruit

    @property
    def weight_gain(self):
        return 0.10


class Dog(Mammal):

    @property
    def sound(self):
        return "Woof!"

    @property
    def type_of_food_eaten(self):
        return Meat

    @property
    def weight_gain(self):
        return 0.40


class Cat(Mammal):

    @property
    def sound(self):
        return "Meow"

    @property
    def type_of_food_eaten(self):
        return Vegetable, Meat

    @property
    def weight_gain(self):
        return 0.30


class Tiger(Mammal):

    @property
    def sound(self):
        return "ROAR!!!"

    @property
    def type_of_food_eaten(self):
        return Meat

    @property
    def weight_gain(self):
        return 1.00
