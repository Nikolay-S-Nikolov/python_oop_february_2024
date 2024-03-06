from typing import List
from math import ceil


class PhotoAlbum:
    MAX_PHOTO_PER_PAGE = 4

    def __init__(self, pages: int):
        self.pages = pages
        self.photos: List[List[str]] = [[] for _ in range(pages)]

    @classmethod
    def from_photos_count(cls, photos_count: int):
        pages = ceil(photos_count / cls.MAX_PHOTO_PER_PAGE)
        return cls(pages)

    def add_photo(self, label: str) -> str:
        for page_num in range(len(self.photos)):
            if len(self.photos[page_num]) < PhotoAlbum.MAX_PHOTO_PER_PAGE:
                self.photos[page_num].append(label)
                return f"{label} photo added successfully on page {page_num+1} slot {len(self.photos[page_num])}"

        return "No more free slots"

    def display(self):
        result = '-----------\n'
        for row in self.photos:
            result += ' '.join(["[]" for _ in range(len(row))])
            result += '\n-----------\n'
        return result


album = PhotoAlbum(2)

print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))

print(album.display())