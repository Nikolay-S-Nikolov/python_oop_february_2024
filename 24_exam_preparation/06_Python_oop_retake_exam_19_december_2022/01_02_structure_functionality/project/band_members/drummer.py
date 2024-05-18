from project.band_members.musician import Musician


class Drummer(Musician):
    SKILL_LIST = [
        "play the drums with drumsticks",
        "play the drums with drum brushes",
        "read sheet music"
    ]

    @property
    def skills_list(self):
        return self.SKILL_LIST
