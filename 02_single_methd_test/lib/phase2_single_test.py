def make_snipset(string):
    if type(string) != str:
        return None
    words = string.split(" ")
    if len(words) > 5:
        first_5 = words[:5]
        string = " ".join(first_5) + " ..."
    #if len(string) > 5:
    #    string = string[0:5]+'...'
    return string

print(make_snipset("22222"))