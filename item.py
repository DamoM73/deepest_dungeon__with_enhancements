# item.py
class Item():
    
    def __init__(self,name):
        # initialise the Item object
        self.name = name.lower()
        self.description = None
        self.damage = 1
        
    def describe(self):
        # prints description of item to the terminal
        return f"\nYou see {self.name} in the room. It is {self.description}."
        