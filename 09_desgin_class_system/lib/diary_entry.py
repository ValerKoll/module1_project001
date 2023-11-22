class DiaryEntry():
    index_chunk = 0
    list_of_prefix = [
        "020", "074", "077"
    ]
    
    def __init__(self, title, content):
        if title != "" and title != None:
            self.title = title
        else:
            self.title = "Untitled"
        self.content = content

    def count_words(self, ):
        if type(self.content) != str or len(self.content) == 0:
            return 0
        return len(self.content.split())

    def reading_time(self, wpm):
        if any([type(self.content) != str, self.content == ""]):
            return 0
        return round(len(self.content.split(" "))/wpm, 1)

    def reading_chunks(self, wpm, minutes):
        words_list = self.content.split(" ")
        words_chuck_start = self.index_chunk
        words_count_chunk = int(round(wpm * minutes, 0))
        # actions
        words_chuck_end = words_chuck_start + words_count_chunk
        self.index_chunk = words_chuck_end
        #if words_chuck_end != 0:
            
        if words_chuck_end > len(words_list):
            words_chuck_end = len(words_list)
            self.index_chunk = 0
        print(f"{len(words_list)} chuck: {words_count_chunk}, s:{words_chuck_start}, e{words_chuck_end}")
        return " ".join(words_list[words_chuck_start:words_chuck_end])

    def get_mobile_number(self):
        for i in self.list_of_prefix:
            if i in self.content:
                start = self.content.index(i)
                end = (self.content[start:] + " ").index(" ")
                return self.content[start:start+end]
        return None
    
#diary = Diary()
diaryentry = DiaryEntry("Today", "The soon the better 07723232300")
diaryentry.get_mobile_number()