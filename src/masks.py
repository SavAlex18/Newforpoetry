def get_mask_card_number(card_number: str) -> str | None:
    """Маскирует номер банковской карты, оставляя 6 первых и 4 последних цифры"""
    if len(card_number) != 16:
        return None
    res = [card_number[i : i + 4] for i in range(0, len(card_number), 4)]
    mask = []
    for index, item in enumerate(res):
        if index in (0, 3):
            mask.append(item)
        elif index == 1:
            mask.append(item[0:2] + 2 * "*")
        else:
            mask.append(4 * "*")
    mask_number = " ".join(mask)
    return mask_number


def get_mask_account(account_number: str) -> str | None:
    """Маскирует счёт клиента оставляя последние 4 цифры"""
    if len(account_number) < 4:
        return None

    return 2 * "*" + account_number[-4:]
