from project.zones.base_zone import BaseZone


class PirateZone(BaseZone):
    INITIAL_VOLUME = 8

    def __init__(self, code: str, ):
        super().__init__(code, self.INITIAL_VOLUME)

    def zone_info(self) -> str:
        battleships_total_count = len(self.ships)
        royalships_count = len([s for s in self.ships if type(s).__name__ == 'RoyalBattleship'])

        result = [
            "@Pirate Zone Statistics@",
            f"Code: {self.code}; Volume: {self.volume}",
            f"Battleships currently in the Pirate Zone: {battleships_total_count}, "
            f"{royalships_count} out of them are Royal Battleships."
        ]

        if battleships_total_count:
            ships = [f"{s.name}" for s in self.get_ships()]
            result.append(f"#{', '.join(ships)}#")

        return '\n'.join(result)
