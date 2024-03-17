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

    def test_add_to_cart_method_correct_price_raise_return_message(self):
        result = self.cart.add_to_cart('apple', 5)
        self.assertEqual("apple product was successfully added to the cart!", result)
        self.assertEqual({'apple': 5}, self.cart.products)




if __name__ == "__main__":
    main()
