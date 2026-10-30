from datetime import date
import pytest
from library.fines import calculate_fine


def test_fine_counts_every_overdue_day():
    assert calculate_fine(date(2026, 10, 1), date(2026, 10, 3), daily_rate=2) == 4.0


def test_grace_period_is_not_charged():
    assert calculate_fine(date(2026, 10, 1), date(2026, 10, 2), daily_rate=2, grace_days=1) == 0.0


def test_fine_is_zero_when_returned_on_due_date():
    assert calculate_fine(date(2026, 10, 1), date(2026, 10, 1)) == 0.0


def test_negative_daily_rate_is_rejected():
    with pytest.raises(ValueError):
        calculate_fine(date(2026, 10, 1), date(2026, 10, 2), daily_rate=-1)
