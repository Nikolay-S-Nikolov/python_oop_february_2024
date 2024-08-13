from abc import ABC, abstractmethod
from typing import List


class BaseStore(ABC):
    def __init__(self, name: str, location: str, capacity: int):
        self.name = name
        self.location = location
        self.capacity = capacity
        self.products: List = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value.strip():
            raise ValueError("Store name cannot be empty!")
        self.__name = value

    @property
    def location(self):
        return self.__location

    @location.setter
    def location(self, value):
        """
        The location must contain exactly 3 characters and should have no white spaces.
        """
        if len(value) != 3 or [True for x in value if x == " "]:
            raise ValueError("Store location must be 3 chars long!")
        self.__location = value

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, value):
        if value < 0:
            raise ValueError("Store capacity must be a positive number or 0!")
        self.__capacity = value

    def get_estimated_profit(self) -> str:
        prices_for_all_products = sum(p.price for p in self.products)
        profit = prices_for_all_products * 0.1

        return f"Estimated future profit for {len(self.products)} products is {profit:.2f}"

    @property
    def store_type(self) -> str:
        return self.__class__.__name__

    @abstractmethod
    def store_stats(self):
        ...

    @property
    @abstractmethod
    def product_type(self):
        ...
