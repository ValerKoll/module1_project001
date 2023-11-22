def reading_chunk(contents, wpm, minutes):
        # set variables
        words_list = contents.split(" ")
        words_chuck_start = 210
        words_count_chunk = int(round(wpm * minutes, 0))
        # actions
        if words_chuck_start == 0:
            words_chuck_end = words_count_chunk        
        words_chuck_end = words_chuck_start + words_count_chunk
        if words_chuck_end > len(words_list):
            words_chuck_end = -1
            index_chunk = 0
        return " ".join(words_list[words_chuck_start:words_chuck_end])

text_exemple_210ws = "one two thr fou fiv six sev eig nin ten one two thr fou fiv six sev eig nin ten one two thr fou fiv six sev eig nin ten one two thr fou fiv six sev eig nin ten one two thr fou fiv six sev eig nin ten one two thr fou fiv six sev eig nin ten one two thr fou fiv six sev eig nin ten one two thr fou fiv six sev eig nin ten one two thr fou fiv six sev eig nin ten one two thr fou fiv six sev eig nin ten one two thr fou fiv six sev eig nin ten one two thr fou fiv six sev eig nin ten one two thr fou fiv six sev eig nin ten one two thr fou fiv six sev eig nin ten one two thr fou fiv six sev eig nin ten one two thr fou fiv six sev eig nin ten one two thr fou fiv six sev eig nin ten one two thr fou fiv six sev eig nin ten one two thr fou fiv six sev eig nin ten one two thr fou fiv six sev eig nin ten one two thr fou fiv six sev eig nin ten"


print(f"""
   Running: 
   Expected: "Diary Entry (date):The next time
   Actual: {reading_chunk(text_exemple_210ws, 98, 1.2)} 
""")


list1 = ["one", "two", "thr", "fou", "fiv", "six", "sev", "eig", "nin"]
print(" ".join(list1[-2:len(list1)]))