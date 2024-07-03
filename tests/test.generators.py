from src.generators import filter_by_currency, transaction_descriptions, card_number_generator


def test_filter_by_currency(transactions):
    currency = filter_by_currency(transactions, "USD")
    assert next(currency) == 939719570
    assert next(currency) == 142264268


def test_transaction_descriptions(transactions, transaction_des):
    description = transaction_descriptions(transactions)
    for expected in transaction_des:
        assert next(description) == expected
        assert next(description) == expected


def test_card_number_generator(transactions, number_generator):
    generator = card_number_generator(1, 5)
    for card in number_generator:
        assert next(generator) == card
        assert next(generator) == card
