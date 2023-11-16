def check_todos(text):
    if any([text == "", text == None]):
        raise Exception("The input parameter is not valid!")
    if '#TODO' not in text:
        return ""
    else:
        index = text.find('#TODO')
        text = text[index + 5:].split('.')
        return text[0].lstrip()