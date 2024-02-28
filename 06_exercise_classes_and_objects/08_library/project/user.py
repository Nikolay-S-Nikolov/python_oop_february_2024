from typing import List


class User:
    def __init__(self, user_id: int, username: str):
        self.user_id = user_id
        self.username = username
        self.books: List[str] = []

    def info(self) -> str:
        """"returns a string containing the books
        currently rented by the user in ascending order
         separated by comma and space"""
        result = ", ".join(sorted(self.books))
        return result

    def __str__(self) -> str:
        return f"{self.user_id}, {self.username}, {self.books}"
