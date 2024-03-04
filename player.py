# player.py

class Player():
    
    def __init__(self):
        self.backpack = []
        self.health = 10
        
    def take_item(self, item):
        self.backpack.append(item)
        print(f"You put {item.name} into your backpack")
        
    def show_inventory(self):
        if self.backpack == []:
            print("It is empty")
        else:
            print("You have:")
            for item in self.backpack:
                print(f"- {item.name.capitalize()}")
                
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