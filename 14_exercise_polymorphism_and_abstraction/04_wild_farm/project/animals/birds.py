from project.animals.animal import Bird
from project.food import Meat, Vegetable, Fruit, Food, Seed


class Owl(Bird):
    WEIGHT_INCREASE_WITH_FOOD_EATEN: float = 0.25
    TYPE_OF_FOOD_EATEN: Food = Meat
    SOUND = "Hoot Hoot"


class Hen(Bird):
    WEIGHT_INCREASE_WITH_FOOD_EATEN: float = 0.35
    TYPE_OF_FOOD_EATEN: Food = (Vegetable, Meat, Fruit, Seed)
    SOUND = "Cluck"
