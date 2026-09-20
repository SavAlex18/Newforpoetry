from datetime import datetime
from typing import Any


def filter_by_state(in_list_operation: list[dict[str,Any]], concept_str:str='EXECUTED')-> list[dict[str, Any]]:
    """ функция возвращает новый список по ключу concept_str, по умолчанию в статусе 'EXECUTED' """
    return [operation for operation in in_list_operation if operation.get('state','') == concept_str]


def sort_by_date(in_list_operation: list[dict[str, Any]], order_by:bool=True) -> list[dict[str, Any]]:
    """Функция возвращает отсортированный по дате операции, по умолчанию - по убыванию"""
    return sorted(in_list_operation, key=lambda rec: datetime.fromisoformat(rec['date']), reverse=order_by)


