# {{PROBLEM}} Function Design Recipe

## 1. Describe the Problem

As a user
So that I can keep track of my tasks
I want to check if a text includes the string #TODO.


## 2. Design the Function Signature


```python
def check_todos(text):
    # detect the intention to store a TODO note
    # Parameters:
    #    a string which contains #TODO 
    # Returns:
    #    a sub-string of the input text witout the #TODO  
    # Side effects: this function doesn't print anything or have any other side-effects
    pass 
```

## 3. Create Examples as Tests

```python
"""
given an empty text
return an Error 
"""
test_text_is_empty()
==>  return Error

"""
given a None value
return an Error
"""
test_text_is_none()
==>  return Error

"""
given a text without a #TODO
return an empty string
"""
test_text_if_not_todo()
#"I stayed out fifteen minutes, and then went back, hoping for better luck. Fill the E30 form by tomorrow.")
==>  return

"""
given a text with a #TODO
return the cropped text (ready to be stored by the main method)
"""
test_text_if_is_todo()
#"I stayed out fifteen minutes, and then went back, hoping for better luck. #TODO Fill the E30 form by tomorrow.")
==>  return
```


## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._


List of testing files
    test_todo_list.py

>>> implement in testing files not here
----------------------------

```python
from  import *
# example
"""
Given a ....
"""
def test_():
    result = func("")
    assert result == [""]

```


EXAMPLE text:
"#TODO Fill the E30 form by tomorrow"
"I stayed out fifteen minutes, and then went back, hoping for better luck. #TODO Fill the E30 form by tomorrow. Of course all the chairs were occupied now, and four men sat waiting, silent, unsociable, distraught, and looking bored, as men always do who are waiting their turn in a barber's shop."