from unittest import TestCase, main

from project.restaurant import Restaurant


class TestRestaurant(TestCase):
    def setUp(self) -> None:
        self.restaurant = Restaurant("Happy", 15)

    def test_correct_init(self):
        self.assertEqual("Happy", self.restaurant.name)
        self.assertEqual(15, self.restaurant.capacity)
        self.assertEqual([], self.restaurant.waiters)

    def test_name_setter_with_invalid_data_return_value_error(self):
        with self.assertRaises(ValueError) as ve:
            Restaurant("", 15)
        self.assertEqual("Invalid name!", str(ve.exception))

        with self.assertRaises(ValueError) as ve:
            Restaurant("  ", 15)
        self.assertEqual("Invalid name!", str(ve.exception))

        with self.assertRaises(ValueError) as ve:
            Restaurant(None, 15)
        self.assertEqual("Invalid name!", str(ve.exception))

    def test_capacity_setter_with_invalid_data_return_value_error(self):
        with self.assertRaises(ValueError) as ve:
            Restaurant("Test", -1)
        self.assertEqual("Invalid capacity!", str(ve.exception))

        with self.assertRaises(ValueError) as ve:
            self.restaurant.capacity = -5
        self.assertEqual("Invalid capacity!", str(ve.exception))

    def test_get_waiters_returns_correct_data(self):
        self.restaurant.waiters = [{'name': 'Test1', 'total_earnings': 5},
                                   {'name': 'Test2', 'total_earnings': 10}, {'name': 'Test3'}]
        result = [{'name': 'Test1', 'total_earnings': 5}, {'name': 'Test2', 'total_earnings': 10}]
        self.assertEqual(result, self.restaurant.get_waiters(3, 11))

        result = [{'name': 'Test1', 'total_earnings': 5}, {'name': 'Test2', 'total_earnings': 10}, {'name': 'Test3'}]
        self.assertEqual(result, self.restaurant.get_waiters())

        result = [{'name': 'Test2', 'total_earnings': 10}]
        self.assertEqual(result, self.restaurant.get_waiters(7))

        result = [{'name': 'Test3'}]
        self.assertEqual(result, self.restaurant.get_waiters(None, 0))

        result = [{'name': 'Test3'}]
        self.assertEqual(result, self.restaurant.get_waiters(0, 0))

    def test_add_waiter_with_correct_data_return_correct_message(self):
        self.assertEqual('The waiter Test1 has been added.', self.restaurant.add_waiter("Test1"))
        self.assertEqual([{'name': 'Test1'}], self.restaurant.waiters)

    def test_add_waiter_in_restaurant_with_max_waiters_correct_message(self):
        restaurant = Restaurant("Test", 3)
        restaurant.waiters = [{'name': 'Test1'}, {'name': 'Test2'}, {'name': 'Test3'}]
        self.assertEqual("No more places!", restaurant.add_waiter("Test4"))
        self.assertEqual([{'name': 'Test1'}, {'name': 'Test2'}, {'name': 'Test3'}], restaurant.waiters)

    def test_add_waiter_in_restaurant_with__existing_waiter_name_correct_message(self):
        self.restaurant.add_waiter("Test1")
        self.restaurant.add_waiter("Test2")
        self.assertEqual([{'name': 'Test1'}, {'name': 'Test2'}], self.restaurant.waiters)
        self.assertEqual(f"The waiter Test2 already exists!", self.restaurant.add_waiter("Test2"))
        self.assertEqual([{'name': 'Test1'}, {'name': 'Test2'}], self.restaurant.waiters)

    def test_remove_waiter_with_existing_names_return_correct_message(self):
        self.restaurant.add_waiter("Test1")
        self.restaurant.add_waiter("Test2")
        self.assertEqual([{'name': 'Test1'}, {'name': 'Test2'}], self.restaurant.waiters)
        self.assertEqual(f"The waiter Test1 has been removed.", self.restaurant.remove_waiter("Test1"))
        self.assertEqual([{'name': 'Test2'}], self.restaurant.waiters)

    def test_remove_waiter_with_names_not_in_waiters_list_return_correct_message(self):
        self.restaurant.add_waiter("Test1")
        self.restaurant.add_waiter("Test2")
        self.assertEqual([{'name': 'Test1'}, {'name': 'Test2'}], self.restaurant.waiters)
        self.assertEqual("No waiter found with the name Test.", self.restaurant.remove_waiter("Test"))
        self.assertEqual([{'name': 'Test1'}, {'name': 'Test2'}], self.restaurant.waiters)

    def test_get_total_earnings_return_correct_value(self):
        self.assertEqual(0, self.restaurant.get_total_earnings())
        self.restaurant.waiters = [{'name': 'Test1', 'total_earnings': 5},
                                   {'name': 'Test2', 'total_earnings': 10}, {'name': 'Test3'}]
        self.assertEqual(15, self.restaurant.get_total_earnings())


if __name__ == "__main__":
    main()
