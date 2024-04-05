class dictionary_iter:
    def __init__(self, dictionary):
        self.dictionary = dictionary
        self.index = -1
        self.dict_list = list(dictionary.keys())

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == len(self.dictionary)-1:
            raise StopIteration
        self.index += 1
        return self.dict_list[self.index], self.dictionary[self.dict_list[self.index]]


result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)

print()

result = dictionary_iter({"name": "Peter", "age": 24})
for x in result:
    print(x)