from datetime import datetime
 
class DiaryEntry:    
    def __init__(self, title, contents):
        self.title = title
        self.contents = contents
        self.index_chunk = 0

    def format(self):
        errors_checklist = [
            self.contents == "",
            self.title == "" and self.contents == "",
            self.title == None and self.contents == None
            ]
        if any(errors_checklist):
            return None
        if self.title == "":
            self.title = f"Diary Entry 12-12-2022"
        new_content = [s.lower() if len(s) > 1 else s for s in self.contents.split(" ")]
        new_content[0] = new_content[0].capitalize()
        new_content = " ".join(new_content)
        return f"{self.title.title()}: {new_content}"

    def count_words(self):
        if self.contents == None or self.contents == "":
            return None
        return len(self.contents.split(" "))

    def reading_time(self, wpm):
        if wpm == 0:
            return "are you asleep?"
        return round(len(self.contents.split(" ")) / wpm, 1)

    def reading_chunk(self, wpm, minutes):
        # set variables
        words_list = self.contents.split(" ")
        words_chuck_start = self.index_chunk
        words_count_chunk = int(round(wpm * minutes, 0))
        # actions
        words_chuck_end = words_chuck_start + words_count_chunk
        self.index_chunk = words_chuck_end
        #if words_chuck_end != 0:
            
        if words_chuck_end > len(words_list):   ###ERROR HERE!!!
            words_chuck_end = len(words_list)
            self.index_chunk = 0
        print(f"{len(words_list)} chuck: {words_count_chunk}, s:{words_chuck_start}, e{words_chuck_end}")
        return " ".join(words_list[words_chuck_start:words_chuck_end])

text_exemple_210ws = "one two thr fou fiv six sev eig nin ten one two thr fou fiv six sev eig nin ten one two thr fou fiv six sev eig nin ten one two thr fou fiv six sev eig nin ten one two thr fou fiv six sev eig nin ten one two thr fou fiv six sev eig nin ten one two thr fou fiv six sev eig nin ten one two thr fou fiv six sev eig nin ten one two thr fou fiv six sev eig nin ten one two thr fou fiv six sev eig nin ten one two thr fou fiv six sev eig nin ten one two thr fou fiv six sev eig nin ten one two thr fou fiv six sev eig nin ten one two thr fou fiv six sev eig nin ten one two thr fou fiv six sev eig nin ten one two thr fou fiv six sev eig nin ten one two thr fou fiv six sev eig nin ten one two thr fou fiv six sev eig nin ten one two thr fou fiv six sev eig nin ten one two thr fou fiv six sev eig nin ten one two thr fou fiv six sev eig nin ten"
dEntry = DiaryEntry("re", text_exemple_210ws)

print(f"""
   Running: 
   Expected: "Diary Entry (date):The next time
   Actual: {dEntry.reading_chunk(98, 1.2)} 
""")
print(f"""
   Running: 
   Expected: "Diary Entry (date):The next time
   Actual: {dEntry.reading_chunk(98, 1.2)} 
""")
print(f"""
   Running: 
   Expected: "Diary Entry (date):The next time
   Actual: {dEntry.reading_chunk(98, 1.2)} 
""")
