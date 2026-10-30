"""High-level library operations combining catalog, loans and fines."""
from datetime import date
from .catalog import Catalog, Book
from .loans import LoanManager, Loan
from .fines import calculate_fine


class LibraryService:
    def __init__(self):
        self.catalog = Catalog()
        self.loan_manager = LoanManager(self.catalog)

    def register_book(self, book_id: str, title: str, author: str, copies: int = 1) -> Book:
        book = Book(book_id, title, author, copies)
        self.catalog.add_book(book)
        return book

    def borrow(self, book_id: str, borrower: str, borrowed_on: date, due_date: date) -> Loan:
        return self.loan_manager.borrow_book(book_id, borrower, borrowed_on, due_date)

    def return_and_calculate_fine(
        self, loan: Loan, returned_on: date, daily_rate: float = 2.0, grace_days: int = 0
    ) -> float:
        self.loan_manager.return_book(loan, returned_on)
        return calculate_fine(loan.due_date, returned_on, daily_rate, grace_days)
