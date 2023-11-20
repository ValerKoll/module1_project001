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

    
    def get_songs_ls(self):
        if not len(self.__songs_dict):
            return None
        list_to_print = [(f"#{key} - {item['author'].upper()}: {item['title']}") for key, item in self.__songs_dict.items() if item['listen']==True]
        return list_to_print
    
    def get_songs_notls(self):
        if not len(self.__songs_dict):
            return None
        list_to_print = [(f"#{key} - {item['author'].upper()}: {item['title']}") for key, item in self.__songs_dict.items() if item['listen']==False]
        return list_to_print

    def flag_songs(self, song_number):
        if song_number > self.__counter:
            raise Exception("No song in the database")
        self.__songs_dict[str(song_number)]['listen'] = True