from project.fish.base_fish import BaseFish


class DeepSeaFish(BaseFish):
    TIME_TO_CATCH = 180

    @property
    def time_to_catch(self):
        return self.TIME_TO_CATCH
