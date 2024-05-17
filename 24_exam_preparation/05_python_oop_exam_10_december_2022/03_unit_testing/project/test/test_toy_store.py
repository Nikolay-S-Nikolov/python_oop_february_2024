from unittest import TestCase, main

from project.toy_store import ToyStore


class TestToyStore(TestCase):

    def setUp(self) -> None:
        self.store = ToyStore()

    def test_correct_constructor_init(self):
        result = self.store.toy_shelf
        expected = {'A': None, 'B': None, 'C': None, 'D': None, 'E': None, 'F': None, 'G': None}
        self.assertEqual(expected, result)

    def test_add_toy_with_correct_data_return_correct_message(self):
        self.assertEqual("Toy:Teddy placed successfully!", self.store.add_toy('A', 'Teddy'))
        expected = {'A': 'Teddy', 'B': None, 'C': None, 'D': None, 'E': None, 'F': None, 'G': None}
        self.assertEqual(expected, self.store.toy_shelf)
        self.assertEqual("Toy:Pooh placed successfully!", self.store.add_toy('B', 'Pooh'))
        self.assertEqual({'A': 'Teddy', 'B': 'Pooh', 'C': None, 'D': None, 'E': None, 'F': None, 'G': None},
                         self.store.toy_shelf)

    def test_add_toy_with_incorrect_shelf_raise_exception(self):
        self.add_toys()
        self.assertEqual({'A': 'Teddy', 'B': 'Pooh', 'C': None, 'D': None, 'E': None, 'F': None, 'G': None},
                         self.store.toy_shelf)
        with self.assertRaises(Exception) as ex:
            self.store.add_toy('X', 'Ralph')
        self.assertEqual("Shelf doesn't exist!", str(ex.exception))
        self.assertEqual({'A': 'Teddy', 'B': 'Pooh', 'C': None, 'D': None, 'E': None, 'F': None, 'G': None},
                         self.store.toy_shelf)

    def test_add_toy_with_toy_that_is_added_on_same_shelf_raise_exception(self):
        self.add_toys()
        self.assertEqual({'A': 'Teddy', 'B': 'Pooh', 'C': None, 'D': None, 'E': None, 'F': None, 'G': None},
                         self.store.toy_shelf)
        with self.assertRaises(Exception) as ex:
            self.store.add_toy('B', 'Pooh')
        self.assertEqual("Toy is already in shelf!", str(ex.exception))
        self.assertEqual({'A': 'Teddy', 'B': 'Pooh', 'C': None, 'D': None, 'E': None, 'F': None, 'G': None},
                         self.store.toy_shelf)

    def test_add_toy_with_shelf_already_taken_raise_exception(self):
        self.add_toys()
        self.assertEqual({'A': 'Teddy', 'B': 'Pooh', 'C': None, 'D': None, 'E': None, 'F': None, 'G': None},
                         self.store.toy_shelf)
        with self.assertRaises(Exception) as ex:
            self.store.add_toy('A', 'Ralph')
        self.assertEqual("Shelf is already taken!", str(ex.exception))
        self.assertEqual({'A': 'Teddy', 'B': 'Pooh', 'C': None, 'D': None, 'E': None, 'F': None, 'G': None},
                         self.store.toy_shelf)

    def test_remove_toy_correct_data_return_correct_message(self):
        self.add_toys()
        self.assertEqual({'A': 'Teddy', 'B': 'Pooh', 'C': None, 'D': None, 'E': None, 'F': None, 'G': None},
                         self.store.toy_shelf)
        self.assertEqual("Remove toy:Pooh successfully!", self.store.remove_toy('B', 'Pooh'))
        self.assertEqual({'A': 'Teddy', 'B': None, 'C': None, 'D': None, 'E': None, 'F': None, 'G': None},
                         self.store.toy_shelf)

    def test_remove_toy_with_not_existing_shelf_raise_exception(self):
        self.add_toys()
        self.assertEqual({'A': 'Teddy', 'B': 'Pooh', 'C': None, 'D': None, 'E': None, 'F': None, 'G': None},
                         self.store.toy_shelf)
        with self.assertRaises(Exception) as ex:
            self.store.remove_toy('Y', 'Ralph')

        self.assertEqual("Shelf doesn't exist!", str(ex.exception))
        self.assertEqual({'A': 'Teddy', 'B': 'Pooh', 'C': None, 'D': None, 'E': None, 'F': None, 'G': None},
                         self.store.toy_shelf)

    def test_remove_toy_with_toy_not_on_that_shelf_raise_exception(self):
        self.add_toys()
        self.assertEqual({'A': 'Teddy', 'B': 'Pooh', 'C': None, 'D': None, 'E': None, 'F': None, 'G': None},
                         self.store.toy_shelf)
        with self.assertRaises(Exception) as ex:
            self.store.remove_toy('B', 'Teddy')
        self.assertEqual("Toy in that shelf doesn't exists!", str(ex.exception))
        self.assertEqual({'A': 'Teddy', 'B': 'Pooh', 'C': None, 'D': None, 'E': None, 'F': None, 'G': None},
                         self.store.toy_shelf)

    def add_toys(self):
        self.store.add_toy('A', 'Teddy')
        self.store.add_toy('B', 'Pooh')


if __name__ == "__main__":
    main()
