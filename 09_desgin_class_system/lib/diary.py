class Diary():
    ENTRY_TYPE_DIARY = 0
    ENTRY_TYPE_TASK = 1
    
    def __init__(self):
        self.diary_entries = []
        self.task_entries = []

    def add_entry(self, entry, entry_type):
        if entry_type == self.ENTRY_TYPE_DIARY:
            self.diary_entries.append(entry)
        elif entry_type == self.ENTRY_TYPE_TASK:
            self.task_entries.append(entry)

    def get_entries(self, entry_type):
        if entry_type == self.ENTRY_TYPE_DIARY:
            return self.diary_entries
        elif entry_type == self.ENTRY_TYPE_TASK:
            return self.task_entries

    def get_list_of_phone_numbers(self):
        list_of_phones = "Phones "
        for i in self.diary_entries:
            list_of_phones += f"Tel num: {i.get_mobile_number()} "
        return ''.join(list_of_phones)

    def find_best_entry_for_reading_time(self, wpm, minutes):
        word_per_time = wpm * minutes
        result = [x for x in self.diary_entries if x.count_words() <= word_per_time]
        return sorted(result, key = lambda x : x.count_words())[-1]