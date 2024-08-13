from project.soccer_player import SoccerPlayer
from unittest import TestCase, main


class TestSoccerPlayer(TestCase):
    def setUp(self) -> None:
        self.player = SoccerPlayer("Ronaldo", 16, 10, "PSG")

    def test_correct_init(self):
        self.assertEqual("Ronaldo", self.player.name)
        self.assertEqual(16, self.player.age)
        self.assertEqual(10, self.player.goals)
        self.assertEqual("PSG", self.player.team)
        self.assertEqual({}, self.player.achievements)
        self.assertEqual(
            ['Barcelona', 'Real Madrid', 'Manchester United', 'Juventus', 'PSG'], self.player._VALID_TEAMS)

    def test_name_setter_return_message(self):
        with self.assertRaises(ValueError) as ve:
            self.player.name = 'Gogo'

        self.assertEqual("Name should be more than 5 symbols!", str(ve.exception))

        with self.assertRaises(ValueError) as ve:
            self.player.name = 'Gogos'

        self.assertEqual("Name should be more than 5 symbols!", str(ve.exception))

    def test_age_setter_return_correct_message(self):
        with self.assertRaises(ValueError) as ve:
            self.player.age = 15

        self.assertEqual("Players must be at least 16 years of age!", str(ve.exception))

    def test_goal_setter_returns_correct_data(self):
        self.assertEqual(10, self.player.goals)
        self.player.goals = -1
        self.assertEqual(0, self.player.goals)

    def test_team_setter_returns_correct_error_message(self):
        with self.assertRaises(ValueError) as ve:
            self.player.team = "Levski"
        expected = "Team must be one of the following: Barcelona, Real Madrid, Manchester United, Juventus, PSG!"
        self.assertEqual(expected, str(ve.exception))

    def test_change_team_returns_invalid_team_message(self):
        self.assertEqual("PSG", self.player.team)

        self.assertEqual("Invalid team name!", self.player.change_team('Levski'))
        self.assertEqual("PSG", self.player.team)

    def test_change_team_with_valid_team_returns_correct_message(self):
        self.assertEqual("PSG", self.player.team)
        for team in ['Barcelona', 'Real Madrid', 'Manchester United', 'Juventus', 'PSG']:
            self.assertEqual("Team successfully changed!", self.player.change_team(team))
            self.assertEqual(team, self.player.team)

    def test_add_new_achievement_returns_correct_message(self):
        expected = "Ball Carrier has been successfully added to the achievements collection!"
        self.assertEqual(expected, self.player.add_new_achievement('Ball Carrier'))
        self.assertEqual({'Ball Carrier': 1}, self.player.achievements)
        self.assertEqual(expected, self.player.add_new_achievement('Ball Carrier'))
        self.assertEqual({'Ball Carrier': 2}, self.player.achievements)

        expected = "Bicycle Kick has been successfully added to the achievements collection!"
        self.assertEqual(expected, self.player.add_new_achievement('Bicycle Kick'))
        self.assertEqual({'Ball Carrier': 2, 'Bicycle Kick': 1}, self.player.achievements)

    def test_lt_return_all_messages_correctly(self):
        other = SoccerPlayer("Messsi", 20, 0, "Juventus")
        expected = 'Ronaldo is a better goal scorer than Messsi.'
        self.assertEqual(expected, self.player<other)
        other = SoccerPlayer("Messsi", 20, 11, "Juventus")
        expected = "Messsi is a top goal scorer! S/he scored more than Ronaldo."
        self.assertEqual(expected, self.player<other)

        other = SoccerPlayer("Messsi", 20, 10, "Juventus")
        expected = "Ronaldo is a better goal scorer than Messsi."
        self.assertEqual(expected, self.player < other)




if __name__ == "__main__":
    main()
