from typing import Any, Iterator


def filter_by_currency(list_transactions: list, currency: str) -> Iterator[dict[str, Any]]:
    """
    функция filter_by_currency принимает на вход список словарей, представляющих транзакции.
    Функция возвращает итератор, который поочередно выдает транзакции
    ,где валюта операции соответствует заданной.
    Args:
        list_transactions (list): [description]
        currency: str
    Yields:
        Iterator[dict[str, any]]: [description]
    """
    for trans in list_transactions:
        if trans.get("operationAmount", {}).get("currency", {}).get("name") == currency:
            yield trans


def transaction_descriptions(list_transactions: list) -> Iterator[str]:  # Iterator[dict[str, Any]] | None:
    """
        Генератор transaction_descriptions
        принимает список словарей с транзакциями и возвращает описание каждой операции по очереди
    Args:
            list_transactions (list): [description]
    Yields:
        Iterator[str]: [description]
    """
    for trans in list_transactions:
        yield trans.get("description")


def card_number_generator(start_number: int, end_number: int) -> Iterator[str]:
    """
    выдает номера банковских карт в формате
    XXXX XXXX XXXX XXXX, где X — цифра номера карты
    Args:
        start_number: int
        end_number: int
    Yields:
        Iterator[str]: [description]
    """
    for number in range(start_number, end_number + 1):
        str_num = ("0" * 16 + str(number))[-16:]
        numb = [str_num[i : i + 4] for i in range(0, len(str_num), 4)]
        yield " ".join(numb)
