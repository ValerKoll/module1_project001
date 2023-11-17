## 1. Describe the Problem
As user
I need to retrive statistics on a single diary entry
In specific: number of word, reading time base on a wpm number, section that can be readen in a given time

## 2. Design the Function Signature
class DiaryEntry:
    def __init__(self, title, contents):
        self.title = title
        self.contents = contents

    def format(self):
        # Returns:
        #   A formatted diary entry, for example:
        #   "My Title: These are the contents"
        pass

    def count_words(self):
        # Returns:
        #   int: the number of words in the diary entry
        pass

    def reading_time(self, wpm):
        # Parameters:
        #   wpm: an integer representing the number of words the user can read 
        #        per minute
        # Returns:
        #   int: an estimate of the reading time in minutes for the contents at
        #        the given wpm.
        pass

    def reading_chunk(self, wpm, minutes):
        # Parameters
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   string: a chunk of the contents that the user could read in the
        #           given number of minutes
        #
        # If called again, `reading_chunk` should return the next chunk,
        # skipping what has already been read, until the contents is fully read.
        # The next call after that should restart from the beginning.
        pass

## 3. Create Examples as Tests
```python
# Instance of class

## Given a title and content - returns a formated string_
def test_given_title_content_return_fstring()
instance of class("the next chapter","On the other HAND I would love TO recall a series of events")
format()
=> ["The Next Chapter: On the other hand I would love to recall a series of events"]

## Given a an empty title and content - returns a formated string
def test_given_notitle_content_return_fstring()
>>> instance of class("","On the other HAND I would love TO recall a series of events")
format()
=> ["Diary Entry {timestamp}: On the other hand I would love to recall a series of events"]

## Given a a title and an empty content - returns None
def test_given_title_nocontent_return_none()
>>> instance of class("the next chapter","")
format()
=> None

## Given an empty title and an empty content - returns None
def test_given_notitle_nocontent_return_none()
>>> instance of class("the next chapter","")
format()
=> None


#========
## Frunction count_words

## exist True or False - wrong number
## return None if no content - return the number if content is present
def test_return_words_count()
>>> instance of class("the next chapter","On the other HAND I would love TO recall a series of events")
>>> count_word()
=> 13
>>> instance of class("the next chapter","")
>>> count_word()
=> None
>>> instance of class("","")
>>> count_word()
=> None

## given tittle-content 
        # Parameters:
        #   wpm: an integer representing the number of words the user can read 
        #        per minute
        # Returns:
        #   int: an estimate of the reading time in minutes for the contents at
        #        the given wpm.
        #   (see text below attched for testing)
>>> instance of class("title","content")
>>> reading_time(_wpm_)
 ==> 210/wpm == minutes
## given title-content
        # Parameters
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   string: a chunk of the contents that the user could read in the
        #           given number of minutes
        #
        # If called again, `reading_chunk` should return the next chunk,
        # skipping what has already been read, until the contents is fully read.
        # The next call after that should restart from the beginning.


```

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._
```python
from lib..... import *
```


```
text_exemple_210ws = "
one two thr fou fiv six sev eig nin ten one two thr fou fiv six sev eig nin ten one two thr fou fiv six sev eig nin ten one two thr fou fiv six sev eig nin ten one two thr fou fiv six sev eig nin ten one two thr fou fiv six sev eig nin ten one two thr fou fiv six sev eig nin ten one two thr fou fiv six sev eig nin ten one two thr fou fiv six sev eig nin ten one two thr fou fiv six sev eig nin ten one two thr fou fiv six sev eig nin ten one two thr fou fiv six sev eig nin ten one two thr fou fiv six sev eig nin ten one two thr fou fiv six sev eig nin ten one two thr fou fiv six sev eig nin ten one two thr fou fiv six sev eig nin ten one two thr fou fiv six sev eig nin ten one two thr fou fiv six sev eig nin ten one two thr fou fiv six sev eig nin ten one two thr fou fiv six sev eig nin ten one two thr fou fiv six sev eig nin ten"
```
