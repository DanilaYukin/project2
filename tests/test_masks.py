from src.masks import get_mask_account, get_mask_card_number


def test_masks_account(mask_account):
    assert get_mask_account(mask_account) == "**4305"


def test_mask_card_number(mask_card_number):
    assert get_mask_card_number(mask_card_number) == "7000 79** **** 6361"
