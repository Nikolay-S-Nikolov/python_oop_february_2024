class take_skip:
    def __init__(self, step: int, count: int):
        self.count = count
        self.step = step
        self.value = 0 - step

    def __iter__(self):
        return self

    def __next__(self):
        self.value += self.step
        if self.value == self.count * self.step:
            self.value = 0
            raise StopIteration
        return self.value


numbers = take_skip(2, 6)
for number in numbers:
    print(number)
print()
numbers = take_skip(10, 5)
for number in numbers:
    print(number)
