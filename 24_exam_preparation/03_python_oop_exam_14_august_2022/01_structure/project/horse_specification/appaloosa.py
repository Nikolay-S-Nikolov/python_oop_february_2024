from project.horse_specification.horse import Horse


class Appaloosa(Horse):
    MAXIMUM_SPEED = 120
    SPEED_INCREASED_WHEN_TRAINED = 2

    @property
    def maximum_speed(self):
        return self.MAXIMUM_SPEED

    @property
    def speed_increased_when_trained(self):
        return self.SPEED_INCREASED_WHEN_TRAINED

