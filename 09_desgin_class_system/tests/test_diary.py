from lib.diary import *
from lib.diary_entry import *
from lib.task_entry import *

def test_added():
    diaryentry = DiaryEntry("","")
    assert (diaryentry.title == "Untitled" and diaryentry.content == "")
    diaryentry = DiaryEntry("Peter","Pan and 100 stories")
    assert diaryentry.title == "Peter" and diaryentry.content == "Pan and 100 stories"

def test_add_entries():
    diary = Diary()
    diaryentry = []
    diaryentry.append(DiaryEntry("Today", "The soon the better"))
    diaryentry.append(DiaryEntry("Sing", "In the middle of the road"))
    for i in diaryentry:
        diary.add_entry(i, diary.ENTRY_TYPE_DIARY)
    assert diary.get_entries(diary.ENTRY_TYPE_DIARY) == [
        diaryentry[0],
        diaryentry[1]
    ]
    taskentry = TaskEntry("cont")
    diary.add_entry(taskentry, diary.ENTRY_TYPE_TASK)
    assert diary.get_entries(diary.ENTRY_TYPE_TASK) == [
        taskentry
    ]
    
def test_phones_entries():
    diary = Diary()
    diaryentry = DiaryEntry("Today", "The soon the better 07723232300")
    assert diaryentry.get_mobile_number() == "07723232300"
    diaryentry = DiaryEntry("Today", "The soon the better 07723232323 end")
    assert diaryentry.get_mobile_number() == "07723232323"
    diaryentry = DiaryEntry("Today", "The soon the better 07223232323 end")
    assert diaryentry.get_mobile_number() == None

def test_list_phones_entries():
    diary = Diary()
    diaryentry = []
    diaryentry.append(DiaryEntry("Today", "The soon the better on the 07723232300"))
    diaryentry.append(DiaryEntry("Sing", "In the middle of the road 07723232323 end"))
    diaryentry.append(DiaryEntry("Today", "The soon the better 02023232323 end"))
    for i in diaryentry:
        diary.add_entry(i, diary.ENTRY_TYPE_DIARY)
    assert diary.get_list_of_phone_numbers() == "Phones Tel num: 07723232300 Tel num: 07723232323 Tel num: 02023232323 "