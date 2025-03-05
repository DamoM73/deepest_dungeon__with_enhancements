# player.py

class Player():
    
    def __init__(self):
        self.backpack = []
        self.health = 10
        
    def take_item(self, item):
        self.backpack.append(item)
        return f"You put {item.name} into your backpack"
        
    def show_inventory(self):
        if self.backpack == []:
            return "It is empty"
        else:
            message = "You have:"
            for item in self.backpack:
                message += f"\n - {item.name.capitalize()}"
            return message
                
    def item_in_backpack(self, item_name):
        for item in self.backpack:
            if item.name == item_name:
                return item
        return None
        
    def damage(self, amount):
        self.health -= amount
        if self.health > 0:
            return True
        else:
            return False