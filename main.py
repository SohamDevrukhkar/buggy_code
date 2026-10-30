"""Small command-line demonstration for the library challenge."""
from datetime import date
from library.service import LibraryService


def build_demo_library() -> LibraryService:
    library = LibraryService()
    library.register_book("B-001", "The Pragmatic Programmer", "Andrew Hunt", copies=2)
    library.register_book("B-002", "Clean Code", "Robert C. Martin", copies=1)
    return library


if __name__ == "__main__":
    app = build_demo_library()
    loan = app.borrow("B-001", "Asha", date(2026, 10, 1), date(2026, 10, 15))
    print(f"Borrowed {loan.book_id}; due {loan.due_date}")
