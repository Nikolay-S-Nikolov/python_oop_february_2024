from project.food.food import Food
from project.food.main_dish import MainDish


class Salmon(MainDish):
    GRAMS = 22

    def __init__(self, name: str, price: float):
        Food.__init__(self, name, price, Salmon.GRAMS)
