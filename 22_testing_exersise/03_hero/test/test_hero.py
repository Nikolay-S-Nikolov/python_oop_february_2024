from unittest import TestCase, main

from project.hero import Hero


class TestHero(TestCase):
    def setUp(self) -> None:
        self.hero = Hero("User", 5, 10, 15)

    def test_constructor_init_for_correct_setup(self):
        self.assertEqual("User", self.hero.username)
        self.assertEqual(5, self.hero.level)
        self.assertEqual(10, self.hero.health)
        self.assertEqual(15, self.hero.damage)

    def test_battle_method_raise_fight_yourself_message(self):
        with self.assertRaises(Exception) as ex:
            self.hero.battle(Hero("User", 5, 10, 15))
        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_battle_method_with_health_0_raise_rest_message(self):
        self.hero.health = 0
        with self.assertRaises(Exception) as ex:
            self.hero.battle(Hero("Test Hero", 5, 10, 15))
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ex.exception))

    def test_battle_method_with_enemy_health_0_raise_rest_message(self):
        with self.assertRaises(Exception) as ex:
            self.hero.battle(Hero("Test Hero", 5, 0, 15))
        self.assertEqual("You cannot fight Test Hero. He needs to rest", str(ex.exception))

    def test_battle_method_draw_result_message(self):
        self.hero.health = 75
        expected = self.hero.battle(Hero("Test Hero", 5, 75, 15))
        self.assertEqual("Draw", expected)

    def test_battle_method_you_win_result_message(self):
        self.hero.health = 85
        expected = self.hero.battle(Hero("Test Hero", 5, 70, 15))
        self.assertEqual("You win", expected)

    def test_battle_method_you_win_correct_level_health_damage_value(self):
        self.hero.health = 85
        enemy = Hero("Test Hero", 5, 70, 15)
        self.hero.battle(enemy)
        self.assertEqual(6, self.hero.level)
        self.assertEqual(15, self.hero.health)
        self.assertEqual(20, self.hero.damage)
        self.assertEqual(-5, enemy.health)

    def test_battle_method_you_lose_result_message(self):
        self.hero.health = 75
        expected = self.hero.battle(Hero("Test Hero", 5, 76, 15))
        self.assertEqual("You lose", expected)

    def test_battle_method_you_lose_correct_level_health_damage_value(self):
        self.hero.health = 75
        enemy = Hero("Test Hero", 5, 76, 15)
        self.hero.battle(enemy)
        self.assertEqual(6, enemy.level)
        self.assertEqual(6, enemy.health)
        self.assertEqual(20, enemy.damage)
        self.assertEqual(0, self.hero.health)

    def test__str__method_for_correct_message(self):
        expected = str(self.hero)
        self.assertEqual("Hero User: 5 lvl\nHealth: 10\nDamage: 15\n", expected)


if __name__ == "__main__":
    main()
