from project.animal import Animal


class Dog(Animal):

    @property
    def sound(self):
        return "Woof!"
