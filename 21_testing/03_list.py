class IntegerList:
    def __init__(self, *args):
        self.__data = []
        for x in args:
            if type(x) == int:
                self.__data.append(x)

    def get_data(self):
        return self.__data

    def add(self, element):
        if not type(element) == int:
            raise ValueError("Element is not Integer")
        self.get_data().append(element)
        return self.get_data()

    def remove_index(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        a = self.get_data()[index]
        del self.get_data()[index]
        return a

    def get(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        return self.get_data()[index]

    def insert(self, index, el):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        elif not type(el) == int:
            raise ValueError("Element is not Integer")

        self.get_data().insert(index, el)

    def get_biggest(self):
        a = sorted(self.get_data(), reverse=True)
        return a[0]

    def get_index(self, el):
        return self.get_data().index(el)


import unittest


class IntegerListTest(unittest.TestCase):
    def setUp(self) -> None:
        self.integers_list = IntegerList(1, 2, 3)

    def test_constructor(self):
        self.assertEqual(3, len(self.integers_list.get_data()))
        self.assertEqual(list, type(self.integers_list.get_data()))
        list_with_not_integers = [6.5, "test", {1: 1, 2: 2}, {1, 2, 3}, (1, 7), False]
        for not_integer in list_with_not_integers:
            integers_list = IntegerList(1, 2, not_integer)
            self.assertEqual(2, len(integers_list.get_data()))

    def test_get_data_return_list_with_elements(self):
        self.assertEqual(3, len(self.integers_list.get_data()))
        self.assertEqual([1, 2, 3], self.integers_list.get_data())

    def test_add_element_method_with_not_integers_raises_error(self):

        list_with_not_integers = [6.5, "test", {1: 1, 2: 2}, {1, 2, 3}, (1, 7), False]

        with self.assertRaises(ValueError) as ex:
            for not_integer in list_with_not_integers:
                self.integers_list.add(not_integer)
            self.assertEqual("Element is not Integer", str(ex.exception))

        self.assertEqual("Element is not Integer", str(ex.exception))

    def test_add_element_method_with_integers(self):
        self.assertEqual([1, 2, 3], self.integers_list.get_data())
        self.integers_list.add(4)
        self.assertEqual([1, 2, 3, 4], self.integers_list.get_data())

    def test_remove_index_method_with_index_out_of_range_raises_error(self):
        with self.assertRaises(IndexError) as ex:
            self.integers_list.remove_index(5)

        self.assertEqual("Index is out of range", str(ex.exception))

    def test_remove_index_method_with_index_in_range(self):
        self.assertEqual([1, 2, 3], self.integers_list.get_data())
        self.integers_list.remove_index(1)
        self.assertEqual([1, 3], self.integers_list.get_data())

    def test_get_index_with_index_out_of_range(self):
        with self.assertRaises(IndexError) as ex:
            self.integers_list.get(3)
        self.assertEqual("Index is out of range", str(ex.exception))

    def test_get_index_with_index_in_range(self):
        result = self.integers_list.get(2)
        self.assertEqual(3, result)

    def test_insert_method_with_index_oy_of_range(self):
        with self.assertRaises(IndexError) as ex:
            self.integers_list.insert(3, 5)
        self.assertEqual("Index is out of range", str(ex.exception))

    def test_insert_method_with_not_integer_element(self):
        with self.assertRaises(ValueError) as ex:
            self.integers_list.insert(1, 'a')
        self.assertEqual("Element is not Integer", str(ex.exception))

    def test_insert_method_with_integer_and_correct_index(self):
        self.assertEqual([1, 2, 3], self.integers_list.get_data())
        self.integers_list.insert(1, 7)
        self.assertEqual([1, 7, 2, 3], self.integers_list.get_data())

    def test_get_biggest_method_correct_functionality(self):
        result = self.integers_list.get_biggest()
        self.assertEqual(3, result)

    def test_get_index_method_correct_functionality(self):
        result = self.integers_list.get_index(3)
        self.assertEqual(2, result)


if __name__ == "__main__":
    unittest.main()
