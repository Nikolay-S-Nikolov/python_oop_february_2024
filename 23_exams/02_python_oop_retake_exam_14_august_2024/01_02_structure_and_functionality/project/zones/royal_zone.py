from project.zones.base_zone import BaseZone


class RoyalZone(BaseZone):
    INITIAL_VOLUME = 10

    def __init__(self, code: str, ):
        super().__init__(code, self.INITIAL_VOLUME)

    def zone_info(self):

        battleships_total_count = len(self.ships)
        pirateships_count = len([s for s in self.ships if type(s).__name__ == 'PirateBattleship'])

        result = [
            "@Royal Zone Statistics@",
            f"Code: {self.code}; Volume: {self.volume}",
            f"Battleships currently in the Royal Zone: {battleships_total_count}, "
            f"{pirateships_count} out of them are Pirate Battleships."
        ]

        if battleships_total_count:
            ships = [f"{s.name}" for s in self.get_ships()]
            result.append(f"#{', '.join(ships)}#")

        return '\n'.join(result)
