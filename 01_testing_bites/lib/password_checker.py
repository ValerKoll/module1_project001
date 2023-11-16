class Present():
    def __init__(self) -> None:
        self.password = None
    
    def wrap(self, password):
        if self.password is not None:
            raise Exception("password is not empty") 
        self.password = password
        
    def check(self):
        if self.password == None:
            raise Exception("not set yet")
        return self.password
        #