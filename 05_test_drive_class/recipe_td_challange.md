## 1. Describe the Problem
As user
I need to be able to check my grammar.
In specific: check the % of correct text passed

### 1.a accepted punctation
```
  [".","!","?"] 
```

## 2. Design the Function Signature
```python
class GrammarStats:
    def __init__(self):
        pass
  
    def check(self, text):
        # Parameters:
        #   text: string
        # Returns:
        #   bool: true if the text begins with a capital letter and ends with a
        #         sentence-ending punctuation mark, false otherwise
        pass
  
    def percentage_good(self):
        # Returns:
        #   int: the percentage of texts checked so far that passed the check
        #        defined in the `check` method. The number 55 represents 55%.
        pass
```

## 3. Create Examples as Tests

_Instance of class_

#### Given a text, check its grammar - returns False if doesn't start with Cap or end with punctation
def test_check_correct_given_text()
instance of class()
check("This could be our the next chapter in life.")
=> True
check("this could be our the next chapter in life.")
=> False
check("This could be our the next chapter in life-")
=> False

## Given multple texts in sequenze - check if multple entries have been stored within the class
def test_given_tests_are_stored()
check("This could be our the next chapter in Boston?")   #VALID
check("This could be our the next chapter in San Francisco.")  #VALID
check("This could be our the next chapter in New York!")   #VALID
check("This could be our the next chapter in Las Vegas.")  #VALID
check("This could be our the next chapter in Miami")  #NOT VALID
=> 4 type: int

## Given multple texts in sequenze - returns a % of correct entries based on the whole dataset
def test_given_tests_return_percentage()
>>> instance of class("","On the other HAND I would love TO recall a series of events")
check("This could be our the next chapter in Boston.")          #VALID
check("This could be our the next chapter in San Francisco?")   #VALID
check("This could be our the next chapter in New York.")        #VALID
check("This could be our the next chapter in Las Vegas.")       #VALID
check("this could be our the next chapter in New York.")        #NOT VALID
check("This could be our the next chapter in Las Vegas.")       #VALID
check("This could be our the next chapter in Miami")            #NOT VALID
check("This could be our the next chapter in Las Vegas!")       #VALID
check("This could be our the next chapter in New York")         #NOT VALID
=> 66% (type: string formatted)



## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._
```python

refere to: test_td_challange.py
from lib..... import *
```
