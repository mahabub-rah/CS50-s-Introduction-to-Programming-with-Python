from fuel import gauge, convert
import pytest

def test_gauge():
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(100) == "F"
    assert gauge(30) == "30%"
    assert gauge(50) == "50%"

def test_convert():
    assert convert(3/4) == 75
    assert convert(1/3) == 33
    assert convert(0/100) == 0
    assert convert(100/100) == 100
    with pytest.raises(ZeroDivisionError):
        convert("100/0")
    with pytest.raises(ValueError):
        convert("3/2")
    with pytest.raises(ValueError):
        convert("1.5/4")
    with pytest.raises(ValueError):
        convert("3/4.5")
    with pytest.raises(ValueError):
        convert("-3/4")

