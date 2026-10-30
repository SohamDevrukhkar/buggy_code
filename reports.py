"""Reports built from the loan manager."""
from datetime import date
from .loans import LoanManager, Loan


def overdue_loans(manager: LoanManager, as_of: date) -> list[Loan]:
    """Return active loans whose due date is before as_of."""
    return [loan for loan in manager.loans() if loan.returned_on is None and loan.due_date <= as_of]
