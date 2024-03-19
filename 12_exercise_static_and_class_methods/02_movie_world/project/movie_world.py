from typing import List

from project.customer import Customer
from project.dvd import DVD


class MovieWorld:
    def __init__(self, name: str):
        self.name = name
        self.customers: List[Customer] = []
        self.dvds: List[DVD] = []

    @staticmethod
    def dvd_capacity() -> int:
        """
        DVD capacity of a movie world
        """
        return 15

    @staticmethod
    def customer_capacity() -> int:
        """
        customer capacity of a movie world
        """
        return 10

    def add_customer(self, customer: Customer):
        if len(self.customers) < self.customer_capacity():
            self.customers.append(customer)

    def add_dvd(self, dvd: DVD):
        if len(self.dvds) < self.dvd_capacity():
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id: int, dvd_id: int):
        current_customer = next(filter(lambda c: c.id == customer_id, self.customers))
        current_dvd = next(filter(lambda d: d.id == dvd_id, self.dvds))
        if current_dvd in current_customer.rented_dvds:
            return f"{current_customer.name} has already rented {current_dvd.name}"

        if current_dvd.is_rented:
            return "DVD is already rented"

        if current_customer.age < current_dvd.age_restriction:
            return f"{current_customer.name} should be at least {current_dvd.age_restriction} to rent this movie"

        current_dvd.is_rented = True
        current_customer.rented_dvds.append(current_dvd)
        return f"{current_customer.name} has successfully rented {current_dvd.name}"

    def return_dvd(self, customer_id: int, dvd_id: int):
        current_customer = next(filter(lambda c: c.id == customer_id, self.customers))
        current_dvd = next(filter(lambda d: d.id == dvd_id, self.dvds))

        if current_dvd not in current_customer.rented_dvds:
            return f"{current_customer.name} does not have that DVD"

        current_customer.rented_dvds.remove(current_dvd)
        current_dvd.is_rented = False
        return f"{current_customer.name} has successfully returned {current_dvd.name}"

    def __repr__(self):
        # result = '\n'.join(str(c) for c in self.customers)
        # result += '\n'
        # result += '\n'.join(str(d) for d in self.dvds)
        return '\n'.join([
            *[str(c) for c in self.customers],
            *[str(d) for d in self.dvds]
        ])

