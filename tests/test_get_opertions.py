from src.get_operations import process_bank_operations, process_bank_search

data = [
    {"id": "1", "description": "Перевод другу"},
    {"id": "2", "description": "Перевод недругу"},
    {"id": "3", "description": "Оплата в ГБ"},
    {"id": "4", "description": "Перевод недругу"},
    {"id": "5", "description": "Оплата в ГБ"},
]

data_no_desc = [
    {"id": "1", "desc": "Перевод другу"},
    {"id": "2", "desc": "Перевод недругу"},
    {"id": "2", "desc": "Оплата в ГБ"},
]

category_list = [
    "Перевод недругу",
    "Перевод другу",
    "Оплата в ГБ",
]


def test_process_bank_search_found():
    result = process_bank_search(data, "Перевод")
    assert result == [
        {"id": "1", "description": "Перевод другу"},
        {"id": "2", "description": "Перевод недругу"},
        {"id": "4", "description": "Перевод недругу"},
    ]


def test_process_bank_search_notfound():
    result = process_bank_search(data, "Вывод")
    assert result == []


def test_process_bank_search_empty():
    result = process_bank_search([], "")
    assert result == []


def test_process_bank_search_no_desc():
    result = process_bank_search(data_no_desc, "Вывод")
    assert result == []


def test_process_bank_operations():
    result = process_bank_operations(data, category_list)
    assert result == {"Перевод недругу": 2, "Перевод другу": 1, "Оплата в ГБ": 2}


def test_process_bank_operations_empty_params():
    result = process_bank_operations([], [])
    assert result == {}


def test_process_bank_operations_short_list():
    result = process_bank_operations(data, ["Перевод недругу"])
    assert result == {"Перевод недругу": 2}
