class Todo:
    # Public Properties:
    #   task: a string representing the task to be done
    #   complete: a boolean representing whether the task is complete

    def __init__(self, task):
        self.task = task
        self.flag = False
        # Parameters:
        #   task: a string representing the task to be done
        # Side-effects:
        #   Sets the task property
        #   Sets the complete property to False
        

    def mark_complete(self):
        self.flag = True
        # Returns:
        #   Nothing
        # Side-effects:
        #   Sets the complete property to True
        

