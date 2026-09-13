import datetime

import masks


def mask_account_card(info_client: str) -> str | None:
    """Функция возвращает замаскированный номер или счёт в зависимости от входного параметра"""
    info_card_account = info_client.split(" ")
    if info_card_account[0].upper() in ["СЧЕТ", "СЧЁТ"]:
        mask_account = masks.get_mask_account(info_card_account[-1])
        if mask_account:
            return "Счет " + mask_account
            # return str("Счет " + masks.get_mask_account(info_card_account[-1]))
        else:
            return None
    else:
        mask_card_number = masks.get_mask_card_number(info_card_account[-1])
        if mask_card_number:
            return str((" ".join(info_card_account[0 : len(info_card_account) - 1]) + " " + mask_card_number))
        else:
            return None


def get_date(input_datetime: str) -> str:
    """Функция возвращает 'немецкий' формат даты в виде дд.мм.гггг из ISO формата"""
    return datetime.datetime.fromisoformat(input_datetime).strftime("%d.%m.%Y")
