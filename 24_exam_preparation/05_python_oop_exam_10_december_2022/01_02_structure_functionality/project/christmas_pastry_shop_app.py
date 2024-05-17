from typing import List

from project.booths.booth import Booth
from project.booths.open_booth import OpenBooth
from project.booths.private_booth import PrivateBooth
from project.delicacies.gingerbread import Gingerbread
from project.delicacies.stolen import Stolen


class ChristmasPastryShopApp:
    def __init__(self):
        self.booths: List[OpenBooth or PrivateBooth] = []
        self.delicacies: List[Gingerbread or Stolen] = []
        self.income: float = 0.0

    def add_delicacy(self, type_delicacy: str, name: str, price: float):
        valid_types = {"Gingerbread": Gingerbread, "Stolen": Stolen}
        if name in [n.name for n in self.delicacies]:
            raise Exception(f"{name} already exists!")
        if type_delicacy not in valid_types:
            raise Exception(f"{type_delicacy} is not on our delicacy menu!")
        new_delicacy = valid_types[type_delicacy](name, price)
        self.delicacies.append(new_delicacy)
        return f"Added delicacy {name} - {type_delicacy} to the pastry shop."

    def add_booth(self, type_booth: str, booth_number: int, capacity: int):
        valid_types = {"Open Booth": OpenBooth, "Private Booth": PrivateBooth}
        if booth_number in [b.booth_number for b in self.booths]:
            raise Exception(f"Booth number {booth_number} already exists!")
        if type_booth not in valid_types:
            raise Exception(f"{type_booth} is not a valid booth!")
        new_booth = valid_types[type_booth](booth_number, capacity)
        self.booths.append(new_booth)
        return f"Added booth number {booth_number} in the pastry shop."

    def reserve_booth(self, number_of_people: int):
        try:
            first_free_booth = next(filter(
                lambda b: (b.capacity >= number_of_people and not b.is_reserved), self.booths
            ))
        except StopIteration:
            raise Exception(f"No available booth for {number_of_people} people!")
        first_free_booth.reserve(number_of_people)
        return f"Booth {first_free_booth.booth_number} has been reserved for {number_of_people} people."

    def order_delicacy(self, booth_number: int, delicacy_name: str):
        try:
            booth = next(filter(lambda b: b.booth_number == booth_number, self.booths))
        except StopIteration:
            raise Exception(f"Could not find booth {booth_number}!")

        try:
            delicacy = next(filter(lambda d: d.name == delicacy_name, self.delicacies))
        except StopIteration:
            raise Exception(f"No {delicacy_name} in the pastry shop!")
        # order the delicacy for that booth
        booth.delicacy_orders.append(delicacy)
        return f"Booth {booth_number} ordered {delicacy_name}."

    def leave_booth(self, booth_number: int):
        booth = [b for b in self.booths if b.booth_number == booth_number][0]
        # Calculates the bill for that booth taking the price for reservation
        # and all the price of all orders. The bill is added to the pastry shop's total income.
        bill = booth.price_for_reservation + sum(d.price for d in booth.delicacy_orders)
        self.income += bill
        booth.delicacy_orders = []
        booth.is_reserved = False
        booth.price_for_reservation = 0.0
        return f"Booth {booth_number}:\n" \
               f"Bill: {bill:.2f}lv."

    def get_income(self):
        return f"Income: {self.income:.2f}lv."
