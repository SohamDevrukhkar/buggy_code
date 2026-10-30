from datetime import date
import pytest


def test_can_borrow_the_last_available_copy(library):
    loan = library.borrow("B2", "Ravi", date(2026, 10, 1), date(2026, 10, 14))
    assert loan.book_id == "B2"
    assert library.catalog.get_book("B2").available_copies == 0


def test_borrowing_decrements_available_copies(library):
    library.borrow("B1", "Mira", date(2026, 10, 1), date(2026, 10, 14))
    assert library.catalog.get_book("B1").available_copies == 1


def test_returning_restores_available_copies(library):
    loan = library.borrow("B1", "Mira", date(2026, 10, 1), date(2026, 10, 14))
    library.loan_manager.return_book(loan, date(2026, 10, 10))
    assert library.catalog.get_book("B1").available_copies == 2


def test_cannot_return_same_loan_twice(library):
    loan = library.borrow("B1", "Mira", date(2026, 10, 1), date(2026, 10, 14))
    library.loan_manager.return_book(loan, date(2026, 10, 10))
    with pytest.raises(ValueError, match="already been returned"):
        library.loan_manager.return_book(loan, date(2026, 10, 11))
