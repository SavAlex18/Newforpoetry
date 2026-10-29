import logging
from pathlib import Path

Path("logs").mkdir(exist_ok=True)
logger = logging.getLogger("masks")
file_handler = logging.FileHandler("logs/masks.log", mode="w")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def get_mask_card_number(card_number: str) -> str | None:
    """Маскирует номер банковской карты, оставляя 6 первых и 4 последних цифры
    функция получает номр банковской карты, строка 16 символов,
    а возвращает строку, оставляя правильными только 6 первых и 4 последних
    цифры, вместо остальных цифр проставляются звёздочки.
    Если на входе строка не 16-ть символов, возвращвется None
    """
    logger.info(f"Получен для маскирования номер карты: {card_number}")
    if len(card_number) != 16:
        logger.error(f"Необрабатываемы номер карты: {card_number}")
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
    logger.info(f"Получен замаскированный номер карты: {mask_number}")
    return mask_number


def get_mask_account(account_number: str) -> str | None:
    """Маскирует счёт клиента оставляя последние 4 цифры
    функця получает на входе символьную строку из цифр,
    возвращает строку из *, кроме 4-х последних, которые
    сохраняют реальные цифры счета.
    Если длина входной строки меньше 4-х символов, возвращается None
    """
    logger.info(f"Получен номер счёта клиента: {account_number}")
    if len(account_number) < 4:
        logger.error(f"Необрабатываемый номер счёта клиента: {account_number}")
        return None
    logger.info(f"Получен замаскированный счет: {2 * "*" + account_number[-4:]}")

    return 2 * "*" + account_number[-4:]
