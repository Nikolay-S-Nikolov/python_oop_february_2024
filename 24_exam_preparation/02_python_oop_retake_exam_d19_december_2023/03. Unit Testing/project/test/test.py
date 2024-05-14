from unittest import TestCase, main

from project.climbing_robot import ClimbingRobot


class TestClimbingRobot(TestCase):
    def setUp(self) -> None:
        self.robot = ClimbingRobot('Mountain', 'test_part', 5, 10)
        self.software = {'name': "test_software", 'capacity_consumption': 2, 'memory_consumption': 3}
        self.software_1 = {'name': "test_software1", 'capacity_consumption': 1, 'memory_consumption': 2}

    def test_constructor_for_correct_init(self):
        self.assertEqual(['Mountain', 'Alpine', 'Indoor', 'Bouldering'], ClimbingRobot.ALLOWED_CATEGORIES)
        self.assertEqual(['Mountain', 'Alpine', 'Indoor', 'Bouldering'], self.robot.ALLOWED_CATEGORIES)
        self.assertEqual('Mountain', self.robot.category)
        self.assertEqual('test_part', self.robot.part_type)
        self.assertEqual(5, self.robot.capacity)
        self.assertEqual(10, self.robot.memory)
        self.assertEqual([], self.robot.installed_software)

    def test_check_setter_category_with_incorrect_data_raise_error(self):
        with self.assertRaises(ValueError) as ex:
            robot = ClimbingRobot('Test', 'test_part', 5, 10)
        self.assertEqual(f"Category should be one of ['Mountain', 'Alpine', 'Indoor', 'Bouldering']", str(ex.exception))

    def test_check_setter_category_with_correct_data_(self):
        self.robot.category = 'Indoor'
        self.assertEqual('Indoor', self.robot.category)

    def test_get_used_capacity_method_returns_correct_data(self):
        self.robot.install_software(self.software)
        self.robot.install_software(self.software_1)
        self.assertEqual(3, self.robot.get_used_capacity())

    def test_get_available_capacity_method_returns_correct_data(self):
        self.robot.install_software(self.software)
        self.assertEqual(3, self.robot.get_available_capacity())

    def test_get_used_memory_method_returns_correct_data(self):
        self.robot.install_software(self.software)
        self.robot.install_software(self.software_1)
        self.assertEqual(5, self.robot.get_used_memory())

    def test_get_available_memory_method_returns_correct_data(self):
        self.robot.install_software(self.software)
        self.assertEqual(7, self.robot.get_available_memory())

    def test_install_software_with_correct_data_return_correct_string(self):
        expected = self.robot.install_software(self.software)
        self.assertEqual("Software 'test_software' successfully installed on Mountain part.", expected)
        self.assertEqual([{'name': "test_software", 'capacity_consumption': 2, 'memory_consumption': 3}],
                         self.robot.installed_software)

    def test_install_software_with_exact_data_return_correct_string(self):
        software = {'name': "test_software", 'capacity_consumption': 5, 'memory_consumption': 10}
        expected = self.robot.install_software(software)
        self.assertEqual("Software 'test_software' successfully installed on Mountain part.", expected)
        self.assertEqual([{'name': "test_software", 'capacity_consumption': 5, 'memory_consumption': 10}],
                         self.robot.installed_software)

    def test_install_software_with_incorrect_data_return_correct_string(self):
        software = {'name': "test_software", 'capacity_consumption': 6, 'memory_consumption': 3}
        expected = self.robot.install_software(software)
        self.assertEqual("Software 'test_software' cannot be installed on Mountain part.", expected)
        self.assertEqual([], self.robot.installed_software)
        software = {'name': "test_software", 'capacity_consumption': 3, 'memory_consumption': 11}
        expected = self.robot.install_software(software)
        self.assertEqual("Software 'test_software' cannot be installed on Mountain part.", expected)
        self.assertEqual([], self.robot.installed_software)


if __name__ == "__main__":
    main()
