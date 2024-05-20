from unittest import TestCase, main

from project.robot import Robot


class TestRobot(TestCase):
    def setUp(self) -> None:
        self.robot = Robot("Peso", 'Military', 25, 110)

    def test_constructor_for_correct_init(self):
        self.assertEqual(['Military', 'Education', 'Entertainment', 'Humanoids'], self.robot.ALLOWED_CATEGORIES)
        self.assertEqual(1.5, self.robot.PRICE_INCREMENT)
        self.assertEqual('Peso', self.robot.robot_id)
        self.assertEqual('Military', self.robot.category)
        self.assertEqual(25, self.robot.available_capacity)
        self.assertEqual(110, self.robot.price)
        self.assertEqual([], self.robot.hardware_upgrades)
        self.assertEqual([], self.robot.software_updates)

    def test_category_setter_with_not_existing_type_return_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.robot.category = 'Agricultural'
        expected = "Category should be one of '['Military', 'Education', 'Entertainment', 'Humanoids']'"
        self.assertEqual(expected, str(ve.exception))
        self.assertEqual('Military', self.robot.category)
        with self.assertRaises(ValueError) as ve:
            Robot('Robot', 'Agricultural', 25, 110)
        self.assertEqual(expected, str(ve.exception))

    def test_category_price_with_negative_value_return_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.robot.price = -1
        self.assertEqual("Price cannot be negative!", str(ve.exception))
        self.assertEqual(110, self.robot.price)
        with self.assertRaises(ValueError) as ve:
            Robot('Robot', 'Humanoids', 25, -5)
        self.assertEqual("Price cannot be negative!", str(ve.exception))

    def test_upgrade_method_with_correct_data_return_correct_message(self):
        self.assertEqual([], self.robot.hardware_upgrades)
        self.assertEqual('Robot Peso was upgraded with Machine gun.', self.robot.upgrade('Machine gun', 20))
        self.assertEqual(['Machine gun'], self.robot.hardware_upgrades)
        self.assertEqual(140, self.robot.price)

        self.assertEqual('Robot Peso was upgraded with First aid.', self.robot.upgrade('First aid', 30))
        self.assertEqual(['Machine gun', 'First aid'], self.robot.hardware_upgrades)
        self.assertEqual(185, self.robot.price)

    def test_upgrade_method_with_existing_component_return_correct_message(self):
        self.robot.upgrade('Machine gun', 20)
        self.robot.upgrade('First aid', 30)
        self.assertEqual(['Machine gun', 'First aid'], self.robot.hardware_upgrades)
        self.assertEqual(185, self.robot.price)
        self.assertEqual(f"Robot Peso was not upgraded.", self.robot.upgrade('Machine gun', 10))
        self.assertEqual(['Machine gun', 'First aid'], self.robot.hardware_upgrades)
        self.assertEqual(185, self.robot.price)
        self.assertEqual(f"Robot Peso was not upgraded.", self.robot.upgrade('First aid', 15))
        self.assertEqual(['Machine gun', 'First aid'], self.robot.hardware_upgrades)
        self.assertEqual(185, self.robot.price)

    def test_update_method_with_correct_data_return_correct_message(self):
        self.assertEqual([], self.robot.software_updates)
        self.assertEqual('Robot Peso was updated to version 1.1.', self.robot.update(1.1, 5))
        self.assertEqual(20, self.robot.available_capacity)
        self.assertEqual([1.1], self.robot.software_updates)
        self.assertEqual('Robot Peso was updated to version 2.0.', self.robot.update(2.0, 6))
        self.assertEqual(14, self.robot.available_capacity)
        self.assertEqual([1.1, 2.0], self.robot.software_updates)

    def test_update_method_with_incorrect_data_return_correct_message(self):
        self.robot.update(1.1, 5)
        self.robot.update(2.0, 6)
        self.assertEqual(14, self.robot.available_capacity)
        self.assertEqual([1.1, 2.0], self.robot.software_updates)
        self.assertEqual("Robot Peso was not updated.", self.robot.update(1.5, 6))
        self.assertEqual(14, self.robot.available_capacity)
        self.assertEqual([1.1, 2.0], self.robot.software_updates)
        self.assertEqual("Robot Peso was not updated.", self.robot.update(2.8, 15))
        self.assertEqual(14, self.robot.available_capacity)
        self.assertEqual([1.1, 2.0], self.robot.software_updates)
        self.assertEqual("Robot Peso was not updated.", self.robot.update(1.8, 15))
        self.assertEqual(14, self.robot.available_capacity)
        self.assertEqual([1.1, 2.0], self.robot.software_updates)

    def test__gt__method_with_smaller_price_of_other_robot_return_correct_message(self):
        result = self.robot.__gt__(Robot('EVA', 'Humanoids', 25, 25))
        self.assertEqual('Robot with ID Peso is more expensive than Robot with ID EVA.', result)
        result = self.robot > Robot('EVA', 'Humanoids', 25, 25)
        self.assertEqual('Robot with ID Peso is more expensive than Robot with ID EVA.', result)

    def test__gt__method_with_higher_price_of_other_robot_return_correct_message(self):
        result = self.robot.__gt__(Robot('EVA', 'Humanoids', 25, 125))
        self.assertEqual('Robot with ID Peso is cheaper than Robot with ID EVA.', result)
        result = self.robot > Robot('EVA', 'Humanoids', 25, 125)
        self.assertEqual('Robot with ID Peso is cheaper than Robot with ID EVA.', result)

    def test__gt__method_with_equal_price_of_other_robot_return_correct_message(self):
        result = self.robot.__gt__(Robot('EVA', 'Humanoids', 25, 110))
        self.assertEqual('Robot with ID Peso costs equal to Robot with ID EVA.', result)
        result = self.robot > Robot('EVA', 'Humanoids', 25, 110)
        self.assertEqual('Robot with ID Peso costs equal to Robot with ID EVA.', result)


if __name__ == "__main__":
    main()
