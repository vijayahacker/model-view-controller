class Mynumber:
    def __init__(self) :
        self.number = 0
    
    def getNumber(self):
        return self.number
    
    def IncrementNumber(self):
        self.number +=1
class menuItems:
    def __init__(self):
        self.Nav = {"Home, settings, profiles"}
    
    def getMenuItems(self):
        return self.Nav
