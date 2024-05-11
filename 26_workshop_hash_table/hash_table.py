class HashTable:
    def __init__(self):
        self.__max_capacity = 4
        self.__keys = [None] * self.__max_capacity
        self.__value = [None] * self.__max_capacity
        self.__length = 0

    def add(self, key, value):
        self[key] = value

    def get(self, key, message=None):
        try:
            return self[key]
        except KeyError:
            return message

    def __getitem__(self, key):
        try:
            index = self.__keys.index(key)
            return self.__value[index]
        except ValueError:
            raise KeyError(f"{key} is not in the hash table")

    def __setitem__(self, key, value):
        try:
            idx = self.__keys.index(key)
            self.__value[idx] = value
            return
        except ValueError:
            pass

        if len(self) == self.__max_capacity:
            self.__resize()

        index = self.calc_index(key)
        self.__keys[index] = key
        self.__value[index] = value

    def __delitem__(self, key):
        idx = self.__keys.index(key)
        self.__keys[idx] = None
        self.__value[idx] = None
        self.__length -= 1

    def __resize(self):
        self.__keys = self.__keys + [None] * self.__max_capacity
        self.__value = self.__value + [None] * self.__max_capacity
        self.__max_capacity *= 2

    def calc_index(self, key):
        index = sum(ord(c) for c in str(key)) % self.__max_capacity

        index = self.get_index(index)
        self.__length += 1
        return index

    def get_index(self, index):
        while True:
            if self.__keys[index % self.__max_capacity] is None:
                return index % self.__max_capacity
            index += 1

    def __str__(self):
        result = []

        for i in range(self.__max_capacity):
            if self.__keys[i] is not None:
                result.append(f"{self.__keys[i]}:{self.__value[i]}")

        return '{' + ', '.join(result) + '}'

    def __len__(self):
        return self.__length


# table = HashTable()
#
# table["name"] = "Peter"
# table['age'] = 25
# table['is_pet_owner'] = True
# table['is_driver'] = False
# table.add('can_fight', True)
# print(table)
# table["age"] = 35
# print(table.get("is sleeping"))
# print(table)
# print(table.get("name"))
# print(table["age"])
# print(len(table))
# del table["age"]
# print(table)

def str_decorator(function):
    def wrapper(*args):
        cls, arg_1 = args[0], args[1]

        if len(args) > 2:
            arg_2 = args[2]
            if not isinstance(arg_1, str) or not isinstance(arg_2, str):
                raise ValueError("Use only strings")
            return function(cls, arg_1, arg_2)

        if not isinstance(arg_1, str):
            raise ValueError("Use only strings")
        return function(cls, arg_1)

    return wrapper


class StringHashTable(HashTable):

    @str_decorator
    def add(self, key, value):
        return super().add(key, value)

    @str_decorator
    def __setitem__(self, key, value):
        return super().__setitem__(key, value)


str_table = StringHashTable()
str_table.add("name", "Nikolay")
str_table['age'] = "25"
# str_table['age'] = 25
# str_table.add("age", 25)
print(str_table)
