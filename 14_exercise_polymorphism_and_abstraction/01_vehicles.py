from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, fuel_quantity: int, fuel_consumption: int):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    @abstractmethod
    def drive(self, distance: float) -> None:
        pass

    @abstractmethod
    def refuel(self, fuel: float) -> None:
        pass


class Car(Vehicle):
    ADDITIONAL_SUMMER_CONSUMPTION = 0.9

    def drive(self, distance: float) -> None:
        if (self.fuel_consumption + self.ADDITIONAL_SUMMER_CONSUMPTION) * distance < self.fuel_quantity:
            self.fuel_quantity -= (self.fuel_consumption + self.ADDITIONAL_SUMMER_CONSUMPTION) * distance

    def refuel(self, fuel: float):
        self.fuel_quantity += fuel


class Truck(Vehicle):
    ADDITIONAL_SUMMER_CONSUMPTION = 1.6
    TRUCK_FUEL_TANK_MAX_CAP = 0.95

    def drive(self, distance: float) -> None:
        if (self.fuel_consumption + self.ADDITIONAL_SUMMER_CONSUMPTION) * distance < self.fuel_quantity:
            self.fuel_quantity -= (self.fuel_consumption + self.ADDITIONAL_SUMMER_CONSUMPTION) * distance

    def refuel(self, fuel: float) -> None:
        self.fuel_quantity += fuel * self.TRUCK_FUEL_TANK_MAX_CAP


truck = Truck(100, 15)
truck.drive(5)
print(truck.fuel_quantity)
truck.refuel(50)
print(truck.fuel_quantity)
