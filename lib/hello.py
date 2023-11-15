def hello(a):
    return f"Hello {a}!"

def report_lenght(a , b):
    #length = len(str)
    return a+b


class StringBuilder:
    def __init__(self):
        self.str = ""

    def add(self, str):
        self.str += str

    def size(self):
        return len(self.str)

    def output(self):
        return self.str
    
class Gratitudes:
    def __init__(self):
        self.gratitudes = []

    def add(self, gratitude):
        self.gratitudes.append(gratitude)

    def format(self):
        formatted = "Be grateful for: "
        formatted += ", ".join(self.gratitudes)
        return formatted
    
    
class Reminder:
    def __init__(self, name):
        self.name = name
        self.task = None

    def remind_me_to(self, task):
        self.task = task

    def remind(self):
        # Look here! We want to fail if there is no reminder yet.
        if self.task is None:
            raise Exception("No reminder set!")
        return f"{self.task}, {self.name}!"


