import pytest
from lib.todo_list import *


def test_text_is_empty():
    with pytest.raises(Exception) as e:
        check_todos("")
    result_message = str(e.value)
    assert result_message == "The input parameter is not valid!"


def test_text_is_none():
    with pytest.raises(Exception) as e:
        check_todos(None)
    result_message = str(e.value)
    assert result_message == "The input parameter is not valid!"


def test_text_if_not_todo():
    text = "I stayed out fifteen minutes, and then went back, hoping for better luck. Fill the E30 form by tomorrow."
    result = check_todos(text)
    assert result == ""

def test_text_if_is_todo():
    text1 = "#TODO Fill the E30 form by tomorrow"
    result = check_todos(text1)
    assert result == "Fill the E30 form by tomorrow"
    text2 = "I stayed out fifteen minutes, and then went back, hoping for better luck. #TODO Fill the E30 form by tomorrow.  Of course all the chairs were occupied now, and four men sat waiting,"
    result = check_todos(text2)
    assert result == "Fill the E30 form by tomorrow"
    