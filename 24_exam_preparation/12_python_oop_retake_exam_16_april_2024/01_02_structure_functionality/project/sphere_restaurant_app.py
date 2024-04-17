from typing import List

from project.clients.base_client import BaseClient
from project.clients.regular_client import RegularClient
from project.clients.vip_client import VIPClient
from project.waiters.base_waiter import BaseWaiter
from project.waiters.full_time_waiter import FullTimeWaiter
from project.waiters.half_time_waiter import HalfTimeWaiter


class SphereRestaurantApp:
    def __init__(self):
        self.waiters: List[BaseWaiter] = []
        self.clients: List[BaseClient] = []

    def hire_waiter(self, waiter_type: str, waiter_name: str, hours_worked: int):
        valid_types = {"FullTimeWaiter": FullTimeWaiter, "HalfTimeWaiter": HalfTimeWaiter}

        try:
            new_waiter = valid_types[waiter_type](waiter_name, hours_worked)

        except KeyError:
            return f"{waiter_type} is not a recognized waiter type."

        if [w for w in self.waiters if w.name == waiter_name]:
            return f"{waiter_name} is already on the staff."

        self.waiters.append(new_waiter)
        return f"{waiter_name} is successfully hired as a {waiter_type}."

    def admit_client(self, client_type: str, client_name: str):
        valid_types = {"RegularClient": RegularClient, "VIPClient": VIPClient}

        try:
            new_client = valid_types[client_type](client_name)

        except KeyError:
            return f"{client_type} is not a recognized client type."

        if [c for c in self.clients if c.name == client_name]:
            return f"{client_name} is already a client."

        self.clients.append(new_client)
        return f"{client_name} is successfully admitted as a {client_type}."

    def process_shifts(self, waiter_name: str):

        try:
            waiter = next(filter(lambda w: w.name == waiter_name, self.waiters))

        except StopIteration:
            return f"No waiter found with the name {waiter_name}."

        return waiter.report_shift()

    def process_client_order(self, client_name: str, order_amount: float):
        try:
            client = next(filter(lambda c: c.name == client_name, self.clients))

        except StopIteration:
            return f"{client_name} is not a registered client."

        points_earned = client.earning_points(order_amount)
        return f"{client_name} earned {points_earned} points from the order."

    def apply_discount_to_client(self, client_name: str):
        try:
            client = next(filter(lambda c: c.name == client_name, self.clients))

        except StopIteration:
            return f"{client_name} cannot get a discount because this client is not admitted!"

        discount_percentage, remaining_points = client.apply_discount()

        return f"{client_name} received a {discount_percentage}% discount. Remaining points {int(remaining_points)}"

    def generate_report(self):
        total_earnings = sum(w.calculate_earnings() for w in self.waiters)
        total_client_points = sum(c.points for c in self.clients)
        result = [
            "$$ Monthly Report $$",
            f"Total Earnings: ${total_earnings:.2f}",
            f"Total Clients Unused Points: {int(total_client_points)}",
            f"Total Clients Count: {len(self.clients)}",
            f"** Waiter Details **"
        ]

        waiters_info = [str(w) for w in sorted(self.waiters, key=lambda w: w.calculate_earnings(),reverse=True)]
        result.extend(waiters_info)

        return "\n".join(result)
