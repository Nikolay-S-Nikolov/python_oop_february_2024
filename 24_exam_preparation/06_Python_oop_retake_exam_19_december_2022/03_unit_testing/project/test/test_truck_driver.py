from unittest import TestCase, main

from project.truck_driver import TruckDriver


class TestTruckDriver(TestCase):
    def setUp(self) -> None:
        self.driver = TruckDriver("Hasan", 2.00)

    def test_constructor_correct_init(self):
        self.assertEqual("Hasan", self.driver.name)
        self.assertEqual(2.00, self.driver.money_per_mile)
        self.assertEqual({}, self.driver.available_cargos)
        self.assertEqual(0, self.driver.earned_money)
        self.assertEqual(0, self.driver.miles)

    def test_earned_money_setter_with_negative_value_raise_value_error(self):
        self.assertEqual(0, self.driver.earned_money)
        with self.assertRaises(ValueError) as ve:
            self.driver.earned_money = -1
        self.assertEqual("Hasan went bankrupt.", str(ve.exception))
        self.assertEqual(0, self.driver.earned_money)
        with self.assertRaises(ValueError) as ve:
            self.driver.eat(250)
        self.assertEqual("Hasan went bankrupt.", str(ve.exception))
        self.assertEqual(0, self.driver.earned_money)

    def test_add_cargo_offer_with_correct_data_return_correct_message(self):
        self.assertEqual({}, self.driver.available_cargos)
        self.assertEqual("Cargo for 200 to Sofia was added as an offer.", self.driver.add_cargo_offer('Sofia', 200))
        self.assertEqual({'Sofia': 200}, self.driver.available_cargos)
        self.assertEqual("Cargo for 500 to Istanbul was added as an offer.",
                         self.driver.add_cargo_offer('Istanbul', 500))
        self.assertEqual({'Sofia': 200, 'Istanbul': 500}, self.driver.available_cargos)

    def test_add_cargo_offer_with_already_added_cargo_raise_exception(self):
        self.assertEqual("Cargo for 200 to Sofia was added as an offer.", self.driver.add_cargo_offer('Sofia', 200))
        self.assertEqual({'Sofia': 200}, self.driver.available_cargos)
        with self.assertRaises(Exception) as ex:
            self.driver.add_cargo_offer('Sofia', 230)
        self.assertEqual("Cargo offer is already added.", str(ex.exception))
        self.assertEqual({'Sofia': 200}, self.driver.available_cargos)

    def test_drive_best_cargo_offer_with_correct_data_return_correct_message(self):  # check for activity no done
        self.assertEqual(0, self.driver.earned_money)
        self.assertEqual(0, self.driver.miles)
        self.driver.add_cargo_offer('Sofia', 100)
        self.driver.add_cargo_offer('Istanbul', 200)
        self.assertEqual({'Sofia': 100, 'Istanbul': 200}, self.driver.available_cargos)
        self.assertEqual("Hasan is driving 200 to Istanbul.", self.driver.drive_best_cargo_offer())
        self.assertEqual({'Sofia': 100, 'Istanbul': 200}, self.driver.available_cargos)
        self.assertEqual(400, self.driver.earned_money)
        self.assertEqual(200, self.driver.miles)

    def test_drive_best_cargo_offer_with_no_offers_return_correct_message(self):  # check for activity no done
        self.assertEqual(0, self.driver.earned_money)
        self.assertEqual(0, self.driver.miles)
        self.assertEqual({}, self.driver.available_cargos)
        self.assertEqual("There are no offers available.", self.driver.drive_best_cargo_offer())
        self.assertEqual(0, self.driver.earned_money)
        self.assertEqual(0, self.driver.miles)
        self.assertEqual({}, self.driver.available_cargos)

    def test_check_for_activities_change_correct_data(self):
        self.assertEqual(0, self.driver.earned_money)
        self.assertEqual(0, self.driver.miles)
        self.driver.check_for_activities(0)
        self.assertEqual(0, self.driver.earned_money)
        self.assertEqual(0, self.driver.miles)
        self.driver.add_cargo_offer('London', 1251)
        self.driver.drive_best_cargo_offer()
        self.assertEqual(2357, self.driver.earned_money)
        self.assertEqual(1251, self.driver.miles)
        self.driver.check_for_activities(1251)
        self.assertEqual(2212, self.driver.earned_money)
        self.assertEqual(1251, self.driver.miles)

    def test_eat_method_changes_correct_data(self):
        self.driver.earned_money = 10_000
        self.assertEqual(10_000, self.driver.earned_money)
        self.driver.eat(249)
        self.assertEqual(10_000, self.driver.earned_money)
        self.driver.eat(250)
        self.assertEqual(9980, self.driver.earned_money)
        self.driver.eat(251)
        self.assertEqual(9980, self.driver.earned_money)

    def test_sleep_method_changes_correct_data(self):
        self.driver.earned_money = 10_000
        self.assertEqual(10_000, self.driver.earned_money)
        self.driver.sleep(999)
        self.assertEqual(10_000, self.driver.earned_money)
        self.driver.sleep(1_000)
        self.assertEqual(9955, self.driver.earned_money)
        self.driver.eat(1001)
        self.assertEqual(9955, self.driver.earned_money)

    def test_pump_gas_method_changes_correct_data(self):
        self.driver.earned_money = 10_000
        self.assertEqual(10_000, self.driver.earned_money)
        self.driver.pump_gas(1_499)
        self.assertEqual(10_000, self.driver.earned_money)
        self.driver.pump_gas(1_500)
        self.assertEqual(9500, self.driver.earned_money)
        self.driver.pump_gas(1501)
        self.assertEqual(9500, self.driver.earned_money)

    def test_repair_truck_method_changes_correct_data(self):
        self.driver.earned_money = 10_000
        self.assertEqual(10_000, self.driver.earned_money)
        self.driver.repair_truck(9_999)
        self.assertEqual(10_000, self.driver.earned_money)
        self.driver.repair_truck(10_000)
        self.assertEqual(2500, self.driver.earned_money)
        self.driver.repair_truck(10_001)
        self.assertEqual(2500, self.driver.earned_money)

    def test_all_methods_eat_sleep_repair_truck_and_pump_gas__changes_correct_data(self):
        self.driver.earned_money = 50_000
        self.driver.check_for_activities(40_000)
        self.assertEqual(2000, self.driver.earned_money)

    def test__repr__method_return_correct_message(self):
        self.driver.add_cargo_offer('London', 1251)
        self.driver.drive_best_cargo_offer()
        self.assertEqual(2357, self.driver.earned_money)
        self.assertEqual(1251, self.driver.miles)
        expected = "Hasan has 1251 miles behind his back."
        actual = str(self.driver)
        self.assertEqual(expected, actual)
        self.assertEqual('Hasan has 1251 miles behind his back.', f"{self.driver}")


if __name__ == "__main__":
    main()
