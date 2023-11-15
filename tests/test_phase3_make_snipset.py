from lib.phase2_single_test import *

#
#  SINGLE-method test
'''
#  - a function called "make_snippet" that takes #1 argument string and returns the first five words and then a '...' if there are more than that.
'''

def test_given_empty_str_return_empty_str():
    result = make_snipset("")
    assert result == ""

#def test_given_longer_than_5():
#    result = make_snipset("abcder 2")
#    assert result == "abcde..."
    
def test_if_given_more_than_5_words_return_5_dots():
    result = make_snipset("one two three four five six")
    assert result == "one two three four five ..."

def test_given_a_non_string_return_None():
    result = make_snipset(12345)
    assert result == None

