from lib.todo import *
from lib.todo_list import *

#only todo.py
def test_add_todo():
    todo = Todo("Feed the fish")
    assert todo.task == "Feed the fish"
    assert todo.flag == False

def test_if_set_completed_mark_completed():
    todo = Todo("Feed the fish")
    todo.mark_complete()
    assert todo.flag == True
    
#only todolist.py
def test_adding_task_return_list_not_empty():
    todolist = TodoList()
    todo = Todo("Feed the fish")
    todolist.add(todo)
    assert todolist.todolist == [todo]

def test_incomplete():
    todolist = TodoList()
    todo1 = Todo("Feed the fish")
    todo2 = Todo("Feed the cat")
    todo3 = Todo("Feed the dog")
    todolist.add(todo1)
    todolist.add(todo2)
    todolist.add(todo3)
    assert todolist.incomplete() == [todo1, todo2, todo3]

def test_complete():
    todolist = TodoList()
    todo1 = Todo("Feed the fish")
    todo2 = Todo("Feed the cat")
    todo3 = Todo("Feed the dog")
    todolist.add(todo1)
    todolist.add(todo2)
    todolist.add(todo3)
    todo2.mark_complete()
    todo3.mark_complete()
    assert todolist.incomplete() == [todo1]
    assert todolist.complete() == [todo2, todo3]

def test_give_up():
    todolist = TodoList()
    todo1 = Todo("Feed the fish")
    todo2 = Todo("Feed the cat")
    todo3 = Todo("Feed the dog")
    todolist.add(todo1)
    todolist.add(todo2)
    todolist.add(todo3)
    todolist.give_up()
    assert todolist.complete() == [todo1, todo2, todo3]