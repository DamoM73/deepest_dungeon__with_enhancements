# character.py
import ollama

class Character():
    
    def __init__(self, name, model):
        # initialises the character object
        self.name = name
        self.description = None
        self.conversation = None
        self.client = ollama.Client()
        if model is not None:
            self.model = model
        else:
            self.model = "phi"
        print(f"{self.name} using {self.model}")
        
    def describe(self):
        # sends a description of the character to the terminal
        return f"\n{self.name} is here, {self.description}"
        
    def talk(self):
        # send converstation to the terminal
        if self.conversation is not None:
            response = self.client.generate(model=self.model, prompt="Who are you?")
            return(self.name, response.response)
        else:
            return(self.name, "Doesn't want to talk to you")
    
    def hug(self):
        # the character responds to a hug
        return(self.name, "Doesn't want to hug you")

    def fight(self,item):
        # the character response to a threat
        return(True, -1, f"{self.name} doesn't want to fight you")
        
            


class Friend(Character):
    
    def __init__(self, name, model=None):
        # initialise the Friend object by calling the character initialise
        super().__init__(name, model)
        
    def hug(self):
        # the friend responds to a hug
        return(self.name, "Hugs you back.")

        
class Enemy(Character):
    
    num_of_enemy = 0
    
    def __init__(self,name, model=None):
        # initialise the Enemy object by calling the character initialise
        super().__init__(name, model)
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
        message = ""
        message += f"You hit {self.name} with {item.name} causing {hit} damage."
        message += f"\n{self.name} has {self.health} health left."
        self.health -= hit
        
        if self.health <= 0:
            message += f"\nYou have slained {self.name}."
            Enemy.num_of_enemy -= 1
            return True, 0, message
        else:
            message += f"\n{self.name} strikes back doing {self.damage} damage."
            return False, self.damage, message
    
    def get_num_of_enemy():
        return Enemy.num_of_enemy