'''
from lib.tdd_singleclass1 import *

def test_given_empty_paramenters_return_none():
    task = Tasks()
    result = task.add_tasks("", "")
    assert result == None
    result = task.add_tasks("Test", "")
    assert result == None


def test_given_correct_paramenters_return_string():
    task = Tasks()
    result = task.add_tasks("", "Test")
    assert result == "Entry Added"
    result = task.add_tasks("Title", "Content ONE")
    assert result == "Entry Added"
    result = task.get_tasks()
    assert result == ["Untitled: test", "Title: content one"]

def test_given_no_tasks_return_message_empty():
    task = Tasks()
    task.add_tasks("Title", "")
    task.add_tasks("", "")
    result = task.get_tasks()
    assert result == "List Empty"
    
    
def test_given_tasks_return_number_correct_entries():
    task = Tasks()
    task.add_tasks("Title", "Content ONE")
    task.add_tasks("Title", "Content ONE")
    task.add_tasks("Title", "Content ONE")
    result = task.get_tasks()
    assert len(result) == 3
    task.add_tasks("Title", "")
    task.add_tasks("Title", "Content ONE")
    result = task.get_tasks()
    assert len(result) == 4
'''