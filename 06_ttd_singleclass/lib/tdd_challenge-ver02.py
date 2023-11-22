class SongTracker():    
    def __init__(self):
        self.__songs_dict = {}
        self.__counter = 0
        
    def add_songs(self, author_to_add, title_to_add):
        if author_to_add == "":
            author_to_add == "Unknown"
        if title_to_add == "":
            return None
        self.__counter += 1
        self.__songs_dict[str(self.__counter)] = {'author':author_to_add, 'title':title_to_add, 'listen':False}
        return "Entry Added"

    def get_songs(self, listened_status = False):
        if not len(self.__songs_dict):
            return None
        return self.__format_text(listened_status)

    def flag_songs(self, song_number):
        if song_number > self.__counter:
            raise Exception("No song in the database")
        self.__songs_dict[str(song_number)]['listen'] = True
        
    #internal use functions
    def __format_text(self, flag_to_print):
        text_to_print = ""
        if flag_to_print:
            text_to_print += "\033[0;34m=== TO LISTEN ===\n"
            temp_list = [(f"#{key} - {item['author'].upper()}: {item['title']}\n") for key, item in self.__songs_dict.items() if item['listen'] == False]
            if len(temp_list):
                text_to_print += ''.join(temp_list)
            else:
                text_to_print += "Empty\n"
        text_to_print += "\033[0;32m=== LISTENED ===\n"
        temp_list = [(f"#{key} - {item['author'].upper()}: {item['title']}\n") for key, item in self.__songs_dict.items() if item['listen'] == True]
        if len(temp_list):
            text_to_print += ''.join(temp_list)
        else:
            text_to_print += "Empty\n"
        return text_to_print    
    

songs = SongTracker()
songs.add_songs("Jack", "Nothing is better than one")
songs.add_songs("Jon", "Pulka from east")
songs.add_songs("Mike", "Dance with the cows")
songs.add_songs("Paul", "The neverless time")

#print(songs.get_songs(True))
while True:
    print(songs.get_songs(True))
    i = int(input("\033[0;35mSong to flag: "))
    if i == 0:
        break
    songs.flag_songs(i)

