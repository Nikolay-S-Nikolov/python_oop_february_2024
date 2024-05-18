from typing import List

from project.band import Band
from project.band_members.drummer import Drummer
from project.band_members.guitarist import Guitarist
from project.band_members.musician import Musician
from project.band_members.singer import Singer
from project.concert import Concert


class ConcertTrackerApp:
    def __init__(self):
        self.bands: List[Band] = []
        self.musicians: List[Singer or Guitarist or Drummer] = []
        self.concerts: List[Concert] = []

    def create_musician(self, musician_type: str, name: str, age: int):
        valid_musicians = {"Guitarist": Guitarist, "Drummer": Drummer, "Singer": Singer}
        if musician_type not in valid_musicians:
            raise ValueError("Invalid musician type!")
        if name in [m.name for m in self.musicians]:
            raise Exception(f"{name} is already a musician!")
        new_musician = valid_musicians[musician_type](name, age)
        self.musicians.append(new_musician)
        return f"{name} is now a {musician_type}."

    def create_band(self, name: str):
        if name in [b.name for b in self.bands]:
            raise Exception(f"{name} band is already created!")
        new_band = Band(name)
        self.bands.append(new_band)
        return f"{name} was created."

    def create_concert(self, genre: str, audience: int, ticket_price: float, expenses: float, place: str):
        if place in [c.place for c in self.concerts]:
            concert = next(filter(lambda c: c.place == place, self.concerts))
            raise Exception(f"{place} is already registered for {concert.genre} concert!")
        new_concert = Concert(genre, audience, ticket_price, expenses, place)
        self.concerts.append(new_concert)
        return f"{genre} concert in {place} was added."

    def add_musician_to_band(self, musician_name: str, band_name: str):
        try:
            musician = next(filter(lambda m: m.name == musician_name, self.musicians))
        except StopIteration:
            raise Exception(f"{musician_name} isn't a musician!")

        try:
            band = next(filter(lambda b: b.name == band_name, self.bands))
        except StopIteration:
            raise Exception(f"{band_name} isn't a band!")

        band.members.append(musician)
        return f"{musician_name} was added to {band_name}."

    def remove_musician_from_band(self, musician_name: str, band_name: str):
        try:
            band = next(filter(lambda b: b.name == band_name, self.bands))
        except StopIteration:
            raise Exception(f"{band_name} isn't a band!")

        try:
            musician = next(filter(lambda m: (m.name == musician_name and m in band.members), self.musicians))
        except StopIteration:
            raise Exception(f"{musician_name} isn't a member of {band_name}!")

        band.members.remove(musician)
        return f"{musician_name} was removed from {band_name}."

    def start_concert(self, concert_place: str, band_name: str):
        band = [b for b in self.bands if b.name == band_name][0]
        guitarist = self.check_band_members_type(band, Guitarist)
        drummer = self.check_band_members_type(band, Drummer)
        singer = self.check_band_members_type(band, Singer)
        if not guitarist or not drummer or not singer:
            raise Exception(f"{band_name} can't start the concert because it doesn't have enough members!")
        concert = [c for c in self.concerts if c.place == concert_place][0]
        if concert.genre == "Rock":
            drummer_is_skilled = self.check_musician_for_skill(drummer, "play the drums with drumsticks")
            singer_is_skilled = self.check_musician_for_skill(singer, "sing high pitch notes")
            guitarist_is_skilled = self.check_musician_for_skill(guitarist, "play rock")

        elif concert.genre == "Metal":
            drummer_is_skilled = self.check_musician_for_skill(drummer, "play the drums with drumsticks")
            singer_is_skilled = self.check_musician_for_skill(singer, "sing low pitch notes")
            guitarist_is_skilled = self.check_musician_for_skill(guitarist, "play metal")

        else:
            drummer_is_skilled = self.check_musician_for_skill(drummer, "play the drums with drum brushes")
            singer_is_skilled = self.check_musician_for_skill(singer, "sing high pitch notes")
            if singer_is_skilled:
                singer_is_skilled = self.check_musician_for_skill(singer, "sing low pitch notes")
            guitarist_is_skilled = self.check_musician_for_skill(guitarist, "play jazz")
        if not drummer_is_skilled or not singer_is_skilled or not guitarist_is_skilled:
            raise Exception(f"The {band_name} band is not ready to play at the concert!")

        profit = (concert.audience*concert.ticket_price) - concert.expenses
        return f"{band_name} gained {profit:.2f}$ from the {concert.genre} concert in {concert.place}."

    @staticmethod
    def check_band_members_type(band: Band, type_musician: Singer or Guitarist or Drummer):
        try:
            _musician = next(filter(lambda m: (type(m) == type_musician), band.members))
        except StopIteration:
            return None
        return _musician

    @staticmethod
    def check_musician_for_skill(musician: Singer or Guitarist or Drummer, skill: str):
        if skill in musician.skills:
            return True
        return False
