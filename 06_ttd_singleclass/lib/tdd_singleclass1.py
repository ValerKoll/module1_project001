class Tasks():
    def __init__(self):
       self.tasks_dict = {}
       self.__index = 0
       
    def add_tasks(self, title_to_add, content_to_add):
        if title_to_add == "":
            title_to_add = "Untitled"
        if content_to_add == "":
            return None
        self.__index += 1
        self.tasks_dict[str(self.__index)] = {'Title':title_to_add, 'content':content_to_add, 'completed':False}
        return "Entry Added"
    
    def get_tasks(self):
        if not len(self.tasks_dict):
            return "List Empty"
        text_to_print = "\033[0;31m==== TASK NOT COMPLETED ====\n"
        text_to_print += ''.join([
            (f"#{key} - {item['Title'].upper()}: {item['content']}\n") for key, item in self.tasks_dict.items() if item['completed']==False])
        text_to_print += "\033[0;36m==== TASK COMPLETED ====\n"
        text_to_print += ''.join([
            (f"#{key} - {item['Title'].upper()}: {item['content']}\n") for key, item in self.tasks_dict.items() if item['completed']==True])
        return text_to_print
    
    def flag_completed(self, task_id):
        self.tasks_dict[str(task_id)]['completed'] = True
    
    
    
    
    
    
    
    
t = Tasks()
t.add_tasks("Wsdsd", "Wsdsd")
t.add_tasks("Ws", "skdlsjdlkjsld;")
t.add_tasks("Not", "skdlsjdlkjsld;")
t.add_tasks("YES", "skdlsjdlkjsld;")
t.add_tasks("But", "skdlsjdlkjsld;")
print(t.get_tasks2())
t.flag_completed(2)
print(t.get_tasks2())
t.flag_completed(4)
print(t.get_tasks2())
