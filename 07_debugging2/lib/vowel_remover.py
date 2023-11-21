class VowelRemover:
    def __init__(self, text):
        self.text = text
        self.vowels = ["a", "e", "i", "o", "u"]

    def remove_vowels(self):
        i = 0
        while i < len(self.text):
            if self.text[i].lower() in self.vowels:
                self.text = self.text[:i] + self.text[i+1:]
                i -= 1
            i += 1
        return self.text
    
    

remover = VowelRemover("We will remove the vowels from this sentence.")
result_no_vowels = remover.remove_vowels()
if result_no_vowels == "W wll rmv th vwls frm ths sntnc.":
    print("OK")
remover = VowelRemover("ab")
result_no_vowels = remover.remove_vowels()
if result_no_vowels == "b":
    print("OK")