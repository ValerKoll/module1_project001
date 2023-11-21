from lib.letter_counter import *



def test_given_correct_text_return_most_common():
    counter = LetterCounter("Digital Punki")
    result = counter.calculate_most_common()
    # Intended output:
    # [2, "i"]    
    assert result == [3, 'i']
        

def test_given_even_letters_return_none():
    counter = LetterCounter("Digtal Punk")
    result = counter.calculate_most_common()
    # Intended output:
    # [2, "i"]    
    assert result == [1, None]