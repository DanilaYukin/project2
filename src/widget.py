from src.masks import get_mask_account
from src.masks import get_mask_card_number
from typing import Optional


def mask_account_card(cards_number: str) -> Optional[str]:
    """ Функция которая маскирует номер карты и счета """
    if "Счет" in cards_number:
        mask_account = get_mask_account(cards_number[:])
        return mask_account
    else:
        card = get_mask_card_number(cards_number[-16:])
        mask_card = cards_number.replace(cards_number[-16:], card)
        return mask_card


if __name__ == '__main__':
    print(mask_account_card('''Maestro 1596837868705199
Счет 64686473678894779589
MasterCard 7158300734726758
Счет 35383033474447895560
Visa Classic 6831982476737658
Visa Platinum 8990922113665229
Visa Gold 5999414228426353
Счет 73654108430135874305'''))
