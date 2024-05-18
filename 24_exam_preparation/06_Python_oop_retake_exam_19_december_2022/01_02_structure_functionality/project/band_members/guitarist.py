from project.band_members.musician import Musician


class Guitarist(Musician):
    SKILL_LIST = ["play metal", "play rock", "play jazz"]

    @property
    def skills_list(self):
        return self.SKILL_LIST


