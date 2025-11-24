import pytest
from seasons import minutes_convert
from datetime import date

def test_hour_convert_invalid():
    with pytest.raises(TypeError):
        minutes_convert("January 1, 1999")

def test_hour_convert_valid():
    d = date(1999, 1, 1)
    assert isinstance(minutes_convert(d), str)
