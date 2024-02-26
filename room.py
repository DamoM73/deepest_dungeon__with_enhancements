# room.py

class Room():
    
    def __init__(self,room_name):
        # initialises the room object
        self.name = room_name.lower()
        self.description = None
        self.linked_rooms = {}
        self.character = None
        self.item = None
        self.locked = False
        
    def describe(self):
        # sends a description of the room to the terminal
        print(f"\nYou are in the {self.name}")
        print(self.description)
        if self.character is not None:
            self.character.describe()
        if self.item is not None:
            self.item.describe()
        for direction in self.linked_rooms.keys():
            print(f"To the {direction} is the {self.linked_rooms[direction].name}")
    
    def link_rooms(self, room, direction):
        # links the provided room, in the provided direction
        self.linked_rooms[direction.lower()] = room
        
    def move(self, direction):
        # returns the room linked in the given direction
        return self.linked_rooms[direction]
        
    def get_directions(self):
        # returns all the possible directions from this room
        return list(self.linked_rooms.keys())
    
    def is_locked(self, direction):
        return self.linked_rooms[direction].locked
    
    def unlock(self, direction):
        self.linked_rooms[direction].locked = False
        print("Door is unlocked.")