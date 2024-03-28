class Book:
    def __init__(self, content: str):
        self.content = content


class Formatter:
    def format(self, book: Book) -> str:
        return book.content


class PaperFormatter:
    def format(self, book: Book) -> str:
        return book.content[:4]


class Printer:
    def get_book(self, book: Book, formatter):
        formatted_book = formatter.format(book)
        return formatted_book


base_formatter = Formatter()
book = Book("Some content")
p = Printer()
paper_formatter = PaperFormatter()

print(p.get_book(book, base_formatter))
print(p.get_book(book, paper_formatter))

