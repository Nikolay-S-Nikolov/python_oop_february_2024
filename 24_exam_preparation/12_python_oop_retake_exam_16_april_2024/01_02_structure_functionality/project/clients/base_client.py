from abc import ABC, abstractmethod


class BaseClient(ABC):
    MEMBERSHIP_TYPE = ["Regular", "VIP"]

    def __init__(self, name: str, membership_type: str):
        self.name = name
        self.membership_type = membership_type
        self.points: int = 0  # Represents the total points earned by a client, based on the spending amount.
        # Set the initial value of the property to zero (0).

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        if not value.strip():
            raise ValueError("Client name should be determined!")

        self.__name = value

    @property
    def membership_type(self):
        return self.__membership_type

    @membership_type.setter
    def membership_type(self, value: str):
        if value not in self.MEMBERSHIP_TYPE:
            raise ValueError("Invalid membership type. Allowed types: Regular, VIP.")
        self.__membership_type = value

    @abstractmethod
    def earning_points(self, order_amount: float):
        ...

    def apply_discount(self):
        if self.points >= 100:
            discount_percentage = 10
            self.points -= 100
            result = (discount_percentage, int(self.points))
            return result

        if self.points >= 50:
            discount_percentage = 5
            self.points -= 50
            result = (discount_percentage, int(self.points))
            return result

        discount_percentage = 0
        result = (discount_percentage, int(self.points))
        return result
