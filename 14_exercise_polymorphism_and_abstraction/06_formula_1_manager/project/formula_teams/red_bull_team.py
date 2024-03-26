from project.formula_teams.formula_team import FormulaTeam


class RedBullTeam(FormulaTeam):

    @property
    def sponsor_money_per_position(self):
        return {1: 1_520_000, 2: 820_000, 3: 20_000, 4: 20_000, 5: 20_000, 6: 20_000, 7: 20_000,
                8: 20000, 9: 10_000, 10: 10_000}

    @property
    def expenses_per_race(self):
        return 250_000
