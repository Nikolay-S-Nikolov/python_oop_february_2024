from abc import ABC, abstractmethod


class Animal(ABC):

    @property
    @abstractmethod
    def sound(self):
        ...

    def animal_sound(self):
        return self.sound

    def __repr__(self):
        return type(self).__name__


class Cat(Animal):

    @property
    def sound(self):
        return "meow"


class Dog(Animal):

    @property
    def sound(self):
        return 'woof-woof'


class Chicken(Animal):

    @property
    def sound(self):
        return 'cluck'


def animal_sound(*animals_list):
    for animal in animals_list:
        print(animal.animal_sound())


animals = Cat(), Dog(), Chicken()
print(animals)
animal_sound(*animals)
