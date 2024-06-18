from typing import Optional


def get_mask_card_number(card_number: str) -> Optional[str]:
    """Функция принимает номер карты и маскирует его"""
    if not card_number.isdigit() or len(card_number) != 16:
        return
    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[12:]}"


print(get_mask_card_number("7000792289606361"))


def get_mask_account(account_number: str) -> Optional[str]:
    """Функция принимает номер счета и маскирует его"""
    if not account_number.isdigit():
        return
    return f"**{account_number[-4:]}"


print(get_mask_account("73654108430135874305"))
