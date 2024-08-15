from typing import List

from project.battleships.pirate_battleship import PirateBattleship
from project.battleships.royal_battleship import RoyalBattleship
from project.zones.pirate_zone import PirateZone
from project.zones.royal_zone import RoyalZone


class BattleManager:
    def __init__(self):
        self.zones: List[RoyalZone or PirateZone] = []
        self.ships: List[RoyalBattleship or PirateBattleship] = []

    def add_zone(self, zone_type: str, zone_code: str):
        valid_types = {"RoyalZone": RoyalZone, "PirateZone": PirateZone}

        if [z for z in self.zones if z.code == zone_code]:
            raise Exception("Zone already exists!")

        try:
            new_zone = valid_types[zone_type](zone_code)

        except KeyError:
            raise Exception("Invalid zone type!")

        self.zones.append(new_zone)
        return f"A zone of type {zone_type} was successfully added."

    def add_battleship(self, ship_type: str, name: str, health: int, hit_strength: int):
        valid_types = {'RoyalBattleship': RoyalBattleship, 'PirateBattleship': PirateBattleship}

        try:
            new_ship = valid_types[ship_type](name, health, hit_strength)

        except KeyError:
            raise Exception(f"{ship_type} is an invalid type of ship!")

        self.ships.append(new_ship)
        return f"A new {ship_type} was successfully added."

    @staticmethod
    def add_ship_to_zone(zone: RoyalZone or PirateZone, ship: RoyalBattleship or PirateBattleship):

        if not zone.volume:
            return f"Zone {zone.code} does not allow more participants!"

        if not ship.health > 0:
            return f"Ship {ship.name} is considered sunk! Participation not allowed!"

        if not ship.is_available:
            return f"Ship {ship.name} is not available and could not participate!"

        zone_ship = {"RoyalZone": "RoyalBattleship", "PirateZone": "PirateBattleship"}
        if zone_ship[type(zone).__name__] == type(ship).__name__:
            ship.is_attacking = True
        else:
            ship.is_attacking = False

        ship.is_available = False
        zone.ships.append(ship)
        zone.volume -= 1

        return f"Ship {ship.name} successfully participated in zone {zone.code}."

    def remove_battleship(self, ship_name: str):
        try:
            ship = next(filter(lambda s: s.name == ship_name, self.ships))

        except StopIteration:
            return "No ship with this name!"

        if not ship.is_available:
            return "The ship participates in zone battles! Removal is impossible!"

        self.ships.remove(ship)
        return f"Successfully removed ship {ship_name}."

    def start_battle(self, zone: RoyalZone or PirateZone):

        try:
            attacker = sorted([a for a in zone.ships if a.is_attacking], key=lambda x: -x.hit_strength)[0]

            target = sorted([a for a in zone.ships if not a.is_attacking], key=lambda x: -x.health)[0]
        except IndexError:
            return "Not enough participants. The battle is canceled."

        attacker.attack()
        target.take_damage(attacker)

        if target.health <= 0:
            zone.ships.remove(target)
            self.ships.remove(target)
            return f"{target.name} lost the battle and was sunk."

        if attacker.ammunition == 0:
            zone.ships.remove(attacker)
            self.ships.remove(attacker)
            return f"{attacker.name} ran out of ammunition and leaves."

        return "Both ships survived the battle."

    def get_statistics(self):

        ordered_zones = sorted(self.zones, key=lambda x: x.code)
        available_ships = [s.name for s in self.ships if s.is_available]

        result = [f"Available Battleships: {len(available_ships)}"]

        if available_ships:
            result.append(f"#{', '.join(available_ships)}#")

        result.extend([f"***Zones Statistics:***", f"Total Zones: {len(self.zones)}"])

        result.extend([z.zone_info() for z in ordered_zones])

        return '\n'.join(result)
