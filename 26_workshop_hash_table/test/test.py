from unittest import TestCase, main

from hash_table import HashTable


class TestHashTable(TestCase):
    def setUp(self) -> None:
        self.table = HashTable()

    def test_correct_constructor_init(self):
        self.assertEqual(4, self.table._HashTable__max_capacity)
        self.assertEqual([None, None, None, None], self.table._HashTable__keys)
        self.assertEqual([None, None, None, None], self.table._HashTable__value)
        self.assertEqual(0, self.table._HashTable__length)

    def test__getitem__correct_data(self):
        self.table["Name"] = "Jhon"
        self.assertEqual("Jhon", self.table["Name"])

    def test__getitem__invalid_key_raises_key_error(self):
        with self.assertRaises(KeyError) as ke:
            result = self.table["test"]

        self.assertEqual("'test is not in the hash table'", str(ke.exception))

    def test_correct_override__setitem__(self):
        self.table["name"] = "Nikolay"
        self.table["name"] = "Ivan"
        self.assertEqual(1, len(self.table))
        self.assertEqual("Ivan", self.table["name"])

    def test_resize_when_len_reach_max_capacity(self):
        self.table["name"] = "Nikolay"
        self.table['age'] = 25
        self.table['is_pet_owner'] = True
        self.table['is_driver'] = False
        self.assertEqual(4, self.table._HashTable__max_capacity)
        self.table.add('can_fight', True)
        self.assertEqual(8, self.table._HashTable__max_capacity)

    def test_calc_index_when_collision_create_correct_index(self):
        self.table["name"] = "Nikolay"
        self.table['age'] = 25
        self.table['is_pet_owner'] = True
        self.assertEqual(['None:None', 'name:Nikolay', 'age:25', 'is_pet_owner:True'], [
            f"{self.table._HashTable__keys[i]}:{self.table._HashTable__value[i]}"
            for i in range(self.table._HashTable__max_capacity)
        ])
        self.assertEqual(0,self.table.calc_index("is sleeping"))

    def test__str__return_correct_message(self):
        self.table["name"] = "Nikolay"
        self.table["age"] = 44
        self.assertEqual("{name:Nikolay, age:44}", str(self.table))

    def test_add_method_correct_value_added(self):
        self.assertEqual("{}", str(self.table))
        self.table.add('test', 75)
        self.assertEqual("{test:75}", str(self.table))

    def test_get_method_returns_none_for_non_existing_key(self):
        self.assertEqual(None, self.table.get('name'))

    def test_get_method_returns_message_for_non_existing_key(self):
        self.assertEqual("Key is not in the hash table", self.table.get('name', "Key is not in the hash table"))

    def test_get_method_returns_value_of_key_for_existing_key(self):
        self.table["name"] = "Nikolay"
        self.table["age"] = 44
        self.assertEqual("Nikolay", self.table.get('name', "Key is not in the hash table"))



if __name__ == "__main__":
    main()
