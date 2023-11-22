# GS08 Design a class system

### Request

```
    As a user
    So that I can record my experiences
     keep a regular diary

    As a user
    So that I can reflect on my experiences
     read my past diary entries

    As a user
    So that I can reflect on my experiences in my busy day
     select diary entries to read based on how much time I have and my reading speed

    As a user
    So that I can keep track of my tasks
     keep a todo list along with my diary

    As a user
    So that I can keep track of my contacts
     see a list of all of the mobile phone numbers in all my diary entries
```

### Design

```
class Diary
    parameters: none
    properties: list of entries
    side-effects: none
    methods:    add entry
                    store 1 instance in list of entries
                        parameters: 1 string
                        returns: "Entry added" or None
                        side-effects: none
                get entries
                    display entries
                        parameters: none
                        returns: list of entries or none if empty
                        side-effects: none
                get phone numbers
                    filter and display numbers
                        returns: list
                        side-effects: none
                best reading time


class diary entries
    manage 1 single entry stored in Diary
    paramenters: title, content
    properties: none
    method:     count_words
                reading_time
                reading_chunks
                get_mobile_number

class todo tasks
    manage 1 single entry stored in a TODOlist
    paramenters: title, content
    properties: none
    method:     mark done

```

### Code signature

```python
class Diary():
    def add_entry():
        pass
    def get_entries():
        pass
    def get_phones():
        pass
    def best_reading*(:)
        pass

class DiaryEntry():
    def count_words():
        pass
    def reading_time():
        pass
    def reading_chunks():
        pass
    def mobile_number():
        pass

class TaskEntry():
    def mark_done():
        pass

```