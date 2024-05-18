from project.band_members.musician import Musician


class Singer(Musician):
    SKILL_LIST = ["sing high pitch notes", "sing low pitch notes"]

    @property
    def skills_list(self):
        return self.SKILL_LIST
