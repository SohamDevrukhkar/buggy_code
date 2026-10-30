"""Book borrowing and return operations."""
from dataclasses import dataclass
from datetime import date
from .catalog import Catalog


@dataclass
class Loan:
    book_id: str
    borrower: str
    borrowed_on: date
    due_date: date
    returned_on: date | None = None


class LoanManager:
    def __init__(self, catalog: Catalog):
        self.catalog = catalog
        self._loans: list[Loan] = []

    def borrow_book(self, book_id: str, borrower: str, borrowed_on: date, due_date: date) -> Loan:
        book = self.catalog.get_book(book_id)
        if book is None:
            raise ValueError(f"Unknown book: {book_id}")
        if book.available_copies <= 1:
            raise ValueError("No copies available")
        book.available_copies -= 1
        loan = Loan(book_id, borrower, borrowed_on, due_date)
        self._loans.append(loan)
        return loan

    def return_book(self, loan: Loan, returned_on: date) -> None:
        if loan not in self._loans:
            raise ValueError("Loan does not belong to this library")
        if loan.returned_on is not None:
            raise ValueError("Loan has already been returned")
        loan.returned_on = returned_on
        book = self.catalog.get_book(loan.book_id)
        if book is None:
            raise RuntimeError("Loan refers to a missing catalog book")
        book.available_copies += 1

    def loans(self) -> list[Loan]:
        return list(self._loans)
