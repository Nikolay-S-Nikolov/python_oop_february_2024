from typing import List

from project.player import Player


class Guild:
    def __init__(self, name: str):
        self.name = name
        self.players: List[Player] = []

    def assign_player(self, player: Player) -> str:

        if player in self.players:
            return f"Player {player.name} is already in the guild."
        if player.guild != "Unaffiliated":
            return f"Player {player.name} is in another guild."

        player.guild = self.name
        self.players.append(player)
        return f"Welcome player {player.name} to the guild {self.name}"

    def kick_player(self, player_name: str) -> str:

        try:
            kick_player = next(filter(lambda p: p.name == player_name, self.players))

        except StopIteration:
            return f"Player {player_name} is not in the guild."

        kick_player.guild = "Unaffiliated"
        self.players.remove(kick_player)

        return f"Player {player_name} has been removed from the guild."

    def guild_info(self) -> str:

        players_info = f"\n".join(p.player_info() for p in self.players)

        return f"Guild: {self.name}\n{players_info}"

