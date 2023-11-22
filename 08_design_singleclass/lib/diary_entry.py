class DiaryEntry:
    # Public Properties:
    #   title: a string
    #   contents: a string

    def __init__(self, title, contents): # title, contents are strings
        self.title = title
        self.contents = contents
        self.index_chunk = 0

    def count_words(self):
        if type(self.contents) != str or len(self.contents) == 0:
            return 0
        divided_str = self.contents.split()
        return len(divided_str)

    def reading_time(self, wpm):
        if any([type(self.contents) != str, self.contents == ""]):
            raise Exception("Error")
        words_count = self.contents.split(" ")
        return round(len(words_count)/wpm, 1)
        # Parameters:
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        # Returns:
        #   An integer representing an estimate of the reading time in minutes
        #   for the contents at the given wpm.
        pass

    def reading_chunk(self, wpm, minutes):
        text_exemple_210ws = "one two thr fou fiv six sev eig nin ten one two thr fou fiv six sev eig nin ten one two thr fou fiv six sev eig nin ten one two thr fou fiv six sev eig nin ten one two thr fou fiv six sev eig nin ten one two thr fou fiv six sev eig nin ten one two thr fou fiv six sev eig nin ten one two thr fou fiv six sev eig nin ten one two thr fou fiv six sev eig nin ten one two thr fou fiv six sev eig nin ten one two thr fou fiv six sev eig nin ten one two thr fou fiv six sev eig nin ten one two thr fou fiv six sev eig nin ten one two thr fou fiv six sev eig nin ten one two thr fou fiv six sev eig nin ten one two thr fou fiv six sev eig nin ten one two thr fou fiv six sev eig nin ten one two thr fou fiv six sev eig nin ten one two thr fou fiv six sev eig nin ten one two thr fou fiv six sev eig nin ten one two thr fou fiv six sev eig nin ten"
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
        # Parameters:
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   A string representing a chunk of the contents that the user could
        #   read in the given number of minutes.
        # If called again, `reading_chunk` should return the next chunk,
        # skipping what has already been read, until the contents is fully read.
        # The next call after that it should restart from the beginning.
        pass

