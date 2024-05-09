from unittest import TestCase, main

from project.vehicle import Vehicle


class TestVehicle(TestCase):
    def setUp(self) -> None:
        self.car = Vehicle(1.5, 5.5)

    def test_if_default_fuel_cons_class_atribute_is_existing(self):
        self.assertEqual(1.25, self.car.DEFAULT_FUEL_CONSUMPTION)

    def test_correct_constructor_setup(self):
        self.assertEqual(1.5, self.car.fuel)
        self.assertEqual(5.5, self.car.horse_power)
        self.assertEqual(1.5, self.car.capacity)
        self.assertEqual(1.25, self.car.fuel_consumption)

    def test_drive_method_with_kilometers_raise_error(self):
        with self.assertRaises(Exception) as ex:
            self.car.drive(5)
        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_drive_method_kilometers_that_car_can_drive(self):
        self.assertEqual(1.5, self.car.fuel)
        self.car.drive(1)
        self.assertEqual(0.25, self.car.fuel)

    def test_refuel_method_with_fuel_amount_bigger_than_capacity_raises_message(self):
        self.assertEqual(1.5, self.car.fuel)
        self.car.drive(1)
        with self.assertRaises(Exception) as ex:
            self.car.refuel(2)
        self.assertEqual("Too much fuel", str(ex.exception))

    def test_refuel_method_with_fuel_that_vehicle_capacity_is_not_exceeded(self):
        self.assertEqual(1.5, self.car.fuel)
        self.car.drive(1)
        self.car.refuel(0.75)
        self.assertEqual(1.0, self.car.fuel)

    def test__str__method_for_correct_message(self):
        expected = str(self.car)
        self.assertEqual("The vehicle has 5.5 horse power with 1.5 fuel left and 1.25 fuel consumption", expected)
