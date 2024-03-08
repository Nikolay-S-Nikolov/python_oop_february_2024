from project.animals.animal import Mammal
from project.food import Vegetable, Meat, Fruit, Food


class Mouse(Mammal):
    WEIGHT_INCREASE_WITH_FOOD_EATEN: float = 0.10
    TYPE_OF_FOOD_EATEN = (Vegetable, Fruit)
    SOUND = "Squeak"


class Dog(Mammal):
    WEIGHT_INCREASE_WITH_FOOD_EATEN: float = 0.40
    TYPE_OF_FOOD_EATEN = Meat
    SOUND = "Woof!"


class Cat(Mammal):
    WEIGHT_INCREASE_WITH_FOOD_EATEN: float = 0.30
    TYPE_OF_FOOD_EATEN: Food = (Vegetable, Meat)
    SOUND = "Meow"


class Tiger(Mammal):
    WEIGHT_INCREASE_WITH_FOOD_EATEN = 1.00
    TYPE_OF_FOOD_EATEN: Food = Meat
    SOUND = "ROAR!!!"
