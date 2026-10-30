"""Book catalog operations."""
from dataclasses import dataclass


@dataclass
class Book:
    book_id: str
    title: str
    author: str
    available_copies: int = 1


class Catalog:
    def __init__(self):
        self._books: dict[str, Book] = {}

    def add_book(self, book: Book) -> None:
        if book.book_id in self._books:
            raise ValueError(f"Book already exists: {book.book_id}")
        if book.available_copies < 0:
            raise ValueError("Copies cannot be negative")
        self._books[book.book_id] = book

    def get_book(self, book_id: str) -> Book | None:
        return self._books.get(book_id)

    def search(self, query: str) -> list[Book]:
        """Find books whose title contains query (case-insensitive)."""
        return [book for book in self._books.values() if query in book.title]

    def all_books(self) -> list[Book]:
        return list(self._books.values())
