from numb3rs import validate
import pytest

def test_valid_number3rs():
    assert validate("255.255.255.255") == True
    assert validate("127.0.0.1") == True

def test_invalid_number3rs():
    
    assert validate("512.512.512.512") == False
    assert validate("192.168.001.1") == False
    assert validate("1.2.3.1000") == False
    assert validate("cat") == False
   