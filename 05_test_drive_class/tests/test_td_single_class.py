from lib.td_single_class import *

## Given a title and content - returns a formated string_
def test_given_title_content_return_fstring():
    #check only title caps
    diaryentry = DiaryEntry("the next chapter","On the other hand")
    result = diaryentry.format()
    assert result == "The Next Chapter: On the other hand"
    #check title and content
    diaryentry = DiaryEntry("the next chapter","On the other HAND I would love TO recall a series of events")
    result = diaryentry.format()
    assert result == "The Next Chapter: On the other hand I would love to recall a series of events"

## Given a an empty title and content - returns a formated string
def test_given_emptytitle_content_return_fstring():
    diaryEntry = DiaryEntry("","On the other HAND I would love TO recall a series of events")
    result = diaryEntry.format()
    assert result == "Diary Entry 12-12-2022: On the other hand I would love to recall a series of events"
    
## Given an empty title or/and an empty content - returns None
def test_given_notitle_nocontent_return_none():
    diaryEntry = DiaryEntry("","")
    result = diaryEntry.format()
    assert result == None
    diaryEntry = DiaryEntry("the next chapter","")
    result = diaryEntry.format()
    assert result == None

def test_return_words_count():
    diaryEntry = DiaryEntry("the next chapter","On the other HAND I would love TO recall a series of events")
    result = diaryEntry.count_words()
    assert result == 13
    diaryEntry = DiaryEntry("the next chapt","")
    result = diaryEntry.count_words()
    assert result == None
    diaryEntry = DiaryEntry("","")
    result = diaryEntry.count_words()
    assert result == None

def test_return_minutes():
    diaryEntry = DiaryEntry("the next chapter", text_exemple_210ws)
    wpm = 98
    result = diaryEntry.reading_time(wpm)
    assert result == 2.1
    wpm = 400
    result = diaryEntry.reading_time(wpm)
    assert result == 0.5
    wpm = 0
    result = diaryEntry.reading_time(wpm)
    assert result == "are you asleep?"    

def test_return_chuck_wpm():
    diaryEntry = DiaryEntry("the next chapter", text_exemple_210ws)
    wpm = 98
    minutes_given = 1.2
    result = diaryEntry.reading_chunk(wpm, minutes_given)
    assert result == "one two thr fou fiv six sev eig nin ten one two thr fou fiv six sev eig nin ten one two thr fou fiv six sev eig nin ten one two thr fou fiv six sev eig nin ten one two thr fou fiv six sev eig nin ten one two thr fou fiv six sev eig nin ten one two thr fou fiv six sev eig nin ten one two thr fou fiv six sev eig nin ten one two thr fou fiv six sev eig nin ten one two thr fou fiv six sev eig nin ten one two thr fou fiv six sev eig nin ten one two thr fou fiv six sev eig" # (98*1.2)=117.6 ==> 118
    result = diaryEntry.reading_chunk(wpm, minutes_given)
    assert result == "nin ten one two thr fou fiv six sev eig nin ten one two thr fou fiv six sev eig nin ten one two thr fou fiv six sev eig nin ten one two thr fou fiv six sev eig nin ten one two thr fou fiv six sev eig nin ten one two thr fou fiv six sev eig nin ten one two thr fou fiv six sev eig nin ten one two thr fou fiv six sev eig nin ten one two thr fou fiv six sev eig nin ten" #no space at the end
    result = diaryEntry.reading_chunk(wpm, minutes_given)
    assert result == "one two thr fou fiv six sev eig nin ten one two thr fou fiv six sev eig nin ten one two thr fou fiv six sev eig nin ten one two thr fou fiv six sev eig nin ten one two thr fou fiv six sev eig nin ten one two thr fou fiv six sev eig nin ten one two thr fou fiv six sev eig nin ten one two thr fou fiv six sev eig nin ten one two thr fou fiv six sev eig nin ten one two thr fou fiv six sev eig nin ten one two thr fou fiv six sev eig nin ten one two thr fou fiv six sev eig" #no space at the end
    result = diaryEntry.reading_chunk(wpm, minutes_given)
    assert result == "nin ten one two thr fou fiv six sev eig nin ten one two thr fou fiv six sev eig nin ten one two thr fou fiv six sev eig nin ten one two thr fou fiv six sev eig nin ten one two thr fou fiv six sev eig nin ten one two thr fou fiv six sev eig nin ten one two thr fou fiv six sev eig nin ten one two thr fou fiv six sev eig nin ten one two thr fou fiv six sev eig nin ten" #no space at the end


text_exemple_210ws = "one two thr fou fiv six sev eig nin ten one two thr fou fiv six sev eig nin ten one two thr fou fiv six sev eig nin ten one two thr fou fiv six sev eig nin ten one two thr fou fiv six sev eig nin ten one two thr fou fiv six sev eig nin ten one two thr fou fiv six sev eig nin ten one two thr fou fiv six sev eig nin ten one two thr fou fiv six sev eig nin ten one two thr fou fiv six sev eig nin ten one two thr fou fiv six sev eig nin ten one two thr fou fiv six sev eig nin ten one two thr fou fiv six sev eig nin ten one two thr fou fiv six sev eig nin ten one two thr fou fiv six sev eig nin ten one two thr fou fiv six sev eig nin ten one two thr fou fiv six sev eig nin ten one two thr fou fiv six sev eig nin ten one two thr fou fiv six sev eig nin ten one two thr fou fiv six sev eig nin ten one two thr fou fiv six sev eig nin ten"