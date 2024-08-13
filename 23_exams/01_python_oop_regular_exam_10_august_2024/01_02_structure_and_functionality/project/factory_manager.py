from typing import List

from project.products.chair import Chair
from project.products.hobby_horse import HobbyHorse
from project.stores.furniture_store import FurnitureStore
from project.stores.toy_store import ToyStore


class FactoryManager:
    def __init__(self, name: str):
        self.name = name
        self.income: float = 0.0
        self.products: List[Chair or HobbyHorse] = []
        self.stores: List[FurnitureStore or ToyStore] = []

    def produce_item(self, product_type: str, model: str, price: float) -> str:
        valid_types = {"Chair": Chair, "HobbyHorse": HobbyHorse}

        try:
            product = valid_types[product_type](model, price)
        except KeyError:
            raise Exception("Invalid product type!")

        self.products.append(product)
        return f"A product of sub-type {product.product_type} was produced."

    def register_new_store(self, store_type: str, name: str, location: str) -> str:

        valid_types = {'FurnitureStore': FurnitureStore, 'ToyStore': ToyStore}

        try:
            store = valid_types[store_type](name, location)
        except KeyError:
            raise Exception(f"{store_type} is an invalid type of store!")

        self.stores.append(store)

        return f"A new {store_type} was successfully registered."

    def sell_products_to_store(self, store: FurnitureStore or ToyStore, *products: Chair or HobbyHorse) -> str:

        if store.capacity < len(products):
            return f"Store {store.name} has no capacity for this purchase."

        store_type = store.product_type
        filtered_products = [p for p in products if p.product_type == store_type]

        if not filtered_products:
            return "Products do not match in type. Nothing sold."

        store.products.extend(filtered_products)
        store.capacity -= len(filtered_products)

        for p in filtered_products:
            self.products.remove(p)
            self.income += p.price

        return f"Store {store.name} successfully purchased {len(filtered_products)} items."

    def unregister_store(self, store_name: str) -> str:

        try:
            store = next(filter(lambda s: s.name == store_name, self.stores))

        except StopIteration:
            raise Exception("No such store!")

        if store.products:
            return "The store is still having products in stock! Unregistering is inadvisable."

        self.stores.remove(store)
        return f"Successfully unregistered store {store_name}, location: {store.location}."

    def discount_products(self, product_model: str) -> str:

        filtered_products = [p.discount() for p in self.products if p.model == product_model]

        return f"Discount applied to {len(filtered_products)} products with model: {product_model}"

    def request_store_stats(self, store_name: str) -> str:

        try:
            store = next(filter(lambda s: s.name == store_name, self.stores))
        except StopIteration:
            return "There is no store registered under this name!"

        return store.store_stats()

    def statistics(self) -> str:
        info = [
            f"Factory: {self.name}",
            f"Income: {self.income:.2f}",
            "***Products Statistics***",
            f"Unsold Products: {len(self.products)}. Total net price: {sum(p.price for p in self.products):.2f}",
        ]

        products_dict = {}
        for product in sorted(self.products, key=lambda p: p.model):
            if product.model not in products_dict:
                products_dict[product.model] = 0
            products_dict[product.model] += 1

        info.extend([f"{model}: {count}" for model, count in products_dict.items()])

        info.append(f"***Partner Stores: {len(self.stores)}***")

        info.extend([s.name for s in sorted(self.stores, key=lambda s: s.name)])

        return '\n'.join(info)
