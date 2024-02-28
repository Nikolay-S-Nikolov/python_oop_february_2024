from project.library import Library
from project.user import User


class Registration:
    # def __init__(self):
    #     pass

    def add_user(self, user: User, library: Library) -> str or None:
        if user in library.user_records:
            return f"User with id = {user.user_id} already registered in the library!"

        library.user_records.append(user)

    def remove_user(self, user: User, library: Library) -> str or None:
        if user not in library.user_records:
            return "We could not find such user to remove!"

        library.user_records.remove(user)

    def change_username(self, user_id: int, new_username: str, library: Library) -> str:
        try:
            user_to_change = next(filter(lambda u: u.user_id == user_id, library.user_records))

        except StopIteration:
            return f"There is no user with id = {user_id}!"

        if user_to_change.username == new_username:
            return "Please check again the provided username - it should be different than the username used so far!"

        if user_to_change.username in library.rented_books:
            library.rented_books[new_username] = library.rented_books.pop(user_to_change.username)

        user_to_change.username = new_username
        return f"Username successfully changed to: {new_username} for user id: {user_id}"


user = User(12, 'Peter')
library = Library()
registration = Registration()
registration.add_user(user, library)
library.books_available.update({'J.K.Rowling': ['The Chamber of Secrets',
                                                'The Prisoner of Azkaban',
                                                'The Goblet of Fire',
                                                'The Order of the Phoenix',
                                                'The Half-Blood Prince',
                                                'The Deathly Hallows']})
library.get_book('J.K.Rowling', 'The Deathly Hallows', 10, user)
print(user)

