import pytest
from lib.reading_time import *

# Given a text
# it returns the duration
def test_given_a_text_returns_duration():
    result = reading_time(get_text(0))
    assert result == 0.5
    result = reading_time(get_text(1))
    assert result == 1


# Given an empty string
#it returns an empty string
def test_given_a_empty_string_return_error():
    with pytest.raises(Exception) as e:
        result = reading_time("")
    erro_message = str(e.value)
    assert erro_message == "Error"

#Given a number
#it returns an error using the raise Exeception method
def test_given_number_return_error():
    #result = reading_time(12345)
    pass


#Given a None value
#It throws an error
def test_given_a_number_throws_error():
    with pytest.raises(Exception) as e:
        result = reading_time(123)
    erro_message = str(e.value)
    assert erro_message == "Error"




##storage for text
def get_text(index):
    # 1:102  2:204
    text = [
        "We produce about two million dollars for each hour we work. #TODO  Fill the form. The fifty hours is one conservative estimate for how long it we take to get any etext selected, entered, proofread, edited, copyright searched and analyzed, the copyright letters written, etc.  This projected audience is one hundred million readers. We produce about two million dollars for each hour we work.  The fifty hours is one conservative estimate for how long it we take to get any etext selected, entered, proofread, edited, copyright searched and analyzed, the copyright letters written, etc.  This projected audience is one hundred million readers.",
        "We produce about two million dollars for each hour we work.  The fifty hours is one conservative estimate for how long it we take to get any etext selected, entered, proofread, edited, copyright searched and analyzed, the copyright letters written, etc.  This projected audience is one hundred million readers. We produce about two million dollars for each hour we work.  The fifty hours is one conservative estimate for how long it we take to get any etext selected, entered, proofread, edited, copyright searched and analyzed, the copyright letters written, etc.  This projected audience is one hundred million readers. We produce about two million dollars for each hour we work.  The fifty hours is one conservative estimate for how long it we take to get any etext selected, entered, proofread, edited, copyright searched and analyzed, the copyright letters written, etc.  This projected audience is one hundred million readers. We produce about two million dollars for each hour we work.  The fifty hours is one conservative estimate for how long it we take to get any etext selected, entered, proofread, edited, copyright searched and analyzed, the copyright letters written, etc.  This projected audience is one hundred million readers."        
    ]
    return text[index]