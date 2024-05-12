class CustomList:
    def __init__(self):
        self.__values = []

    def append(self, value):
        """
        Adds a value to the end of the list. Returns the list.
        """
        self.__values.append(value)
        return list(self)

    def remove(self, index):
        """
        Removes the value on the index. Returns the value removed.
        """
        self.check_index(index)

        return self.__values.pop(index)

    def get(self, index):
        """
        Returns the value on the index.
        """
        self.check_index(index)
        return self.__values[index]

    def extend(self, iterable):
        """
        Appends the iterable to the list. Returns the new list.
        """
        [self.append(i) for i in iterable]
        return list(self)

    def insert(self, index, value):
        """
        Adds the value on the specific index. Returns the list.
        """
        if index > len(self.__values) or index < (-len(self.__values) - 1):
            self.check_index(index)
        self.__values.insert(index, value)
        return list(self)

    def pop(self):
        """
        Removes the last value and returns it.
        """
        if not self.__values:
            raise IndexError("You are trying to pop from empty list")
        return self.__values.pop()

    def clear(self):
        """
        Removes all values, contained in the list.
        """
        self.__values.clear()

    def index(self, value):
        """
        Returns the index of the given value.
        """
        if not self.__values:
            raise IndexError("List is empty")

        if value not in self.__values:
            raise ValueError(f"Value {value} is not in list")
        return self.__values.index(value)

    def count(self, value):
        """
        Returns the number of times the value is contained in the list.
        """
        return self.__values.count(value)

    def reverse(self):
        """
        Returns the values of the list in reverse order.
        """
        new_list = CustomList()
        [new_list.__values.append(x) for x in self.__values[::-1]]
        return list(new_list)

    def copy(self):
        """
        Returns a copy of the list.
        """
        new_list = CustomList()
        [new_list.__values.append(x) for x in self.__values]
        return list(new_list)

    def size(self):
        """
        Returns the length of the list.
        """
        return len(self.__values)

    def add_first(self, value):
        """
        Adds the value at the beginning of the list
        """
        self.insert(0, value)

    def dictionize(self):
        """
         Returns the list as a dictionary: The keys will be
         each value on an even position and their values will be
         each value on an odd position. If the last value on an
         even position, its value will be " " (space)
        """
        list_dict = {}
        for idx in range(len(self.__values)):
            if idx % 2 == 0:
                list_dict[self.__values[idx]] = " "
            else:
                list_dict[self.__values[idx - 1]] = self.__values[idx]

        return list_dict

    def move(self, amount):
        """
        Move the first "amount" of values to the end of the list.
        Returns the list.
        """
        if len(self.__values) <= amount or amount < 0:
            raise IndexError("Invalid move amount")
        self.__values = self.__values[amount:] + self.__values[:amount]
        return list(self)

    def sum(self):
        """
        Returns the sum of the list. If the value is not a number,
        add the length of the value to the overall number.
        """
        sum_values = 0
        for v in self.__values:
            if isinstance(v, (int, float)):
                sum_values += v
            else:
                sum_values += len(str(v))
        return sum_values

    def overbound(self):
        """
        Returns the index of the biggest value.
        If the value is not a number, check its length.
        """
        if not self.__values:
            raise ValueError('List is empty')
        converted_list = [x if isinstance(x, (int, float)) else len(str(x)) for x in self.__values]
        return converted_list.index(max(converted_list))

    def underbound(self):
        """
        Returns the index of the smallest value.
        If the value is not a number, check its length.
        """
        if not self.__values:
            raise ValueError('List is empty')
        converted_list = [x if isinstance(x, (int, float)) else len(str(x)) for x in self.__values]
        return converted_list.index(min(converted_list))

    def check_index(self, index):
        """
        Check if the index is in range and if not rises IndexError.
        """
        try:
            self.__values[index]
        except IndexError:
            raise IndexError(f"index {index} is out of range")

    def __iter__(self):
        for value in self.__values:
            yield value

    def __str__(self):
        return '[' + ', '.join(str(x) for x in self.__values) + ']'



