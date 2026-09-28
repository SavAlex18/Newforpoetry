import pytest

from src.widget import get_date, mask_account_card

def test_get_date(make_iso):
    result = get_date(make_iso)
    assert result == "18.07.2025"

@pytest.mark.parametrize('value, expected', [
    ('счет 1234567', 'Счет **4567'),
    ('счет 123456789', 'Счет **6789'),
    ('МИР 1234567890123456','МИР 1234 56** **** 3456'),
    ('Master Card 1234567890123456', 'Master Card 1234 56** **** 3456')
])
def test_mask_account_card(value, expected):
    assert mask_account_card(value) == expected