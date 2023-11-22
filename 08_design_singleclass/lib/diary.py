class Diary:
    def __init__(self):
        self.diaryentry = []

    def add(self, entry):
        self.diaryentry.append(entry)
        # Parameters:
        #   entry: an instance of DiaryEntry
        # Returns:
        #   Nothing
        # Side-effects:
        #   Adds the entry to the entries list
        
    def all(self):
        return self.diaryentry
        # Returns:
        #   A list of instances of DiaryEntry

    def count_words(self):
        counter = 0
        for i in self.diaryentry:
            counter += i.count_words()
        return counter
        # Returns:
        #   An integer representing the number of words in all diary entries
        # HINT:
        #   This method should make use of the `count_words` method on DiaryEntry.


    def reading_time(self, wpm):
        counter = self.count_words()
        return counter / wpm
        # Parameters:
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        # Returns:
        #   An integer representing an estimate of the reading time in minutes
        #   if the user were to read all entries in the diary.


    def find_best_entry_for_reading_time(self, wpm, minutes):
        diaryentry = []
        word_per_time = wpm * minutes
        #for i in self.diaryentry:
        result = [x for x in self.diaryentry if x.count_words() <= word_per_time]
        return sorted(result, key = lambda x : x.count_words())[-1]

        #return result[0]
        # Parameters:
        #   wpm:     an integer representing the number of words the user can
        #            read per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   An instance of DiaryEntry representing the entry that is closest to,
        #   but not over, the length that the user could read in the minutes
        #   they have available given their reading speed.

