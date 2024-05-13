from collections import deque
from unittest import TestCase, main

from project.railway_station import RailwayStation


class TestRailwayStation(TestCase):
    def setUp(self) -> None:
        self.station = RailwayStation("Test")

    def test_constructor_correct_init(self):
        self.assertEqual("Test", self.station.name)
        self.assertEqual(deque([]), self.station.arrival_trains)
        self.assertEqual(deque([]), self.station.departure_trains)

    def test_name_setter_raise_error_with_incorrect_data(self):
        with self.assertRaises(ValueError) as ex:
            RailwayStation('Tes')
        self.assertEqual("Name should be more than 3 symbols!", str(ex.exception))

        with self.assertRaises(ValueError) as ex:
            RailwayStation('')
        self.assertEqual("Name should be more than 3 symbols!", str(ex.exception))

    def test_method_new_arrival_on_board_correct_data(self):
        self.assertEqual(deque([]), self.station.arrival_trains)
        self.station.new_arrival_on_board('arrival')
        self.assertEqual(deque(['arrival']), self.station.arrival_trains)

    def test_train_has_arrived_method_with_correct_data(self):
        self.station.new_arrival_on_board('arrival')
        expected = self.station.train_has_arrived('arrival')
        self.assertEqual("arrival is on the platform and will leave in 5 minutes.", expected)
        self.assertEqual(deque(['arrival']), self.station.departure_trains)
        self.assertEqual(deque([]), self.station.arrival_trains)

    def test_train_has_arrived_method_with_train_not_next_in_line(self):
        self.station.new_arrival_on_board('arrival')
        self.station.new_arrival_on_board('next')
        expected = self.station.train_has_arrived('next')
        self.assertEqual("There are other trains to arrive before next.", expected)

    def test_train_has_left_method_with_correct_data(self):
        self.station.new_arrival_on_board('arrival')
        self.station.train_has_arrived('arrival')
        expected = self.station.train_has_left('arrival')
        self.assertTrue(expected)
        self.assertEqual(deque([]), self.station.departure_trains)

    def test_train_has_left_method_with_train_not_next_in_line(self):
        self.station.new_arrival_on_board('arrival')
        self.station.train_has_arrived('arrival')
        self.station.new_arrival_on_board('next')
        self.station.train_has_arrived('next')
        expected = self.station.train_has_left('next')
        self.assertFalse(expected)
        self.assertEqual(deque(['arrival', 'next']), self.station.departure_trains)


if __name__ == "__main__":
    main()
