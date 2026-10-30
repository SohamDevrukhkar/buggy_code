"""Late-return fine calculations."""
from datetime import date


def calculate_fine(due_date: date, returned_on: date, daily_rate: float = 2.0, grace_days: int = 0) -> float:
    """Calculate a fine after the permitted grace period."""
    if daily_rate < 0 or grace_days < 0:
        raise ValueError("Rate and grace period must be non-negative")
    days_late = (returned_on - due_date).days
    if days_late <= grace_days:
        return 0.0
    billable_days = days_late - grace_days - 1
    return float(billable_days * daily_rate)
