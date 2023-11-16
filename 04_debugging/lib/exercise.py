def say_hello(name):
    return f"hello {name}"


# EXERCISE 2
def encode(text, key):
    cipher = make_cipher(key)
    ciphertext_chars = []
    for i in text:
        ciphered_char = chr(65 + cipher.index(i))
        print(f"{i} - {ciphered_char}")
        ciphertext_chars.append(ciphered_char)
    # === check ===
    print(ciphertext_chars)
    # =============

    return "".join(ciphertext_chars)


def decode(encrypted, key):
    cipher = make_cipher(key)

    plaintext_chars = []
    for i in encrypted:
        plain_char = cipher[ord(i) - 65]
        plaintext_chars.append(plain_char)

    return "".join(plaintext_chars)


def make_cipher(key):
    # set the lowercase alphabet
    alphabet = [chr(i + 97) for i in range(0, 26)]
    # list of key letters + alphabet
    cipher_with_duplicates = list(key) + alphabet
    # list where to save resulted list
    cipher = []
    # go thorugh the list from 0 to all the letters  (26 letter + len of key)
    for i in range(0, len(cipher_with_duplicates)):
        # add only uniqie letter in new order
        if cipher_with_duplicates[i] not in cipher_with_duplicates[:i]:
            cipher.append(cipher_with_duplicates[i])

    return cipher

#res = make_cipher("key")
# alpha = list("abcdefghijklmnopqrstvuwyz")
# assert res == alpha

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