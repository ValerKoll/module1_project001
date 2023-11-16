from lib.exercise import * 
# Intended output:
#
# > say_hello("kay")
# => "hello kay"
def test_given_name_return_helloname():
    result = say_hello('Ethor')
    assert result == "hello Ethor"
    
   

# EXERCISE 2
# When you run this file, these next lines will show you the expected
# and actual outputs of the functions above.
'''
print(f"""
 Running: encode("theswiftfoxjumpedoverthelazydog", "secretkey")
Expected: EMBAXNKEKSYOVQTBJSWBDEMBPHZGJSL
  Actual: {encode('theswiftfoxjumpedoverthelazydog', 'secretkey')}
""")

print(f"""
 Running: decode("EMBAXNKEKSYOVQTBJSWBDEMBPHZGJSL", "secretkey")
Expected: theswiftfoxjumpedoverthelazydog
  Actual: {decode('EMBAXNKEKSYOVQTBJSWBDEMBPHZGJSL', 'secretkey')}
""") 

'''
#def test_make_chiper():
##    res = make_cipher("")
 #   alpha = list("abcdefghijklmnopqrstvuwyz")
 #   assert res == alpha
def test_encode():
    reusult = encode("theswiftfoxjumpedoverthelazydog", "secretkey")
    assert reusult == "EMBAXNKEKSYOVQTBJSWBDEMBPHZGJSL"
def test_decode():
    result = decode("EMBAXNKEKSYOVQTBJSWBDEMBPHZGJSL", "secretkey")
    assert result == "theswiftfoxjumpedoverthelazydog"
