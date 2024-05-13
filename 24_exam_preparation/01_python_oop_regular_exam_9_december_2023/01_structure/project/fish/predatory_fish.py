from project.fish.base_fish import BaseFish


class PredatoryFish(BaseFish):
    TIME_TO_CATCH = 90

    @property
    def time_to_catch(self):
        return self.TIME_TO_CATCH
