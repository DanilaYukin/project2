import pytest
from src.decorators import log, function


def test_log():
    with pytest.raises(ZeroDivisionError):
        function(2, 0)
