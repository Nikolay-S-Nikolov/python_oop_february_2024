from typing import List


class Book:
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author
        self.page = 0

    def turn_page(self, page):
        self.page = page

    def __repr__(self):
        return f"Book {self.title} from {self.author}"


class Library:
    def __init__(self, books):
        self.books: List[Book] = books

    def add_book(self, book_title: str, author: str):
        if book_title in [b.title for b in self.books]:
            raise Exception(f"Book with title{book_title} already in the library")
        new_book = Book(title=book_title, author=author)
        self.books.append(new_book)
        return f"Book with title {book_title} from author {author} added to the library"

    def get_books_by_title(self, title: str):
        books = [b for b in self.books if b.title == title]
        if not books:
            return f"Book with title {title} not found"
        if len(books) > 1:
            found_books = '\n'.join([f"Title: {b.title} and author: {b.author}" for b in books])
            return f"The following books with title {title} found:" \
                   f"{found_books}"
        return f"Title: {books[0].title} from author: {books[0].author}"

    def get_books_by_author(self, author: str):
        return '\n'.join([b.title for b in self.books if b.author == author])

    def find_book(self, title: str):
        return '\n'.join([str(b) for b in self.books if b.title == title])


if __name__ == '__main__':
    book1 = Book('1', 'A')
    book2 = Book('2', 'B')
    book3 = Book('3', 'C')
    book4 = Book('4', 'D')

    library = Library([book1, book2, book3, book4])

    print(library.find_book('1'))
    print(library.find_book('7'))
    print(library.get_books_by_title('3'))
    print(library.get_books_by_title('5'))
    print(library.get_books_by_author('D'))
    print(library.get_books_by_author('F'))
    print(library.add_book('5', 'E'))
    print(library.add_book('5', 'E'))
