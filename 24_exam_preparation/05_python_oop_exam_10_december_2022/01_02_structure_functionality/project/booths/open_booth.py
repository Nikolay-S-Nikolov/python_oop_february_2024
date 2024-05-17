from project.booths.booth import Booth


class OpenBooth(Booth):
    PRICE_PER_PERSON_TO_RESERVE = 2.5

    def reserve(self, number_of_people: int):
        self.price_for_reservation = number_of_people * self.PRICE_PER_PERSON_TO_RESERVE
        self.is_reserved = True
