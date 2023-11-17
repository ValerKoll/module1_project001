from lib.td_challange import *

def test_check_correct_given_text():
    grammar = GrammarStats()
    result = grammar.check("This could be our the next chapter in life.")
    assert result == True
    result = grammar.check("this could be our the next chapter in life.")
    assert result == False
    result = grammar.check("This could be our the next chapter in life-")
    assert result == False

## Given multple texts in sequenze - check if multple entries have been stored within the class
def test_given_tests_are_stored():
    grammar = GrammarStats()
    grammar.check("This could be our the next chapter in Boston?")   #VALID
    grammar.check("This could be our the next chapter in San Francisco.")  #VALID
    grammar.check("This could be our the next chapter in New York!")   #VALID
    grammar.check("This could be our the next chapter in Las Vegas.")  #VALID
    grammar.check("This could be our the next chapter in Miami")  #NOT VALID
    assert len(grammar.added_tests) == 4

## Given multple texts in sequenze - returns a % of correct entries based on the whole dataset
def test_given_tests_return_percentage():
    grammar = GrammarStats()
    grammar.check("This could be our the next chapter in Boston.")          #VALID
    grammar.check("This could be our the next chapter in San Francisco?")   #VALID
    grammar.check("This could be our the next chapter in New York.")        #VALID
    grammar.check("This could be our the next chapter in Las Vegas.")       #VALID
    grammar.check("this could be our the next chapter in New York.")        #NOT VALID
    grammar.check("This could be our the next chapter in Las Vegas.")       #VALID
    grammar.check("This could be our the next chapter in Miami")            #NOT VALID
    grammar.check("This could be our the next chapter in Las Vegas!")       #VALID
    grammar.check("This could be our the next chapter in New York")         #NOT VALID
    result = grammar.percentage_good()
    assert result == "66%"