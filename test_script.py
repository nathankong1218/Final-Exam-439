import pytest
from script import *
#!/usr/bin/ env python3
#Import script.py. Tests on the possible, observed, dataframe and linguistic functions. More info on readme. 

def test_possible_1():
    k = 1
    actual_value = possible("ATTTGGATT",k)
    expected = 1
    assert actual_value == expected

def test_possible_empty():
    k = 10
    actual_value = possible("",k)
    expected = 0
    assert actual_value == expected

def test_possible_0():
    k = 0
    actual_value = possible("ATTTGGATT", k)
    expected = 0
    assert actual_value == expected

def test_observed_9():
    k = 9
    actual_value = observed("ATTTGGATT", k)
    expected = 1
    assert actual_value == expected

def test_observed_empty():
    string = ""
    actual_value = observed(string,9)
    expected = 0
    assert actual_value == expected

def test_observed_neg():
    k = -1
    actual_value = observed("ATTTGGATT",k)
    expected = 0
    assert actual_value == expected

def test_observed_high():
    k = 10
    actual_value = observed ("ATTTGGATT", k)
    expected = 0
    assert actual_value == expected

def test_dataFrame_empty():
    with pytest.raises(ValueError):
        dataFrame("",10)

def test_linguistic_0():
    with pytest.raises(ValueError):
        linguistic("ATTTGGATT",0)


