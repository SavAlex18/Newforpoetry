import re
from collections import Counter

# from src.import_csv_xlsx import get_transactions_csv, get_transactions_xlsx


def process_bank_search(data: list[dict], search: str) -> list[dict]:
    """принимает список словарей с данными о банковских операциях и строку поиска,
    а возвращает список словарей, у которых в описании есть данная строка
    """
    # print(search)
    ret_list = []
    if len(data) == 0 or len(search) == 0:
        return ret_list
    for item_dict in data:
        try:
            if re.search(search, str(item_dict.get("description", "")), re.IGNORECASE):
                ret_list.append(item_dict)
        except Exception:
            continue

    return ret_list


def process_bank_operations(data: list[dict], categories: list) -> dict:
    """Функция подсчета количества банковских операций определенного типа
    принимает два аргумента: список с транзакциями и список категорий операций,
     по которым необходимо выполнить подсчёт на основе поля description
    """
    if len(data) == 0 or len(categories) == 0:
        return dict()
    category_counter = Counter(
        item.get("description", "") for item in data if item.get("description", "") in categories
    )
    return dict(category_counter)
