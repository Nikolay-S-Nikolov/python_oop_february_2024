from unittest import TestCase, main

from project.trip import Trip


class TestTrip(TestCase):

    def setUp(self) -> None:
        self.trip = Trip(10_000, 3, True)

    def test_correct_constructor_init(self):
        self.assertEqual(10_000, self.trip.budget)
        self.assertEqual(3, self.trip.travelers)
        self.assertEqual(True, self.trip.is_family)
        self.assertEqual({}, self.trip.booked_destinations_paid_amounts)
        expected = {'New Zealand': 7500, 'Australia': 5700, 'Brazil': 6200, 'Bulgaria': 500}
        self.assertEqual(expected, self.trip.DESTINATION_PRICES_PER_PERSON)

    def test_travelers_setter_raise_value_error(self):
        with self.assertRaises(ValueError) as ve:
            Trip(5_000, 0, False)
        self.assertEqual('At least one traveler is required!', str(ve.exception))

        with self.assertRaises(ValueError) as ve:
            self.trip.travelers = 0
        self.assertEqual('At least one traveler is required!', str(ve.exception))

    def test_is_family_setter_change_to_false_when_one_traveler(self):
        self.trip.is_family = False
        self.assertEqual(False, self.trip.is_family)
        self.trip.travelers = 1
        self.trip.is_family = True
        self.assertEqual(False, self.trip.is_family)
        new_trip = Trip(5_000, 1, True)
        self.assertEqual(False, new_trip.is_family)

    def test_book_a_trip_with_wrong_destination_return_correct_message(self):
        expected = 'This destination is not in our offers, please choose a new one!'
        self.assertEqual(expected, self.trip.book_a_trip('Greece'))

    def test_book_a_trip_with_not_enough_budget(self):
        self.assertEqual(10_000, self.trip.budget)
        self.assertEqual({}, self.trip.booked_destinations_paid_amounts)
        self.assertEqual('Your budget is not enough!', self.trip.book_a_trip('New Zealand'))
        self.assertEqual(10_000, self.trip.budget)
        self.assertEqual({}, self.trip.booked_destinations_paid_amounts)
        self.trip.book_a_trip('Bulgaria')
        self.assertEqual(8650, self.trip.budget)
        self.assertEqual({'Bulgaria': 1350.0}, self.trip.booked_destinations_paid_amounts)
        self.assertEqual('Your budget is not enough!', self.trip.book_a_trip('Brazil'))
        self.assertEqual(8650, self.trip.budget)
        self.assertEqual({'Bulgaria': 1350.0}, self.trip.booked_destinations_paid_amounts)

    def test_book_a_trip_with_family_and_enough_budget_return_correct_message_and_change_values(self):
        self.assertEqual(10_000, self.trip.budget)
        self.assertEqual({}, self.trip.booked_destinations_paid_amounts)
        expected = 'Successfully booked destination Bulgaria! Your budget left is 8650.00'
        self.assertEqual(expected, self.trip.book_a_trip('Bulgaria'))
        self.assertEqual(8650, self.trip.budget)
        self.assertEqual({'Bulgaria': 1350.0}, self.trip.booked_destinations_paid_amounts)
        self.trip.budget = 30_000
        expected = 'Successfully booked destination New Zealand! Your budget left is 9750.00'
        self.assertEqual(expected, self.trip.book_a_trip('New Zealand'))
        self.assertEqual(9750, self.trip.budget)
        self.assertEqual({'Bulgaria': 1350.0, 'New Zealand': 20250.0}, self.trip.booked_destinations_paid_amounts)

    def test_book_a_trip_with_enough_budget_and_not_family_return_correct_message_and_change_values(self):
        new_trip = Trip(50_000, 2, False)
        expected = 'Successfully booked destination New Zealand! Your budget left is 35000.00'
        self.assertEqual(expected, new_trip.book_a_trip('New Zealand'))
        self.assertEqual(35000, new_trip.budget)
        self.assertEqual({'New Zealand': 15000}, new_trip.booked_destinations_paid_amounts)
        expected = 'Successfully booked destination Australia! Your budget left is 23600.00'
        self.assertEqual(expected, new_trip.book_a_trip('Australia'))
        self.assertEqual(23600, new_trip.budget)
        self.assertEqual({'Australia': 11400, 'New Zealand': 15000}, new_trip.booked_destinations_paid_amounts)

    def test_booking_status_with_no_booking_return_correct_message(self):
        self.assertEqual('No bookings yet. Budget: 10000.00', self.trip.booking_status())

    def test_booking_status_with_booking_return_correct_message(self):
        self.trip.budget = 25_000
        self.trip.book_a_trip('Bulgaria')
        self.trip.book_a_trip('Australia')
        expected = """Booked Destination: Australia
Paid Amount: 15390.00
Booked Destination: Bulgaria
Paid Amount: 1350.00
Number of Travelers: 3
Budget Left: 8260.00"""
        self.assertEqual(expected, self.trip.booking_status())


if __name__ == "__main__":
    main()
