from unittest import TestCase, main

from project.shopping_cart import ShoppingCart


class TestShoppingCart(TestCase):
    def setUp(self) -> None:
        self.cart = ShoppingCart("Lidl", 100)

    def test_constructor_for_proper_init(self):
        self.assertEqual("Lidl", self.cart.shop_name)
        self.assertEqual(100, self.cart.budget)
        self.assertEqual({}, self.cart.products)

    def test_shop_name_setter_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            ShoppingCart("lidl", 100)
        self.assertEqual("Shop must contain only letters and must start with capital letter!", str(ve.exception))
        with self.assertRaises(ValueError) as ve:
            ShoppingCart("Li123", 100)
        self.assertEqual("Shop must contain only letters and must start with capital letter!", str(ve.exception))

    def test_add_to_cart_method_with_higher_than_limit_price_raise_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.cart.add_to_cart('apple', 150)
        self.assertEqual("Product apple cost too much!", str(ve.exception))
        self.assertEqual({}, self.cart.products)

    def test_add_to_cart_method_with_equal_to_limit_price_raise_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.cart.add_to_cart('apple', 100)
        self.assertEqual("Product apple cost too much!", str(ve.exception))

    def test_add_to_cart_method_with_correct_price_raise_return_message(self):
        result = self.cart.add_to_cart('apple', 5)
        self.assertEqual("apple product was successfully added to the cart!", result)
        self.assertEqual({'apple': 5}, self.cart.products)

    def test_remove_from_cart_with_not_existing_product_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.cart.remove_from_cart("test")
        self.assertEqual("No product with name test in the cart!", str(ve.exception))

    def test_remove_from_cart_with_existing_product_return_message(self):
        self.cart.add_to_cart("apple", 7)
        self.cart.add_to_cart("melon", 8)
        result = self.cart.remove_from_cart('apple')
        self.assertEqual("Product apple was successfully removed from the cart!", result)
        self.assertEqual({"melon": 8}, self.cart.products)

    def test__add__method_correct_functionality(self):
        new_cart = ShoppingCart("City", 200)
        new_cart.products = {"Lemon": 3, "Watermelon": 4}
        self.cart.products = {"Apple": 3, "Banana": 4}
        result = self.cart + new_cart
        self.assertEqual("LidlCity", result.shop_name)
        self.assertEqual(300, result.budget)
        self.assertEqual({'Apple': 3, 'Banana': 4, 'Lemon': 3, 'Watermelon': 4}, result.products)

    def test_buy_products_method_with_total_sum_bigger_than_budget_raises_value_error(self):
        new_cart = ShoppingCart('Store', 10)
        new_cart.products = {'Apple': 3, 'Banana': 4, 'Lemon': 3, 'Watermelon': 4}
        expected = f"Not enough money to buy the products! Over budget with {4:.2f}lv!"
        with self.assertRaises(ValueError) as ve:
            new_cart.buy_products()
        self.assertEqual(expected, str(ve.exception))

    def test_buy_products_method_return_correct_message(self):
        new_cart = ShoppingCart('Store', 15)
        new_cart.products = {'Apple': 3, 'Banana': 5, 'Lemon': 3, 'Watermelon': 4}
        result = new_cart.buy_products()
        expected = f'Products were successfully bought! Total cost: {15:.2f}lv.'
        self.assertEqual(expected, result)


if __name__ == "__main__":
    main()
