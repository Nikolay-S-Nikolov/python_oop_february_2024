from unittest import TestCase, main

from project.second_hand_car import SecondHandCar


class TestSecondHandCar(TestCase):

    def setUp(self) -> None:
        self.car = SecondHandCar("WV", "Golf", 110_000, 2_000)

    def test_constructor_correct_init(self):
        self.assertEqual("WV", self.car.model)
        self.assertEqual("Golf", self.car.car_type)
        self.assertEqual(110_000, self.car.mileage)
        self.assertEqual(2_000, self.car.price)
        self.assertEqual([], self.car.repairs)

    def test_price_setter_with_le_then_one_raise_value_error_message(self):
        with self.assertRaises(ValueError) as ve:
            SecondHandCar('Opel', 'Astra', 300_000, 1)
        self.assertEqual('Price should be greater than 1.0!', str(ve.exception))
        with self.assertRaises(ValueError) as ve:
            SecondHandCar('Opel', 'Astra', 300_000, 0)
        self.assertEqual('Price should be greater than 1.0!', str(ve.exception))
        with self.assertRaises(ValueError) as ve:
            self.car.price = -100
        self.assertEqual('Price should be greater than 1.0!', str(ve.exception))

    def test_mileage_setter_with__less_and_equal_to__100_raise_value_error_message(self):
        with self.assertRaises(ValueError) as ve:
            SecondHandCar('Opel', 'Astra', 100, 3)
        self.assertEqual('Please, second-hand cars only! Mileage must be greater than 100!', str(ve.exception))
        with self.assertRaises(ValueError) as ve:
            SecondHandCar('Opel', 'Astra', 99, 3)
        self.assertEqual('Please, second-hand cars only! Mileage must be greater than 100!', str(ve.exception))
        with self.assertRaises(ValueError) as ve:
            self.car.mileage = 0
        self.assertEqual('Please, second-hand cars only! Mileage must be greater than 100!', str(ve.exception))

    def test_set_promotional_price_with_new_price_smaller_then_old_return_correct_message(self):
        self.assertEqual(2_000, self.car.price)
        self.assertEqual('The promotional price has been successfully set.', self.car.set_promotional_price(1_999))
        self.assertEqual(1_999, self.car.price)
        self.assertEqual('The promotional price has been successfully set.', self.car.set_promotional_price(1_500))
        self.assertEqual(1_500, self.car.price)

    def test_set_promotional_price_with_new_price_equal_or_higher_then_old_raise_value_error_message(self):
        with self.assertRaises(ValueError) as ve:
            self.car.set_promotional_price(2_000)
        self.assertEqual('You are supposed to decrease the price!', str(ve.exception))
        self.assertEqual(2_000, self.car.price)
        with self.assertRaises(ValueError) as ve:
            self.car.set_promotional_price(2_500)
        self.assertEqual('You are supposed to decrease the price!', str(ve.exception))
        self.assertEqual(2_000, self.car.price)

    def test_need_repair_with_repair_price_higher_then_car_price_divided_by_2_return_correct_message(self):
        self.assertEqual('Repair is impossible!', self.car.need_repair(1_001, "replace engine"))
        self.assertEqual(2_000, self.car.price)
        self.assertEqual([], self.car.repairs)
        self.car.need_repair(500, "replace engine")
        self.assertEqual(2_500, self.car.price)
        self.assertEqual(['replace engine'], self.car.repairs)
        self.assertEqual('Repair is impossible!', self.car.need_repair(1_251, "replace gear"))
        self.assertEqual(2_500, self.car.price)
        self.assertEqual(['replace engine'], self.car.repairs)

    def test_need_repair_return_correct_message(self):
        self.assertEqual(2_000, self.car.price)
        self.assertEqual([], self.car.repairs)
        self.assertEqual('Price has been increased due to repair charges.', self.car.need_repair(500, "replace engine"))
        self.assertEqual(2_500, self.car.price)
        self.assertEqual(['replace engine'], self.car.repairs)
        self.assertEqual('Price has been increased due to repair charges.', self.car.need_repair(250, "replace gear"))
        self.assertEqual(2_750, self.car.price)
        self.assertEqual(['replace engine', "replace gear"], self.car.repairs)

    def test__gt__method_with_different_car_type_return_correct_message(self):
        other_car = SecondHandCar('Opel', 'Astra', 200_000, 2200)
        self.assertEqual('Cars cannot be compared. Type mismatch!', self.car > other_car)
        self.assertEqual('Cars cannot be compared. Type mismatch!', self.car.__gt__(other_car))

    def test__gt__method_with_correct_car_type_return_true_or_false(self):
        other_car = SecondHandCar('WV', 'Golf', 200_000, 1800)
        self.assertTrue(self.car > other_car)
        self.assertTrue(self.car.__gt__(other_car))
        other_golf = SecondHandCar('WV', 'Golf', 200_000, 2_000)
        self.assertFalse(self.car > other_golf)
        self.assertFalse(self.car.__gt__(other_golf))

    def test__str__method_return_correct_message(self):
        self.car.need_repair(500, "replace engine")
        self.car.need_repair(250, "replace gear")
        result = f"""Model {self.car.model} | Type {self.car.car_type} | Milage {self.car.mileage}km
Current price: {self.car.price:.2f} | Number of Repairs: {len(self.car.repairs)}"""
        self.assertEqual(result, str(self.car))


if __name__ == "__main__":
    main()
