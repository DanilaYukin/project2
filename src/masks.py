from typing import Optional


def get_mask_card_number(card_number: str) -> Optional[str]:
    """Функция принимает номер карты и маскирует его"""
    if card_number.isdigit() and len(card_number) == 16:
        return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[12:]}"


def get_mask_account(account_number: str) -> Optional[str]:
    """Функция принимает номер счета и маскирует его"""
    if account_number.isdigit():
        return f"**{account_number[-4:]}"


if __name__ == '__main__':
    print(get_mask_account("73654108430135874305"))
    print(get_mask_card_number("7000792289606361"))
