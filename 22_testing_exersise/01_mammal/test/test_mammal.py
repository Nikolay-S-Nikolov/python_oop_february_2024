from unittest import TestCase, main

from project.mammal import Mammal


class TestMammal(TestCase):
    def setUp(self) -> None:
        self.mammal = Mammal('Ralph', "dog", "bark")

    def test_constructor(self):
        self.assertEqual('Ralph', self.mammal.name)
        self.assertEqual('dog', self.mammal.type)
        self.assertEqual('bark', self.mammal.sound)

    def test_make_sound_method_for_correct_message(self):
        expected = self.mammal.make_sound()
        self.assertEqual("Ralph makes bark", expected)

    def test_get_kingdom_method_return_kingdom(self):
        self.assertEqual('animals', self.mammal.get_kingdom())

    def test_info_method_returns_correct_massage(self):
        expected = self.mammal.info()
        self.assertEqual("Ralph is of type dog",expected)


if __name__ == "__main__":
    main()
