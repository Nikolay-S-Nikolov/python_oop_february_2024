from project.formula_teams.formula_team import FormulaTeam


class MercedesTeam(FormulaTeam):

    @property
    def sponsor_money_per_position(self):
        return {1: 1_100_000, 2: 1_100_000, 3: 600_000, 4: 100_00, 5: 100_000, 6: 50_000,
                7: 50_000}

    @property
    def expenses_per_race(self):
        return 200_000
