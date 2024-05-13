from project.divers.base_diver import BaseDiver


class ScubaDiver(BaseDiver):
    OXYGEN_LEVEL = 540
    OXYGEN_REDUCED_WHEN_MISSED_FISH = 0.3

    @property
    def initial_oxygen_level(self):
        return self.OXYGEN_LEVEL

    @property
    def consumed_oxygen_percentage(self):
        return self.OXYGEN_REDUCED_WHEN_MISSED_FISH
