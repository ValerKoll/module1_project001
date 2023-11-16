## 1. Describe the Problem (given)

'''
As a user  
So that I can manage my time  
I want to see an estimate of reading time for a text, assuming that I can read
200 words a minute.
'''



## 2. Design the Function Signature (fixed)
```python
def reading_time(text):
# extimate reading time given a string
# Parameters:
#    a medium to long text from a book contaning a mix of simbols and words (e.g. "")
#    Returns:
#        a list of integers rappresenting the duration in hours minutes seconds (HH MM SS)
#   Side effects:
#        This function doesn't trigger any events or interact with other functions/classes
    pass # Test-driving means _not_ writing any code here yet.
```

## 3. Create Examples as Tests (to update)

```python
"""
Given a text
it returns the duration
"""

reading_time("We produce about two million dollars for each hour we work.  The fifty hours is one conservative estimate for how long it we take to get any etext selected, entered, proofread, edited, copyright searched and analyzed, the copyright letters written, etc.  This projected audience is one hundred million readers.") ==  # 51/200 = 0.255 # 51 words 

"""
Given an empty string
it returns an empty string
"""
reading_time("") => [""]

"""
Given a number
it returns an error using the raise Exeception method
"""
reading_time(12345) throws an error

"""
Given a None value
It throws an error
"""
reading_time(None) throws an error

```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour (on tests/Test_ file)

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._


"""
list of test files
test_reading_time.py
"""
