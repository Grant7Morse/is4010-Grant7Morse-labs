# lab06.py

class Book:
    """A simple Book model with title, author, and publication year."""

    def __init__(self, title: str, author: str, year: int):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self) -> str:
        return f"\"{self.title}\" by {self.author} ({self.year})"

    def get_age(self) -> int:
        return 2025 - self.year


class EBook(Book):
    """A digital book that extends Book with a file size in megabytes."""

    def __init__(self, title: str, author: str, year: int, file_size: int):
        super().__init__(title, author, year)
        self.file_size = file_size

    def __str__(self) -> str:
        return f"{super().__str__()} ({self.file_size} MB)"


if __name__ == '__main__':
    b = Book("The Hobbit", "J.R.R. Tolkien", 1937)
    e = EBook("Dune", "Frank Herbert", 1965, 5)
    print(b)
    print(e)
    print("EBook age:", e.get_age())