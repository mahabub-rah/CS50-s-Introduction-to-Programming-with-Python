import pytest
from jar import Jar

def test_init():
    
    #default jar
    jar = Jar()
    assert jar.capacity == 12
    assert jar.size == 0
    
    #custom jar
    jar_custom = Jar(5)
    assert jar_custom.capacity == 5
    assert jar_custom.size == 0
    
    # test invalid
    with pytest.raises(ValueError):
        Jar(-1)

def test_str():
    jar = Jar()
    
    # test empty jar
    assert str(jar) == ""
    
    # test jar with cookies
    jar.deposit(3)
    assert str(jar) == "🍪🍪🍪"
    
    # test with different number of cookies
    jar.deposit(2)
    assert str(jar) == "🍪🍪🍪🍪🍪"

def test_deposit():
    jar = Jar(5)
    
    # test normal deposit
    jar.deposit(3)
    assert jar.size == 3
    
    # test additional deposit
    jar.deposit(2)
    assert jar.size == 5
    
    # test invalid
    with pytest.raises(ValueError):
        jar.deposit(1)
    with pytest.raises(ValueError):
        jar.deposit(-1)


def test_withdraw():
    jar = Jar(5)
    
    jar.deposit(4)
    assert jar.size == 4
    
    # test normal withdrawal
    jar.withdraw(2)
    assert jar.size == 2
    
    # test withdrawal to empty
    jar.withdraw(2)
    assert jar.size == 0
    
    # test invalid
    jar.deposit(1)  
    with pytest.raises(ValueError):
        jar.withdraw(2)
    with pytest.raises(ValueError):
        jar.withdraw(-1)
    