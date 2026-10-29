from src.utils import get_operations

test_operation = {
    "id": 41428829,
    "state": "EXECUTED",
    "date": "2019-07-03T18:35:29.512364",
    "operationAmount": {"amount": "8221.37", "currency": {"name": "USD", "code": "USD"}},
    "description": "Перевод организации",
    "from": "MasterCard 7158300734726758",
    "to": "Счет 35383033474447895560",
}


def test_get_operations() -> None:
    assert get_operations("") == []
    assert get_operations(r"c:\qqqw") == []
    assert (test_operation in get_operations(r"./data/operations.json")) is True
    assert (len(get_operations(r"./data/operations.json"))) == 101
    # assert (type(get_operations(r"./data/operations.json"))) == list()
