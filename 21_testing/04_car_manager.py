class Car:
    def __init__(self, make, model, fuel_consumption, fuel_capacity):
        self.make = make
        self.model = model
        self.fuel_consumption = fuel_consumption
        self.fuel_capacity = fuel_capacity
        self.fuel_amount = 0

    @property
    def make(self):
        return self.__make

    @make.setter
    def make(self, new_value):
        if not new_value:
            raise Exception("Make cannot be null or empty!")
        self.__make = new_value

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, new_value):
        if not new_value:
            raise Exception("Model cannot be null or empty!")
        self.__model = new_value

    @property
    def fuel_consumption(self):
        return self.__fuel_consumption

    @fuel_consumption.setter
    def fuel_consumption(self, new_value):
        if new_value <= 0:
            raise Exception("Fuel consumption cannot be zero or negative!")
        self.__fuel_consumption = new_value

    @property
    def fuel_capacity(self):
        return self.__fuel_capacity

    @fuel_capacity.setter
    def fuel_capacity(self, new_value):
        if new_value <= 0:
            raise Exception("Fuel capacity cannot be zero or negative!")
        self.__fuel_capacity = new_value

    @property
    def fuel_amount(self):
        return self.__fuel_amount

    @fuel_amount.setter
    def fuel_amount(self, new_value):
        if new_value < 0:
            raise Exception("Fuel amount cannot be negative!")
        self.__fuel_amount = new_value

    def refuel(self, fuel):
        if fuel <= 0:
            raise Exception("Fuel amount cannot be zero or negative!")
        self.__fuel_amount += fuel
        if self.__fuel_amount > self.__fuel_capacity:
            self.__fuel_amount = self.__fuel_capacity

    def drive(self, distance):
        needed = (distance / 100) * self.__fuel_consumption

        if needed > self.__fuel_amount:
            raise Exception("You don't have enough fuel to drive!")

        self.__fuel_amount -= needed


# car = Car("a", "b", 1, 4)
# car.make = ""
# print(car)

import unittest


class CarTest(unittest.TestCase):
    def setUp(self):
        self.car = Car("WV", "Sharan", 6, 70)

    def test_constructor(self):
        self.assertEqual("WV", self.car.make)
        self.assertEqual("Sharan", self.car.model)
        self.assertEqual(6, self.car.fuel_consumption)
        self.assertEqual(70, self.car.fuel_capacity)
        self.assertEqual(0, self.car.fuel_amount)

    def test_make_property_getter_setter_for_incorrect_value_raise_error(self):
        with self.assertRaises(Exception) as ex:
            self.car.make = ''

        self.assertEqual("Make cannot be null or empty!", str(ex.exception))

        with self.assertRaises(Exception) as ex:
            self.car.make = 0
        self.assertEqual("Make cannot be null or empty!", str(ex.exception))

    def test_make_property_getter_setter_with_correct_value(self):
        self.assertEqual("WV", self.car.make)
        self.car.make = "Seat"
        self.assertEqual("Seat", self.car.make)

    def test_model_property_getter_setter_for_incorrect_value_raise_error(self):
        with self.assertRaises(Exception) as ex:
            self.car.model = ''

        self.assertEqual("Model cannot be null or empty!", str(ex.exception))

        with self.assertRaises(Exception) as ex:
            self.car.model = 0
        self.assertEqual("Model cannot be null or empty!", str(ex.exception))

    def test_model_property_getter_setter_with_correct_value(self):
        self.assertEqual("Sharan", self.car.model)
        self.car.model = "Alhambra"
        self.assertEqual("Alhambra", self.car.model)

    def test_fuel_consumption_property_getter_setter_for_incorrect_value_raise_error(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_consumption = 0

        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

        with self.assertRaises(Exception) as ex:
            self.car.fuel_consumption = -11
        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

    def test_fuel_consumption_property_getter_setter_with_correct_value(self):
        self.assertEqual(6, self.car.fuel_consumption)
        self.car.fuel_consumption = 7
        self.assertEqual(7, self.car.fuel_consumption)

    def test_fuel_capacity_property_getter_setter_for_incorrect_value_raise_error(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_capacity = 0

        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

        with self.assertRaises(Exception) as ex:
            self.car.fuel_capacity = -11
        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

    def test_fuel_capacity_property_getter_setter_with_correct_value(self):
        self.assertEqual(70, self.car.fuel_capacity)
        self.car.fuel_capacity = 60
        self.assertEqual(60, self.car.fuel_capacity)

    def test_fuel_amount_property_getter_setter_for_incorrect_value_raise_error(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_amount = -1

        self.assertEqual("Fuel amount cannot be negative!", str(ex.exception))

    def test_fuel_amount_property_getter_setter_with_correct_value(self):
        self.assertEqual(0, self.car.fuel_amount)
        self.car.fuel_amount = 60
        self.assertEqual(60, self.car.fuel_amount)

    def test_refuel_method_with_negative_value_raise_error(self):
        self.assertEqual(0, self.car.fuel_amount)
        with self.assertRaises(Exception) as ex:
            self.car.refuel(-20)

        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))

    def test_refuel_method_with_correct_value(self):
        self.assertEqual(0, self.car.fuel_amount)
        self.car.refuel(20)
        self.assertEqual(20, self.car.fuel_amount)

    def test_refuel_method_with_correct_higher_than_capacity_value(self):
        self.assertEqual(0, self.car.fuel_amount)
        self.car.refuel(80)
        self.assertEqual(70, self.car.fuel_amount)

    def test_drive_method_with_distance_bigger_than_car_can_drive_with_available_fuel_raise_error(self):
        self.assertEqual(0, self.car.fuel_amount)
        with self.assertRaises(Exception) as ex:
            self.car.drive(1)
        self.assertEqual("You don't have enough fuel to drive!", str(ex.exception))
        self.car.refuel(20)
        self.assertEqual(20, self.car.fuel_amount)
        with self.assertRaises(Exception) as ex:
            self.car.drive(351)
        self.assertEqual("You don't have enough fuel to drive!", str(ex.exception))

    def test_drive_method_with_distance_that_car_can_drive_with_available_fuel(self):
        self.car.refuel(30)
        self.car.drive(300)
        self.assertEqual(12, self.car.fuel_amount)


if __name__ == "__main__":
    unittest.main()
