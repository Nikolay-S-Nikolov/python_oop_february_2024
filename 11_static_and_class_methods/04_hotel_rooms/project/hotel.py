from typing import List

from project.room import Room


class Hotel:
    def __init__(self, name: str):
        self.name = name
        self.rooms: List[Room] = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count: int):
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room: Room) -> None:
        self.rooms.append(room)

    def take_room(self, room_number: int, people: int) -> None or str:
        room = next(filter(lambda r: r.number == room_number, self.rooms))
        result = room.take_room(people)
        if result:
            return result
        self.guests += people

    def free_room(self, room_number: int) -> str or None:
        room_to_free = next(filter(lambda r: r.number == room_number, self.rooms))
        guests = room_to_free.guests
        result = room_to_free.free_room()
        if result:
            return result
        self.guests -= guests

    def status(self) -> str:
        free_rooms = [str(f.number) for f in self.rooms if not f.is_taken]
        taken_rooms = [str(f.number) for f in self.rooms if f.is_taken]
        return f"Hotel {self.name} has {self.guests} total guests\n" \
               f"Free rooms: {', '.join(free_rooms)}\n" \
               f"Taken rooms: {', '.join(taken_rooms)}"
