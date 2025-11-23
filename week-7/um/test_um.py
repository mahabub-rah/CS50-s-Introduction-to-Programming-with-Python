from um import count

def test_valid_count():
    assert count("um") == 1
    assert count("um?") == 1
    assert count("ummm?") == 0
    assert count("Um, thanks for the album") == 1
    assert count("Um, thanks, um...") == 2
    assert count("yummy") == 0
    assert count("yum") == 0
    assert count("UM............um") == 2