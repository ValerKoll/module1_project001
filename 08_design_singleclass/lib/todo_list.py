class TodoList:
    def __init__(self):
        self.todolist = []

    def add(self, todo):
        self.todolist.append(todo)
        # Parameters:
        #   todo: an instance of Todo
        # Returns:
        #   Nothing
        # Side-effects:
        #   Adds the todo to the list of todos
         
    def incomplete(self):
        return [i for i in self.todolist if i.flag == False]
        # Returns:
        #   A list of Todo instances representing the todos that are not complete

    def complete(self):
        return [i for i in self.todolist if i.flag == True]
        # Returns:
        #   A list of Todo instances representing the todos that are complete

    def give_up(self):
        for i in self.todolist:
            i.mark_complete()
        # Returns:
        #   Nothing
        # Side-effects:
        #   Marks all todos as complete
    