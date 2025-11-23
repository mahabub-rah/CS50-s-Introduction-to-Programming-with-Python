from working import convert
import pytest

def test_valid_time():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("10 AM to 8:50 PM") == "10:00 to 20:50"
    assert convert("10:30 PM to 8 AM") == "22:30 to 08:00"


def test_invalid_time():
    invalid_time = ["9:60 AM to 5:60 PM",
                    "9 AM - 5 PM",
                    "09:00 AM - 17:00 PM",
                    "9AM to 5PM",
                    "9AM - 5PM",
                    "13 AM to 5 PM",
                    "0 AM to 5 PM",
                    "9 AM to 5:70 PM",
                    "9 AM until 5 PM",
                    ]

    for t in invalid_time:
        with pytest.raises(ValueError):
            convert(t)
