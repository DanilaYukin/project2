from src.utils import get_transaction_list


def test_get_transaction_list():
    assert get_transaction_list('[]') == []


def test_transaction_patch():
    assert get_transaction_list('..\\tests\\operations.json') == []
