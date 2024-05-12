from unittest import TestCase, main

from custom_list import CustomList


class TestCustomList(TestCase):
    def setUp(self) -> None:
        self.ll = CustomList()

    def test_correct_init(self):
        self.assertEqual([], self.ll._CustomList__values)
        self.assertEqual([], list(self.ll))
        self.assertEqual("[]", str(self.ll))

    def test_append__when_list_is_empty_expect_one_value_new_list(self):
        test = CustomList()
        value = 1
        result = test.append(value)

        self.assertListEqual([value], list(test))
        self.assertListEqual([value], result)

    def test_append__when_list_is_not_empty_expect_new_value_added_to_list(self):
        test = CustomList()
        values = [1, 2, 3]
        result = [test.append(v) for v in values]

        self.assertListEqual(
            values,
            list(test)
        )
        self.assertListEqual(
            [[1], [1, 2], [1, 2, 3]],
            result
        )

    def test_remove__when_index_is_in_range_returns_correct_value(self):
        [self.ll.append(x) for x in [0, 1, 2, 3, 4, 5, 6]]
        self.assertEqual([0, 1, 2, 3, 4, 5, 6], self.ll._CustomList__values)
        self.assertEqual([0, 1, 2, 3, 4, 5, 6], list(self.ll))
        self.assertEqual(6, self.ll.remove(6))
        self.assertEqual(0, self.ll.remove(-6))

    def test_remove__when_index_is_invalid_raise_index_error(self):
        [self.ll.append(x) for x in [0, 1, 2, 3, 4, 5, 6]]
        self.assertEqual([0, 1, 2, 3, 4, 5, 6], list(self.ll))
        with self.assertRaises(IndexError) as ie:
            self.ll.remove(7)
        self.assertEqual("index 7 is out of range", str(ie.exception))
        self.assertEqual([0, 1, 2, 3, 4, 5, 6], list(self.ll))
        with self.assertRaises(IndexError) as ie:
            self.ll.remove(-8)
        self.assertEqual("index -8 is out of range", str(ie.exception))
        self.assertEqual([0, 1, 2, 3, 4, 5, 6], list(self.ll))

    def test_get__when_index_is_in_range_returns_correct_value(self):
        [self.ll.append(x) for x in [0, 1, 2, 3, 4, 5, 6]]
        self.assertEqual(6, self.ll.get(6))
        self.assertEqual(0, self.ll.get(-7))

    def test_get__when_index_is_invalid_raise_index_error(self):
        [self.ll.append(x) for x in [0, 1, 2, 3, 4, 5, 6]]
        with self.assertRaises(IndexError) as ie:
            self.ll.get(7)
        self.assertEqual("index 7 is out of range", str(ie.exception))

        with self.assertRaises(IndexError) as ie:
            self.ll.get(-8)
        self.assertEqual("index -8 is out of range", str(ie.exception))

    def test_extend__with_list_return_extended_list(self):
        self.assertEqual([], list(self.ll))
        self.assertEqual([1, 2], self.ll.extend([1, 2]))
        self.assertEqual([1, 2], list(self.ll))

    def test_extend__with_tuple_return_extended_list(self):
        self.assertEqual([], list(self.ll))
        self.assertEqual([1, 2], self.ll.extend((1, 2)))
        self.assertEqual([1, 2], list(self.ll))

    def test_extend__with_set_return_extended_list(self):
        self.assertEqual([], list(self.ll))
        self.assertEqual([1, 2], self.ll.extend({1, 2}))
        self.assertEqual([1, 2], list(self.ll))

    def test_extend__with_tuple_set_list_and_another_iterable_return_extended_list(self):
        self.assertEqual([], list(self.ll))
        self.assertEqual([1, 2], self.ll.extend(x for x in range(1, 3)))
        self.assertEqual([1, 2], list(self.ll))

    def test_insert__when_index_is_invalid_raise_index_error(self):
        [self.ll.append(x) for x in [0, 1, 2, 3, 4, 5, 6]]
        with self.assertRaises(IndexError) as ie:
            self.ll.insert(8, 9)
        self.assertEqual("index 8 is out of range", str(ie.exception))

        with self.assertRaises(IndexError) as ie:
            self.ll.insert(-9, 9)
        self.assertEqual("index -9 is out of range", str(ie.exception))

    def test_insert__when_index_is_in_range_returns_correct_value(self):
        [self.ll.append(x) for x in [0, 1, 2, 3, 4, 5, 6]]
        self.assertEqual([0, 1, 2, 3, 4, 5, 6], self.ll._CustomList__values)
        self.assertEqual([0, 1, 2, 3, 4, 5, 6, 9], self.ll.insert(7, 9))
        self.assertEqual([0, 1, 2, 3, 4, 5, 6, 9], self.ll._CustomList__values)
        self.assertEqual([9, 0, 1, 2, 3, 4, 5, 6, 9], self.ll.insert(-8, 9))
        self.assertEqual([9, 0, 1, 2, 3, 4, 5, 6, 9], self.ll._CustomList__values)

    def test_pop__when_list_is_empty_return_index_error(self):
        with self.assertRaises(IndexError) as ie:
            self.ll.pop()
        self.assertEqual("You are trying to pop from empty list", str(ie.exception))

    def test_pop__when_list_is_not_empty_return_last_list_item(self):
        [self.ll.append(x) for x in [0, 1, 2, 3, 4, 5, 6]]
        self.assertEqual([0, 1, 2, 3, 4, 5, 6], self.ll._CustomList__values)
        self.assertEqual([0, 1, 2, 3, 4, 5, 6], list(self.ll))
        self.assertEqual(6, self.ll.pop())
        self.assertEqual([0, 1, 2, 3, 4, 5], list(self.ll))
        self.assertEqual(5, self.ll.pop())
        self.assertEqual([0, 1, 2, 3, 4], list(self.ll))

    def test_clear_when_list_is_empty_and_when_not(self):
        self.assertEqual([], list(self.ll))
        self.ll.clear()
        self.assertEqual([], list(self.ll))
        [self.ll.append(x) for x in [0, 1, 2, 3, 4, 5, 6]]
        self.assertEqual([0, 1, 2, 3, 4, 5, 6], list(self.ll))

        self.ll.clear()
        self.assertEqual([], list(self.ll))

    def test_index__when_list_is_empty_raise_index_error(self):
        self.assertEqual([], list(self.ll))
        with self.assertRaises(IndexError) as ie:
            self.ll.index(0)
        self.assertEqual("List is empty", str(ie.exception))

    def test_index__when_value_is_not_in_list_raise_value_error(self):
        [self.ll.append(x) for x in [0, 1, 2, 3, 4, 5, 6]]
        self.assertEqual([0, 1, 2, 3, 4, 5, 6], list(self.ll))
        with self.assertRaises(ValueError) as ve:
            self.ll.index(9)
        self.assertEqual("Value 9 is not in list", str(ve.exception))

    def test_index__when_value_correct_returns_correct_index(self):
        [self.ll.append(x) for x in [0, 1, 2, 3, 4, 5, 6]]
        self.assertEqual([0, 1, 2, 3, 4, 5, 6], list(self.ll))
        self.assertEqual(3, self.ll.index(3))
        self.assertEqual(0, self.ll.index(0))

    def test_count__when_value_not_in_list_returns_0(self):
        self.assertEqual(0, self.ll.count(1))
        [self.ll.append(x) for x in [0, 1, 2, 3, 4, 5, 6]]
        self.assertEqual(0, self.ll.count(9))

    def test_count__when_value_in_list_one_and_more_times_returns_correct(self):
        [self.ll.append(x) for x in [1, 2, 4, 1, 4, 1, 1]]
        self.assertEqual(1, self.ll.count(2))
        self.assertEqual(4, self.ll.count(1))
        self.assertEqual(2, self.ll.count(4))

    def test_reverse__when_list_is_empty(self):
        self.assertEqual([], list(self.ll))
        first_list = list(self.ll)
        second_list = self.ll.reverse()
        self.assertEqual([], second_list)
        result = (id(first_list) == id(second_list))
        self.assertFalse(result)

    def test_reverse__when_list_have_values(self):
        [self.ll.append(x) for x in [0, 1, 2, 3, 4, 5, 6]]
        first_list = list(self.ll)
        second_list = self.ll.reverse()
        self.assertEqual([6, 5, 4, 3, 2, 1, 0], second_list)
        result = (id(first_list) == id(second_list))
        self.assertFalse(result)

    def test_copy__when_list_is_empty(self):
        self.assertEqual([], list(self.ll))
        first_list = list(self.ll)
        second_list = self.ll.copy()
        self.assertEqual([], second_list)
        result = (id(first_list) == id(second_list))
        self.assertFalse(result)

    def test_copy__when_list_have_values(self):
        [self.ll.append(x) for x in [0, 1, 2, 3, 4, 5, 6]]
        first_list = list(self.ll)
        second_list = self.ll.copy()
        self.assertEqual([0, 1, 2, 3, 4, 5, 6], second_list)
        result = (id(first_list) == id(second_list))
        self.assertFalse(result)

    def test_size__return_correct_value(self):
        self.assertEqual(0, self.ll.size())
        [self.ll.append(x) for x in [0, 1, 2, 3, 4, 5, 6]]
        self.assertEqual(7, self.ll.size())

    def test_add_first__inserts_value_in_beginning_of_the_list(self):
        self.ll.add_first(1)
        self.assertEqual([1], list(self.ll))
        self.ll.add_first(2)
        self.assertEqual([2, 1], list(self.ll))
        self.ll.add_first(3)
        self.assertEqual([3, 2, 1], list(self.ll))

    def test_dictionize__when_list_len_is_even_number(self):
        [self.ll.append(x) for x in [0, 1, 2, 3, 4, 5]]

        self.assertEqual({0: 1, 2: 3, 4: 5}, self.ll.dictionize())

    def test_dictionize__when_list_len_is_odd_number(self):
        [self.ll.append(x) for x in [0, 1, 2, 3, 4, 5, 6]]

        self.assertEqual({0: 1, 2: 3, 4: 5, 6: ' '}, self.ll.dictionize())

    def test_move__when_amount_is_negative_rise_index_error(self):
        [self.ll.append(x) for x in [0, 1, 2, 3, 4, 5, 6]]
        self.assertEqual([0, 1, 2, 3, 4, 5, 6], list(self.ll))
        with self.assertRaises(IndexError) as ie:
            self.ll.move(-1)
        self.assertEqual("Invalid move amount", str(ie.exception))

    def test_move__when_amount_is_bigger_or_equal_to_list_len_rise_index_error(self):
        [self.ll.append(x) for x in [0, 1, 2, 3, 4, 5, 6]]
        self.assertEqual([0, 1, 2, 3, 4, 5, 6], list(self.ll))
        with self.assertRaises(IndexError) as ie:
            self.ll.move(7)
        self.assertEqual("Invalid move amount", str(ie.exception))
        with self.assertRaises(IndexError) as ie:
            self.ll.move(8)
        self.assertEqual("Invalid move amount", str(ie.exception))

    def test_move__when_amount_is_zero_or_smaller_then_list_len_return_correct(self):
        [self.ll.append(x) for x in [0, 1, 2, 3, 4, 5, 6]]
        self.assertEqual([0, 1, 2, 3, 4, 5, 6], list(self.ll))
        self.assertEqual([0, 1, 2, 3, 4, 5, 6], self.ll.move(0))
        self.assertEqual([3, 4, 5, 6, 0, 1, 2], self.ll.move(3))

    def test_sum__when_values_are_digits_return_correct(self):
        [self.ll.append(x) for x in [0, 1, 2, 3, 4, 5, 6]]
        self.assertEqual(21, self.ll.sum())

    def test_sum__when_values_are_strings_return_correct(self):
        [self.ll.append(x) for x in ['apple', 'banana', 'strawberry', 'peach']]
        self.assertEqual(26, self.ll.sum())

    def test_sum__when_values_are_strings_and_numbers_return_correct(self):
        my_list = [0, False, 2, 'apple', 3, 'banana', 7, 'strawberry', 4, 'peach', 3, True]
        [self.ll.append(x) for x in my_list]
        self.assertEqual(46, self.ll.sum())

    def test_overbound__when_list_is_empty_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.ll.overbound()

        self.assertEqual('List is empty', str(ve.exception))

    def test_overbound__when_values_are_digits_return_correct_index(self):
        [self.ll.append(x) for x in [0, 1, 2, 3, 4, 5, 6]]
        self.assertEqual(6, self.ll.overbound())

    def test_overbound__when_values_are_strings_return_correct_index(self):
        [self.ll.append(x) for x in ['apple', 'banana', 'strawberry', 'peach']]
        self.assertEqual(2, self.ll.overbound())

    def test_overbound__when_values_mixed_types_return_correct(self):
        my_list = [0, False, 2, 'apple', 3, 'banana', 7, 'strawberry', 4, 'peach', 3, True]
        [self.ll.append(x) for x in my_list]
        self.assertEqual(7, self.ll.overbound())

    def test_underbound__when_list_is_empty_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.ll.underbound()

        self.assertEqual('List is empty', str(ve.exception))

    def test_underbound__when_values_are_digits_return_correct_index(self):
        [self.ll.append(x) for x in [0, 1, 2, 3, 4, 5, 6]]
        self.assertEqual(0, self.ll.underbound())

    def test_underbound__when_values_are_strings_return_correct_index(self):
        [self.ll.append(x) for x in ['apple', 'banana', 'strawberry', 'peach']]
        self.assertEqual(0, self.ll.underbound())

    def test_underbound__when_values_mixed_types_return_correct(self):
        my_list = ['apple', 3, 'banana', 7, False, 'strawberry', 4, 'peach', 3]
        [self.ll.append(x) for x in my_list]
        self.assertEqual(4, self.ll.underbound())
