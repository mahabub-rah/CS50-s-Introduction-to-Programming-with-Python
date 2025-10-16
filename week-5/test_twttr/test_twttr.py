from twttr import shorten
import pytest

def test_twttr():
    assert shorten('Twitter') == 'Twttr'
    assert shorten("What's your name?") == "Wht's yr nm?"
    assert shorten("CS50") == "CS50"
    assert shorten("PYTHON") == "PYTHN"

