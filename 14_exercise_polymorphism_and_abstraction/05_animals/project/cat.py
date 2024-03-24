from project.animal import Animal


class Cat(Animal):

    @property
    def sound(self):
        return "Meow meow!"
