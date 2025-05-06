

class Cell:
    def __init__(self, alive:bool=False):

        self.alive: bool = alive

    def __str__(self):
        if self.alive == True:
            return "🦠"
        elif self.alive == False:
            return "  "
    
    def isalive(self):
        return self.alive