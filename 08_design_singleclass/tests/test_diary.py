from lib.diary import *
from lib.diary_entry import *

# diary
#def test_():
#    pass

#diary_entry
def test_empty_title_content():
    diaryentry = DiaryEntry("", "")
    assert diaryentry.title == ""
    assert diaryentry.contents == ""
    diaryentry = DiaryEntry("Title", "Entry1")
    assert diaryentry.title == "Title"
    assert diaryentry.contents == "Entry1"
    #=> None
    #=> ""#

def test_count_words():
    diaryentry = DiaryEntry("Title", "Entry1 second")
    assert diaryentry.count_words() == 2

def test_reading_time():
    diaryentry = DiaryEntry("Title", "Entry1 second Entry1 second Entry1 second Entry1 second")
    assert diaryentry.reading_time(8) == 1
    
def test_():
    text_exemple_210ws = "one two thr fou fiv six sev eig nin ten one two thr fou fiv six sev eig nin ten one two thr fou fiv six sev eig nin ten one two thr fou fiv six sev eig nin ten one two thr fou fiv six sev eig nin ten one two thr fou fiv six sev eig nin ten one two thr fou fiv six sev eig nin ten one two thr fou fiv six sev eig nin ten one two thr fou fiv six sev eig nin ten one two thr fou fiv six sev eig nin ten one two thr fou fiv six sev eig nin ten one two thr fou fiv six sev eig nin ten one two thr fou fiv six sev eig nin ten one two thr fou fiv six sev eig nin ten one two thr fou fiv six sev eig nin ten one two thr fou fiv six sev eig nin ten one two thr fou fiv six sev eig nin ten one two thr fou fiv six sev eig nin ten one two thr fou fiv six sev eig nin ten one two thr fou fiv six sev eig nin ten one two thr fou fiv six sev eig nin ten"

    #diaryentry = DiaryEntry("Title", text_exemple_210ws)
    #assert diaryentry.reading_time(8) == 1
    
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

def test_adding_entry_stored_correctly():
    diary = Diary()
    diaryentry = DiaryEntry("Title", "Entry1 second")
    diary.add(diaryentry)
    #check if entry in diary
    assert diary.all() == [diaryentry]

def test_adding_entry_stored_correctly():
    diary = Diary()
    diaryentry1 = DiaryEntry("Title", "Entry1 secon")
    diaryentry2 = DiaryEntry("Title", "Entry2 third")
    diaryentry3 = DiaryEntry("Title", "Entry3 secon")
    diary.add(diaryentry1)
    diary.add(diaryentry2)
    diary.add(diaryentry3)
    result = diary.count_words()
    assert result == 6

def test_reading_time_whole():
    diary = Diary()
    diaryentry1 = DiaryEntry("Title", "Entry1 secon")
    diaryentry2 = DiaryEntry("Title", "Entry2 third")
    diaryentry3 = DiaryEntry("Title", "Entry3 secon")
    diary.add(diaryentry1)
    diary.add(diaryentry2)
    diary.add(diaryentry3)
    assert diary.reading_time(6) == 1
    
def test_best_reading_time():
    diary = Diary()
    diaryentry1 = DiaryEntry("Title", "one two thr fou fiv six sev eig nin ten")
    diaryentry2 = DiaryEntry("Title", "one two thr fou fiv six sev eig nin")
    diaryentry3 = DiaryEntry("Title", "one two thr fou fiv")
    diaryentry4 = DiaryEntry("Title", "one two thr fou fiv six")
    diary.add(diaryentry1)
    diary.add(diaryentry2)
    diary.add(diaryentry3)
    diary.add(diaryentry4)
    assert diary.find_best_entry_for_reading_time(9, 1) == diaryentry4