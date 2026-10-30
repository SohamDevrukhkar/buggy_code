from datetime import date
from library.reports import overdue_loans


def test_loan_due_today_is_not_yet_overdue(library):
    loan = library.borrow("B1", "Mira", date(2026, 10, 1), date(2026, 10, 30))
    assert overdue_loans(library.loan_manager, date(2026, 10, 30)) == []


def test_past_due_active_loan_is_reported(library):
    loan = library.borrow("B1", "Mira", date(2026, 10, 1), date(2026, 10, 20))
    assert overdue_loans(library.loan_manager, date(2026, 10, 21)) == [loan]


def test_returned_loan_is_not_reported_overdue(library):
    loan = library.borrow("B1", "Mira", date(2026, 10, 1), date(2026, 10, 20))
    library.loan_manager.return_book(loan, date(2026, 10, 19))
    assert overdue_loans(library.loan_manager, date(2026, 10, 21)) == []
