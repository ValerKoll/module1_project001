from lib.hello import *

def test_hello_1():
    expected = 'Hello Sarah!'
    actual = hello('Sarah')
    
    assert actual == expected

def test_hello_2():
    expected = 'Hello Ja!'
    actual = hello('Ja')
    
    assert actual == expected