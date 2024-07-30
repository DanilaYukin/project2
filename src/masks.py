from typing import Optional
import logging

logger = logging.getLogger('masks')
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler('../logs/masks.log', "w", encoding="utf-8")
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_mask_card_number(card_number: str) -> Optional[str]:
    """Функция принимает номер карты и маскирует его"""
    try:
        logger.info("Поверяем номер карты, чтобы он соответствовал параметрам")
        if card_number.isdigit() and len(card_number) == 16:
            return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[12:]}"
    except Exception as ex:
        logger.error(f"Произошла ошибка: {ex}")


def get_mask_account(account_number: str) -> Optional[str]:
    """Функция принимает номер счета и маскирует его"""
    try:
        logger.info("Проверяем номер счета, чтобы он соответствовал параметрам и маскируем его")
        if len(account_number) == 20 and account_number.isdigit():
            return f"**{account_number[-4:]}"
    except Exception as ex:
        logger.error(f"Произошла ошибка: {ex}")


if __name__ == "__main__":
    print(get_mask_account("73654108430135874305"))
    print(get_mask_card_number("7000792289606361"))
