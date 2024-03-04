from project.beverage.beverage import Beverage
from project.beverage.hot_beverage import HotBeverage
from project.product import Product


class Coffee(HotBeverage):
    MILLILITERS = 50
    PRICE = 3.50

    def __init__(self, name: str, caffeine: float):
        Beverage.__init__(self, name, Coffee.PRICE, Coffee.MILLILITERS)
        self.__caffeine = caffeine

    @property
    def caffeine(self):
        return self.__caffeine
