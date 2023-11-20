import pytest
from lib.tdd_challenge import *

def test_empty_dictionary():
    tracker = SongTracker()
    result = tracker.get_songs_notls()
    assert result == None
    
def test_given_empty_paramenters_return_none():
    tracker = SongTracker()
    result = tracker.add_songs("Jack", "")
    assert result == None
    result = tracker.get_songs_notls()
    assert result == None

def test_given_correct_paramenters_return_string():
    tracker = SongTracker()
    result = tracker.add_songs("Jack", "The river under the bridge")
    assert result == "Entry Added"
    result = tracker.get_songs_notls()
    assert result == ["#1 - JACK: The river under the bridge"]

def test_given_multple_songs_return_the_list(): 
    tracker = SongTracker()
    tracker.add_songs("Jack", "The river under the bridge1")
    tracker.add_songs("Nolan", "The river under the bridge2")
    tracker.add_songs("Mike", "The river under the bridge2")
    tracker.add_songs("Jordy", "The river under the bridge3")
    result = tracker.get_songs_notls()
    assert len(result) == 4
    
def test_given_songs_and_flag_1_return_correct_number():
    tracker = SongTracker()
    tracker.add_songs("Jack", "The river under the bridge1")
    tracker.add_songs("Nolan", "The river under the bridge2")
    tracker.add_songs("Mike", "The river under the bridge2")
    tracker.add_songs("Jordy", "The river under the bridge3")
    tracker.flag_songs(2)
    #not listened
    result = tracker.get_songs_notls()
    assert len(result) == 3
    #already listened
    result = tracker.get_songs_ls()
    assert len(result) == 1
    
def test_given_songs_and_flag_1_wrong_number():
    tracker = SongTracker()
    tracker.add_songs("Jack", "The river under the bridge1")
    tracker.add_songs("Nolan", "The river under the bridge2")
    with pytest.raises(Exception) as e:
        tracker.flag_songs(3) #wrong song
    assert str(e.value) == "No song in the database"
    