# TDD a single class

## Exercise 1

### Describe the problem

`As a user
So that I can keep track of my tasks
I want a program that I can add todo tasks to and see a list of them.`

`As a user
So that I can focus on tasks to complete
I want to mark tasks as complete and have them disappear from the list.`

#### Design
```
class name: Tasks
    parameters: none
    properties: dictionary of tasks (tasks_dict)   scope: private
    methods:
        - add_tasks
            accept #2 parameter, a title and a content
            return "Entry Added" if the task has been added successfully - if not None
            conditions: content not empty, title also empty but replaced by "Untitled"
            note: the timestamp and a flag (toComplete True/False) is added in separted fields
        - get_tasts
            accept #0 parameters
            return a list of tasks
            conditions: list is not empty
```

#### Code signature:
```python
class Tasks():
    #dictionary structure
    tasks_dict = {
        taskid {
            title
            content
            timestamp
            flag
            }
    }


    def __init__():
        pass
    def add_tasks(title_to_add, content_to_add):
        pass
    def get_tasks():
        pass  #return a list
```

#### Tests
```
empty/wrong/correct
add: wrong input - right input
    test_given_empty_paramenters_return_none
    test_given_correct_paramenters_return_"Entry Added" (compare using get_tasks)
get: empty list - output has to be right format
    test_given_no_tasks_return_empty_list (use len(list))
    test_given_tasks_return_number_correct_entries
```


<br><br>
 ---------- PHASE 2 ------------------
## CHALLANGE


### Describe the problem

`As a user
So that I can keep track of my music listening
I want to add tracks I've listened to and see a list of them.`

#### Design
```
class name: SongTracks
    parameters: none
    properties:
        '__tasks_dict' - is the main song entries container - private scope
        '__counter' - it keeps tracks of the number of entries - private scope
    methods:
        - add_songs
            accept #2 parameters, an Author and a Title
            return "Entry Added" if the song has been added successfully - if not returns None
            conditions: content not empty, title also empty but replaced by "Unknown"
            note: the timestamp and a flag (toComplete True/False) is added in separted fields
        - get_songs
            accept #0 parameters
            return the summary of all the songs added divided by listened or not
            conditions: dictionary is not empty
        - flag_songs
            accept #1 parameter - song index #01
            return an error in case the song has not been found
```

#### Code signature:
```python
class SongTracker():
    #properties 
    songs_dict = {
        songs_id {
            Author
            Title
            flag
            }
    }
    counter = 0

    #methods
    def __init__():
        pass

    def add_songs(author_to_add, title_to_add):
        pass

    def get_songs():
        pass

    def flag_songs():
        pass
```

#### Tests
```python
"""
when no entry is added
the database is empty returns str"Empty"
"""
tracker = SongTracker()
get_song() == None

"""
when given empty parmaneters
returns None
"""
tracker = SongTracker()
add_songs("Jack", "")
get_song() == None

"""
when adding 1 song
it returns "Entry added" and shows in the dictionary
"""
tracker = SongTracker()
add_songs("Jack", "The river under the bridge")
get_songs() == "Jack: The river under the bridge"

"""
when adding multple songs
are all recflected in the dictionary
"""
tracker = SongTracker()
add_songs("Jack", "The river under the bridge1")
add_songs("Nolan", "The river under the bridge2")
get_songs() == ["Jack: The river under the bridge", "Nolan", "The river under the bridge2"]

"""
when adding multple songs
and flag 1 completed, it dissappears from the returned list
"""
tracker = SongTracker()
add_songs("Jack", "The river under the bridge1")
add_songs("Nolan", "The river under the bridge2")
flag_songs(1)
get_songs() == ["Nolan", "The river under the bridge2"]

"""
when flagging a task not in the list as completed
return an error
"""
tracker = SongTracker()
add_songs("Jack", "The river under the bridge1")
add_songs("Nolan", "The river under the bridge2")
flag_songs(3) == ERROR
```






