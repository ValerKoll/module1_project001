def count_words(text):
    if type(text) != str or len(text) == 0:
        return 0
    divided_str = text.split()
    return len(divided_str)