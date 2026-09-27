from datetime import datetime
from typing import Any


def filter_by_state(in_list_operation: list[dict[str, Any]], concept_str: str = "EXECUTED") -> list[dict[str, Any]]:
    """
    функция получает на входе список словарей, и значение ключа отбора
    возвращает новый список словарей, в котором только те словаре, у которых
     значение по ключу отбора 'state' равно значению полученного в параметрах
     concept_str, по умолчанию в статусе 'EXECUTED'
    """
    return [operation for operation in in_list_operation if operation.get("state", "") == concept_str]


def sort_by_date(in_list_operation: list[dict[str, Any]], order_by: bool = True) -> list[dict[str, Any]]:
    """
    Функция принимает 2 параметра: список словарей и значение параметра сортировки  по умолчанию - по убыванию
     для поля 'date', возвращает новый отсортированный список словарей по дате операции
    """
    return sorted(in_list_operation, key=lambda rec: datetime.fromisoformat(rec["date"]), reverse=order_by)
