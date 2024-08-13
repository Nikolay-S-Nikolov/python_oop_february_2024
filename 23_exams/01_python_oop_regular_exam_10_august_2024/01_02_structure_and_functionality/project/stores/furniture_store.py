from project.stores.base_store import BaseStore


class FurnitureStore(BaseStore):
    INITIAL_CAPACITY = 50

    def __init__(self, name: str, location: str):
        super().__init__(name, location, capacity=self.INITIAL_CAPACITY)

    @property
    def product_type(self):
        return "Furniture"

    def store_stats(self) -> str:

        information = [
            f"Store: {self.name}, location: {self.location}, available capacity: {self.capacity}",
            self.get_estimated_profit(),
            "**Furniture for sale:"
        ]

        products_dict = {}
        for product in sorted(self.products, key=lambda p: p.model):
            if product.model not in products_dict:
                products_dict[product.model] = []
            products_dict[product.model].append(product.price)

        sale_info = []
        for model, prices in products_dict.items():
            avg_price_per_model = sum(p for p in prices) / len(prices)
            sale_info.append(f"{model}: {len(prices)}pcs, average price: {avg_price_per_model:.2f}")

        information.extend(sale_info)
        return '\n'.join(information)
