from unittest import TestCase, main

from project.tennis_player import TennisPlayer


class TestTennisPlayer(TestCase):
    def setUp(self) -> None:
        self.player = TennisPlayer('Nadal', 18, 22.0)

    def test_constructor_proper_init(self):
        self.assertEqual('Nadal', self.player.name)
        self.assertEqual(18, self.player.age)
        self.assertEqual(22, self.player.points)
        self.assertEqual([], self.player.wins)

    def test_name_setter_with_name_less_than_2_symbols_raise_value_error(self):
        with self.assertRaises(ValueError) as ve:
            TennisPlayer('GD', 30, 22.0)
        self.assertEqual("Name should be more than 2 symbols!", str(ve.exception))
        with self.assertRaises(ValueError) as ve:
            TennisPlayer('G', 30, 22.0)
        self.assertEqual("Name should be more than 2 symbols!", str(ve.exception))
        with self.assertRaises(ValueError) as ve:
            self.player.name = ''
        self.assertEqual("Name should be more than 2 symbols!", str(ve.exception))
        self.assertEqual('Nadal', self.player.name)

    def test_age_setter_with_age_less_than_18_raise_value_error(self):
        with self.assertRaises(ValueError) as ve:
            TennisPlayer('Federer', 17, 22.0)
        self.assertEqual("Players must be at least 18 years of age!", str(ve.exception))
        with self.assertRaises(ValueError) as ve:
            self.player.age = 16
        self.assertEqual("Players must be at least 18 years of age!", str(ve.exception))
        self.assertEqual(18, self.player.age)

    def test_add_new_win_with_tournament_not_in_list_(self):
        self.assertEqual([], self.player.wins)
        self.player.add_new_win('Sofia')
        self.assertEqual(['Sofia'], self.player.wins)
        self.player.add_new_win('Marseille')
        self.assertEqual(['Sofia', 'Marseille'], self.player.wins)

    def test_add_new_win_with_tournament_already_in_list_return_correct_message(self):
        self.assertEqual([], self.player.wins)
        self.player.add_new_win('Sofia')
        self.assertEqual(['Sofia'], self.player.wins)
        self.player.add_new_win('Marseille')
        self.assertEqual(['Sofia', 'Marseille'], self.player.wins)
        self.assertEqual("Sofia has been already added to the list of wins!", self.player.add_new_win('Sofia'))
        self.assertEqual(['Sofia', 'Marseille'], self.player.wins)

    def test__lt__with_points_smaller_than_other_return_correct_message(self):
        expected = 'Federer is a top seeded player and he/she is better than Nadal'
        self.assertEqual(expected, self.player.__lt__(TennisPlayer('Federer', 33, 40.0)))
        self.assertEqual(expected, self.player < TennisPlayer('Federer', 33, 40.0))
        self.assertEqual(expected, self.player.__lt__(TennisPlayer('Federer', 33, 40.0)))

    def test__lt__with_points_bigger_or_equal_than_other_return_correct_message(self):
        expected = 'Nadal is a better player than Federer'
        self.assertEqual(expected, self.player.__lt__(TennisPlayer('Federer', 33, 18.0)))
        self.assertEqual(expected, self.player < TennisPlayer('Federer', 33, 18))
        self.assertEqual(expected, self.player.__lt__(TennisPlayer('Federer', 33, 22.0)))
        self.assertEqual(expected, self.player < TennisPlayer('Federer', 33, 22))

    def test__str__method_return_correct_message(self):
        self.player.add_new_win('Sofia')
        self.player.add_new_win('Marseille')
        expected = f"Tennis Player: Nadal\n" \
                   f"Age: 18\n" \
                   f"Points: 22.0\n" \
                   f"Tournaments won: Sofia, Marseille"
        self.assertEqual(expected, str(self.player))


if __name__ == '__main__':
    main()
