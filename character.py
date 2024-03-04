# character.py

class Character():
    
    def __init__(self, name):
        # initialises the character object
        self.name = name
        self.description = None
        self.conversation = None
        
    def describe(self):
        # sends a description of the character to the terminal
        print(f"{self.name} is here, {self.description}")
        
    def talk(self):
        # send converstation to the terminal
        if self.conversation is not None:
            print(f"{self.name}: {self.conversation}")
        else:
            print(f"{self.name} doesn't want to talk to you")
    
    def hug(self):
        # the character responds to a hug
        print(f"{self.name} doesn't want to hug you")

    def fight(self,item):
        # the character response to a threat
        print(f"{self.name} doesn't want to fight you")
        return True


class Friend(Character):
    
    def __init__(self, name):
        # initialise the Friend object by calling the character initialise
        super().__init__(name)
        
    def hug(self):
        # the friend responds to a hug
        print(f"{self.name} hugs you back.")

        
class Enemy(Character):
    
    num_of_enemy = 0
    
    def __init__(self,name):
        # initialise the Enemy object by calling the character initialise
        super().__init__(name)
        self.weakness = None
        self.damage = 2
        self.health = 10
        Enemy.num_of_enemy += 1
        
        
    def fight(self, item):
        # fights enemy with provided item and returns if enemy is still alive
        # calculate hit amount
        if item == self.weakness:
            hit = item.damage * 5
        else:
            hit = item.damage
        
        # assess damage
        print(f"You hit {self.name} with {item.name} causing {hit} damage.")
        print(f"{self.name} has {self.health} health left")
        self.health -= hit
        
        if self.health <= 0:
            print(f"You have slained {self.name}.")
            Enemy.num_of_enemy -= 1
            return True, 0
        else:
            print(f"{self.name} strikes back doing {self.damage} damage.")
            return False, self.damage
    
    def get_num_of_enemy():
        return Enemy.num_of_enemy