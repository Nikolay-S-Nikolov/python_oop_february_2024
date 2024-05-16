import copy
from typing import List

from project.client import Client
from project.meals.dessert import Dessert
from project.meals.main_dish import MainDish
from project.meals.meal import Meal
from project.meals.starter import Starter


class FoodOrdersApp:
    def __init__(self):
        self.menu: List[Meal] = []
        self.clients_list: List[Client] = []
        self.__receipt_id = 0

    def register_client(self, client_phone_number: str):
        if client_phone_number in [c.phone_number for c in self.clients_list]:
            raise Exception("The client has already been registered!")
        new_client = Client(client_phone_number)
        self.clients_list.append(new_client)
        return f"Client {client_phone_number} registered successfully."

    def add_meals_to_menu(self, *meals: Meal):
        valid_meals = [Starter, MainDish, Dessert]
        for meal in meals:
            if type(meal) in valid_meals:
                self.menu.append(meal)

    def show_menu(self):
        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")
        menu_details = [m.details() for m in self.menu]
        return '\n'.join(menu_details)

    def add_meals_to_shopping_cart(self, client_phone_number: str, **meal_names_and_quantities):
        """
        If the exception is raised, the client could NOT make the order
        at all (none of the meals should be added to the client's shopping cart, and
        the bill should not be increased)
        """
        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")

        if client_phone_number not in [c.phone_number for c in self.clients_list]:
            self.register_client(client_phone_number)
        order_dict = {}
        for meal_name, quantities in meal_names_and_quantities.items():
            try:
                meal = next(filter(lambda m: m.name == meal_name, self.menu))
            except StopIteration:
                raise Exception(f"{meal_name} is not on the menu!")
            if quantities > meal.quantity:
                raise Exception(f"Not enough quantity of {meal.__class__.__name__}: {meal_name}!")
            # it is not required to check if meal type is valid
            order_dict[meal] = [meal.price, quantities]
        client = [c for c in self.clients_list if c.phone_number == client_phone_number][0]
        for ordered_meal, info in order_dict.items():
            price, qty = info
            ordered_meal.quantity -= qty
            client_meal = copy.deepcopy(ordered_meal)
            client_meal.quantity = qty
            client.shopping_cart.append(client_meal)
            client.bill += price * qty

        return f"Client {client_phone_number} successfully ordered " \
               f"{', '.join(m.name for m in client.shopping_cart)} for {client.bill:.2f}lv."

    def cancel_order(self, client_phone_number: str):
        client = [c for c in self.clients_list if c.phone_number == client_phone_number][0]
        if not client.shopping_cart:
            raise Exception("There are no ordered meals!")

        for meal in client.shopping_cart:
            meal_in_menu = [m for m in self.menu if m.name == meal.name][0]
            meal_in_menu.quantity += meal.quantity

        client.shopping_cart = []
        client.bill = 0.0
        return f"Client {client_phone_number} successfully canceled his order."

    def finish_order(self, client_phone_number: str):
        client = [c for c in self.clients_list if c.phone_number == client_phone_number][0]
        if not client.shopping_cart:
            raise Exception("There are no ordered meals!")
        client.shopping_cart = []
        total_paid_money = client.bill
        client.bill = 0.0
        self.__receipt_id += 1
        return f"Receipt #{self.__receipt_id} with total amount of {total_paid_money:.2f} " \
               f"was successfully paid for {client_phone_number}."

    def __str__(self):
        return f"Food Orders App has {len(self.menu)} meals on the menu and {len(self.clients_list)} clients."
