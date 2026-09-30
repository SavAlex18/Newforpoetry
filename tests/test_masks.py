from src.masks import get_mask_account, get_mask_card_number


def test_get_mask_card_number() -> None:
    assert get_mask_card_number("1234567890123456") == ("1234 56** **** 3456")
    assert get_mask_card_number("") == (None)
    assert get_mask_card_number("12345678901234567") == (None)


def test_get_mask_account() -> None:
    assert get_mask_account("987654321") == ("**4321")
    assert get_mask_account("4321") == ("**4321")
    assert get_mask_account("321") == (None)
