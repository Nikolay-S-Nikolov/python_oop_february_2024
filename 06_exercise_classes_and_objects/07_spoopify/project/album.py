from typing import List, Tuple

from project.song import Song


class Album:
    def __init__(self, name: str, *song: Song):
        self.name = name
        self.songs: List[Song] = []
        self.published = False
        self.songs.extend(song)

    def add_song(self, song: Song) -> str:

        if song in self.songs:
            return "Song is already in the album."

        if self.published:
            return "Cannot add songs. Album is published."

        if song.single:
            return f"Cannot add {song.name}. It's a single"

        self.songs.append(song)

        return f"Song {song.name} has been added to the album {self.name}."

    def remove_song(self, song_name: str) -> str:
        if self.published:
            return "Cannot remove songs. Album is published."
        try:
            song_to_remove = next(filter(lambda s: s.name == song_name, self.songs))

        except StopIteration:
            return "Song is not in the album."

        self.songs.remove(song_to_remove)

        return f"Removed song {song_name} from album {self.name}."

    def publish(self):
        if self.published:
            return f"Album {self.name} is already published."

        self.published = True

        return f"Album {self.name} has been published."

    def details(self):
        song_info = '\n'.join(f"== {s.get_info()}" for s in self.songs)
        return f"Album {self.name}\n{song_info}"
