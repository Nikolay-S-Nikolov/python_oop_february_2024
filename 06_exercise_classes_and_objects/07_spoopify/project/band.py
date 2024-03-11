from typing import List

from project.album import Album
from project.song import Song


class Band:
    def __init__(self, name: str):
        self.name = name
        self.albums: List[Album] = []

    def add_album(self, album: Album) -> str:
        if album in self.albums:
            return f"Band {self.name} already has {album.name} in their library."

        self.albums.append(album)

        return f"Band {self.name} has added their newest album {album.name}."

    def remove_album(self, album_name: str) -> str:
        try:
            album_to_remove = next(filter(lambda a: a.name == album_name, self.albums))

        except StopIteration:
            return f"Album {album_name} is not found."

        if album_to_remove.published:
            return "Album has been published. It cannot be removed."

        self.albums.remove(album_to_remove)

        return f"Album {album_name} has been removed."

    def details(self) -> str:
        album_info = '\n'.join(a.details() for a in self.albums)
        return f"Band {self.name}\n{album_info}"

