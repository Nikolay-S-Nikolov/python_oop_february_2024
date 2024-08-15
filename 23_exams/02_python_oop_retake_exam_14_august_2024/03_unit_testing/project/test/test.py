from project.furniture import Furniture
from unittest import TestCase, main


class TestFurniture(TestCase):
    def setUp(self) -> None:
        self.c = Furniture('Chair', 22.7, (20, 20, 20), True)
        name = 50 * " " + 'Table' + 50 * " "
        self.t = Furniture(name, 0, (60, 80, 120), True, 25.7)

    def test_correct_init(self):
        self.assertEqual("Chair", self.c.model)
        self.assertEqual(22.7, self.c.price)
        self.assertEqual((20, 20, 20), self.c.dimensions)
        self.assertEqual(True, self.c.in_stock)
        self.assertEqual(None, self.c.weight)

        self.assertEqual(50 * " " + 'Table' + 50 * " ", self.t.model)
        self.assertEqual(0, self.t.price)
        self.assertEqual(25.7, self.t.weight)

    def test_correct_setter_model_raise_value_error(self):
        expected = "Model must be a non-empty string with a maximum length of 50 characters."
        with self.assertRaises(ValueError) as ve:
            self.c.model = ''
        self.assertEqual(expected, str(ve.exception))

        with self.assertRaises(ValueError) as ve:
            self.c.model = '    '
        self.assertEqual(expected, str(ve.exception))

        with self.assertRaises(ValueError) as ve:
            self.c.model = 51 * "A"
        self.assertEqual(expected, str(ve.exception))

    def test_correct_setter_price_raise_value_error(self):
        expected = "Price must be a non-negative number."
        with self.assertRaises(ValueError) as ve:
            self.c.price = -1
        self.assertEqual(expected, str(ve.exception))

    def test_correct_setter_dimension_raise_value_error(self):
        expected = "Dimensions tuple must contain 3 integers."
        with self.assertRaises(ValueError) as ve:
            self.c.dimensions = (20, 20)
        self.assertEqual(expected, str(ve.exception))

        with self.assertRaises(ValueError) as ve:
            self.c.dimensions = (20, 20, 20, 20)
        self.assertEqual(expected, str(ve.exception))

        expected = "Dimensions tuple must contain integers greater than zero."

        with self.assertRaises(ValueError) as ve:
            self.c.dimensions = (-20, 20, 20)
        self.assertEqual(expected, str(ve.exception))

        with self.assertRaises(ValueError) as ve:
            self.c.dimensions = (20, -20, 20)
        self.assertEqual(expected, str(ve.exception))

        with self.assertRaises(ValueError) as ve:
            self.c.dimensions = (20, 20, -20)
        self.assertEqual(expected, str(ve.exception))

        with self.assertRaises(ValueError) as ve:
            self.c.dimensions = (-20, -20, 20)
        self.assertEqual(expected, str(ve.exception))

        with self.assertRaises(ValueError) as ve:
            self.c.dimensions = (-20, 20, -20)
        self.assertEqual(expected, str(ve.exception))

        with self.assertRaises(ValueError) as ve:
            self.c.dimensions = (-20, 20, -20)
        self.assertEqual(expected, str(ve.exception))

    def test_correct_setter_weight_raise_value_error(self):
        expected = "Weight must be greater than zero."
        with self.assertRaises(ValueError) as ve:
            self.c.weight = -0.1
        self.assertEqual(expected, str(ve.exception))

        with self.assertRaises(ValueError) as ve:
            self.c.weight = 0
        self.assertEqual(expected, str(ve.exception))

    def test_get_available_status_returns_correct_string(self):
        self.assertEqual("Model: Chair is currently in stock.", self.c.get_available_status())

        self.c.in_stock = False
        self.assertEqual("Model: Chair is currently unavailable.", self.c.get_available_status())

    def test_get_specifications_returns_correct_string(self):
        expected = "Model: Chair has the following dimensions: 20mm x 20mm x 20mm and weighs: N/A"
        self.assertEqual(expected, self.c.get_specifications())
        self.t.model = "Table"
        result = "Model: Table has the following dimensions: 60mm x 80mm x 120mm and weighs: 25.7"
        self.assertEqual(result, self.t.get_specifications())


if __name__ == "__main__":
    main()
