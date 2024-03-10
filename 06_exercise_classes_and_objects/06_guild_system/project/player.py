class Player:
    def __init__(self, name: str, hp: int, mp: int):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.skills = {}
        self.guild = "Unaffiliated"

    def add_skill(self, skill_name: str, mana_cost: int) -> str:

        if self.skills.get(skill_name, 0):

            return "Skill already added"

        self.skills[skill_name] = mana_cost

        return f"Skill {skill_name} added to the collection of the player {self.name}"

    def player_info(self) -> str:

        skills = f'\n'.join(f"==={k} - {v}" for k, v in self.skills.items())

        return f"Name: {self.name}\nGuild: {self.guild}\nHP: {self.hp}\nMP: {self.mp}\n{skills}"
