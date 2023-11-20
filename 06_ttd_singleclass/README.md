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