def reading_time(text):
    #if type(text) != str:
    #    raise Exception("Error")
    #if text == "":
    #    return 0
    if any([type(text) != str, text == ""]):
        raise Exception("Error")
    #if type(text) != str:
        
    words_count = text.split(" ")
    return round(len(words_count)/200,1)