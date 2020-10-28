class User:

    def __init__(self, username, name, password):
        self.username = username
        self.name = name
        self.password = password
    
    def getUsername(self):
        return self.username

    def getName(self):
        return self.name
    
    def getPassword(self):
        return self.password
    
    def setUsername(self, username):
        self.username = username 

    def setName(self, name):
        self.name = name 
    
    def setPassword(self, password):
        self.password = password