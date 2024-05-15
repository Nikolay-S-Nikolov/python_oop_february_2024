from typing import List

from project.horse_race import HorseRace
from project.horse_specification.appaloosa import Appaloosa
from project.horse_specification.thoroughbred import Thoroughbred
from project.jockey import Jockey


class HorseRaceApp:
    def __init__(self):
        self.horses: List[Appaloosa or Thoroughbred] = []
        self.jockeys: List[Jockey] = []
        self.horse_races: List[HorseRace] = []

    def add_horse(self, horse_type: str, horse_name: str, horse_speed: int):
        valid_horse_types = {'Appaloosa': Appaloosa, 'Thoroughbred': Thoroughbred}
        if horse_name in [h.name for h in self.horses]:
            raise Exception(f"Horse {horse_name} has been already added!")

        if horse_type in valid_horse_types:
            new_horse = valid_horse_types[horse_type](horse_name, horse_speed)
            self.horses.append(new_horse)
            return f"{horse_type} horse {horse_name} is added."
        pass

    def add_jockey(self, jockey_name: str, age: int):
        if jockey_name in [j.name for j in self.jockeys]:
            raise Exception(f"Jockey {jockey_name} has been already added!")
        new_jockey = Jockey(jockey_name, age)
        self.jockeys.append(new_jockey)
        return f"Jockey {jockey_name} is added."

    def create_horse_race(self, race_type: str):
        if race_type in [t.race_type for t in self.horse_races]:
            raise Exception(f"Race {race_type} has been already created!")
        new_race = HorseRace(race_type)
        self.horse_races.append(new_race)
        return f"Race {race_type} is created."

    def add_horse_to_jockey(self, jockey_name: str, horse_type: str):
        horse_types = {'Appaloosa': Appaloosa, 'Thoroughbred': Thoroughbred}

        try:
            jockey = next(filter(lambda j: j.name == jockey_name, self.jockeys))

        except StopIteration:
            raise Exception(f"Jockey {jockey_name} could not be found!")
        if jockey.horse:
            return f"Jockey {jockey_name} already has a horse."

        try:
            # filter horses of that type and the one that are not taken
            horse = next(filter(
                lambda h: (horse_types[horse_type] == type(h) and h.is_taken == False
                           ), reversed(self.horses)))
        except StopIteration:
            raise Exception(f"Horse breed {horse_type} could not be found!")

        horse.is_taken = True
        jockey.horse = horse
        return f"Jockey {jockey_name} will ride the horse {horse.name}."

    def add_jockey_to_horse_race(self, race_type: str, jockey_name: str):
        try:
            race = next(filter(lambda r: r.race_type == race_type, self.horse_races))
        except StopIteration:
            raise Exception(f"Race {race_type} could not be found!")

        try:
            jockey = next(filter(lambda j: j.name == jockey_name, self.jockeys))

        except StopIteration:
            raise Exception(f"Jockey {jockey_name} could not be found!")

        if not jockey.horse:
            raise Exception(f"Jockey {jockey_name} cannot race without a horse!")

        if jockey in race.jockeys:
            return f"Jockey {jockey_name} has been already added to the {race_type} race."

        # for existing_races in self.horse_races:
        #     if jockey in existing_races.jockeys:
        #         return f"Jockey {jockey_name} has been already added to the {race_type} race."
        # jockey_participating_in_race = [r for r in self.horse_races if jockey in r.jockeys]
        # if jockey_participating_in_race:
        #     return f"Jockey {jockey_name} has been already added to the {race_type} race."
        race.jockeys.append(jockey)
        return f"Jockey {jockey_name} added to the {race_type} race."

    def start_horse_race(self, race_type: str):
        try:
            race = next(filter(lambda r: r.race_type == race_type, self.horse_races))
        except StopIteration:
            raise Exception(f"Race {race_type} could not be found!")

        if len(race.jockeys) < 2:
            raise Exception(f"Horse race {race_type} needs at least two participants!")

        winner = list(sorted(race.jockeys, key=lambda x: x.horse.speed, reverse=True))[0]
        return f"The winner of the {race_type} race, with a speed" \
               f" of {winner.horse.speed}km/h is {winner.name}! Winner's horse: {winner.horse.name}."
