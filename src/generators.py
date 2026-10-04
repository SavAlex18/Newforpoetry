from typing import Iterator, Any, Dict


def filter_by_currency(list_transactions: list) -> Iterator[dict[str, any]]:
    """
    функция filter_by_currency принимает на вход список словарей, представляющих транзакции.
    Функция возвращает итератор, который поочередно выдает транзакции
    ,где валюта операции соответствует заданной.

    AI is creating summary for filter_by_currency

    Args:
        list_transactions (list): [description]

    Yields:
        Iterator[dict[str, any]]: [description]
    """
    pass


def transaction_descriptions():
    """
        Генератор transaction_descriptions
        который принимает список словарей с транзакциями и возвращает описание каждой операции по очереди
    """
    pass


def card_number_generator(start_number: int, end_number: int) -> str:
    """
        выдает номера банковских карт в формате
        XXXX XXXX XXXX XXXX, где X — цифра номера карты
    """
    current_number = start_number
    while current_number <= end_number:
        # str_num = str(current_number)
        str_num = ('0' * 16 + str(current_number))[-16:]
        numb = [str_num[i:i+4] for i in range(0, len(str_num), 4)]

        # print(' '.join(numb))
        current_number += 1
    return ' '.join(numb)


if __name__ == '__main__':


    print(card_number_generator(45468465, 45468466))
