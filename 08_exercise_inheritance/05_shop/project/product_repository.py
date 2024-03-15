from typing import List
from project.product import Product


class ProductRepository:

    def __init__(self):
        self.products: List[Product] = []

    def add(self, product: Product) -> None:
        self.products.append(product)

    def find(self, product_name: str) -> str or None:
        try:
            searched_product = next(filter(lambda p: p.name == product_name, self.products))
            return searched_product
        except StopIteration:
            pass

    def remove(self, product_name: str)-> None:
        searched_product = self.find(product_name)

        if searched_product:
            self.products.remove(searched_product)

    def __repr__(self):
        result = '\n'.join(f"{p.name}: {p.quantity}" for p in self.products)
        return result

