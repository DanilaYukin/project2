from src.generators import filter_by_currency, transaction_descriptions, card_number_generator


def test_filter_by_currency():
    currency = filter_by_currency
    assert next(currency) == 939719570
    assert next(currency) == 142264268


def test_transaction_descriptions(transaction_des):
    description = transaction_descriptions
    for expected in transaction_des:
        assert next(description) == expected
        assert next(description) == expected


def test_card_number_generator(number_generator):
    generator = card_number_generator
    for card in number_generator:
        assert next(generator) == card
        assert next(generator) == card
