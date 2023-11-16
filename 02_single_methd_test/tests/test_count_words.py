from lib.count_words import *

'''
A function called "count_words" thaa takes a string as an argument and returns the number of words in that string

error checks: 1.wrong number 2.wrong number becasue the divider 3.empty string 4.no returns 5.not a string
'''

def test_given_empty_str_return_empty_str():
    result = count_words("")
    assert result == 0

def test_given_a_non_string_return_None():
    result = count_words(12345)
    assert result == 0

def test_if_given_more_than_5_words_return_5_dots():
    result = count_words("one two three four five six")
    assert result == 6
    
def test_if_given_more_than_5_words_return_5_dots_wrong_divider():
    result = count_words("one two three four five, six")
    assert result == 6

