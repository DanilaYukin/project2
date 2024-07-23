from src.processing import filter_by_state, sort_by_date


def test_filter(filter_state):
    assert filter_by_state(filter_state) == [
        {"id": 41428829, "state": "EXECUTED", "data": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "data": "2018-06-30T02:08:58.425572"},
    ]


def test_date(filter_date):
    assert sort_by_date(filter_date) == [
        {"id": 41428829, "state": "EXECUTED", "data": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "data": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "data": "2018-09-12T21:27:25.241689"},
        {"id": 939719570, "state": "EXECUTED", "data": "2018-06-30T02:08:58.425572"},
    ]
