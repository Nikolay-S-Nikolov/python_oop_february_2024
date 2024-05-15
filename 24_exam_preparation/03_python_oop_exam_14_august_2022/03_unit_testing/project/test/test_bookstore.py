from unittest import TestCase, main

from project.bookstore import Bookstore


class TestBookstore(TestCase):
    def setUp(self) -> None:
        self.store = Bookstore(20)

    def test_constructor_correct_init(self):
        self.assertEqual(20, self.store.books_limit)
        self.assertEqual({}, self.store.availability_in_store_by_book_titles)
        self.assertEqual(0, self.store._Bookstore__total_sold_books)
        self.assertEqual(0, self.store.total_sold_books)

    def test_books_limit_setter_with_incorrect_data_raise_value_error(self):
        with self.assertRaises(ValueError) as ex:
            self.store = Bookstore(0)
        self.assertEqual(f"Books limit of 0 is not valid", str(ex.exception))
        with self.assertRaises(ValueError) as ex:
            self.store = Bookstore(-5)
        self.assertEqual(f"Books limit of -5 is not valid", str(ex.exception))

    def test_len_method_returns_correct_value(self):
        self.assertEqual(0, len(self.store))
        self.store.receive_book('Test', 3)
        self.assertEqual(3, len(self.store))
        self.store.receive_book('Test1', 2)
        self.store.receive_book('Test2', 5)
        self.assertEqual(10, len(self.store))

    def test_receive_book_method_with_books_amount_that_return_limit_exception(self):
        self.assertEqual(0, len(self.store))
        self.store.receive_book('Test', 20)
        with self.assertRaises(Exception) as ex:
            self.store.receive_book('Test1', 1)
        self.assertEqual("Books limit is reached. Cannot receive more books!", str(ex.exception))
        self.assertEqual(20, len(self.store))

    def test_receive_book_method__returns_correct_message(self):
        self.assertEqual(0, len(self.store))
        expected = self.store.receive_book('Test', 5)
        self.assertEqual("5 copies of Test are available in the bookstore.", expected)
        expected = self.store.receive_book('Test', 10)
        self.assertEqual("15 copies of Test are available in the bookstore.", expected)
        expected = self.store.receive_book('Test1', 3)
        self.assertEqual("3 copies of Test1 are available in the bookstore.", expected)

    def test_sell_book_method_with_incorrect_data_raises_exception(self):
        self.store.receive_book('Test', 5)
        with self.assertRaises(Exception) as ex:
            self.store.sell_book('test1', 5)
        self.assertEqual("Book test1 doesn't exist!", str(ex.exception))

    def test_sell_book_method_with_not_enough_book_copies_raises_exception(self):
        self.store.receive_book('Test', 5)
        with self.assertRaises(Exception) as ex:
            self.store.sell_book('Test', 6)
        self.assertEqual("Test has not enough copies to sell. Left: 5", str(ex.exception))

    def test_sell_book_method_with_correct_data_returns_correct_message(self):
        self.store.receive_book('Test', 5)
        self.store.receive_book('Test1', 15)
        expected = self.store.sell_book('Test1', 15)
        self.assertEqual("Sold 15 copies of Test1", expected)
        self.assertEqual(0, self.store.availability_in_store_by_book_titles["Test1"])
        self.assertEqual(5, self.store.availability_in_store_by_book_titles["Test"])

    def test_str_method_returns_correct_message(self):
        expected = str(self.store)
        self.assertEqual("Total sold books: 0\nCurrent availability: 0", expected)
        self.store.receive_book('Test', 5)
        self.store.receive_book('Test1', 15)
        self.store.sell_book('Test1', 6)
        self.store.sell_book('Test', 3)
        expected = "Total sold books: 9\nCurrent availability: 11\n - Test: 2 copies\n - Test1: 9 copies"
        self.assertEqual(expected, str(self.store))


if __name__ == "__main__":
    main()
