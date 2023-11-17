class GrammarStats:
    ending_punct_chars = [".","!","?"] 
    total_added_emtries = 0
    
    def __init__(self):
        self.added_tests = []
        pass
  
    def check(self, text: str):
        self.total_added_emtries += 1
        if any([
            text[0] != text[0].capitalize(),
            text[-1] not in self.ending_punct_chars
            ]):
            return False
        self.added_tests.append(text)
        return True
  
    def percentage_good(self):
        return f"{int((len(self.added_tests)/self.total_added_emtries)*100)}%"