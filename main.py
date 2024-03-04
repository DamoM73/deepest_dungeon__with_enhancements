# main.py

from room import Room
from character import Enemy, Friend
from item import Item
from player import Player

# create player
player = Player()

# create rooms
cavern = Room("Cavern")
cavern.description = "A room so big that the light of your torch doesn’t reach the walls."

armoury = Room("Armoury")
armoury.description = "The walls are lined with racks that once held weapons and armour."

lab = Room("Laboratory")
lab.description = "A strange odour hangs in a room filled with unknownable contraptions."

dimension = Room("Another dimension")
dimension.description = "This place is weird. You feel like your insides are on your outside."

gaol = Room("Gaol")
gaol.description = "There cells with skeletons chained to the wall. Rats scamper out of the way.\nAt fist you think the dripping sound is water, then the smell tells you it's sewage."
gaol.locked = True

# link rooms
cavern.link_rooms(armoury,"south")
armoury.link_rooms(cavern,"north")
armoury.link_rooms(lab,"east")
armoury.link_rooms(gaol,"down")
gaol.link_rooms(armoury,"up")
lab.link_rooms(armoury,"west")
lab.link_rooms(dimension,"portal")
dimension.link_rooms(lab,"portal")

# create items
cheese = Item("Cheese")
cheese.description = "super smelly"

sword = Item("Sword")
sword.description = "very pointy and kind of hurty"
sword.damage = 2

elmo = Item("Elmo")
elmo.description = "wanting to be tickled"

key = Item("Key")
key.description = "This something that might unlock something else."

# add items to rooms
cavern.item = sword
armoury.item = elmo
lab.item = cheese
dimension.item = key

# create characters
ugine = Enemy("Ugine")
ugine.description = "a huge troll with rotting teeth."
ugine.weakness = cheese

nigel = Friend("Nigel")
nigel.description = "a burly dwarf with golden bead in woven through his beard."
nigel.conversation = "Well youngan, what are you doing here?"

# add characters to rooms
armoury.character = ugine
lab.character = nigel

# initialise variables
running = True
current_room = cavern
backpack = []

# ----- MAIN LOOP -----
while running:
    current_room.describe()
    
    command = input("> ").lower()
    
    # move
    if command in current_room.get_directions():
        if not current_room.is_locked(command):
            current_room = current_room.move(command)
            print(f"You travel {command}")
        else:
            print("Room is locked")
    # unlock
    elif command == "unlock":
        door = input("Which room do you want to unlock? > ").lower()
        if door in current_room.get_directions():
            if current_room.is_locked(door):
                if player.item_in_backpack("key"):
                    current_room.unlock(door)
                else:
                    print("You do not have a key")
            else:
                print("That door is not locked")
        else:
            print("There is no door in that direction")
            
    # talk
    elif command == "talk":
        if current_room.character is not None:
            current_room.character.talk()
        else:
            print("There is no one here to talk to")
    # hug
    elif command == "hug":
        if current_room.character is not None:
            current_room.character.hug()
        else:
            print("There is no one here to hug")
    # fight
    elif command== "fight":
        if current_room.character is not None:
            choice = input("What will you fight with? > ").lower()
            weapon = player.item_in_backpack(choice)
            if weapon:
                win, hurt = current_room.character.fight(weapon)
                if win:
                    if Enemy.num_of_enemy == 0:
                        print("You have slain the enemy. You are victorious!")
                        running = False
                else:
                    alive = player.damage(hurt)
                    print(f"You have {player.health} health left.")
                    if not alive:
                        print("You have been killed")
                        running = False
            else:
                print(f"You don't have {weapon}")
                print(f"{current_room.character.name} strikes you down.")
                running = False
        else:
            print("There is no one here to fight")
    # take
    elif command == "take":
        if current_room.item is not None:
            player.take_item(current_room.item)
            current_room.item = None
        else:
            print("There is nothing here to take")
    # backpack
    elif command == "backpack":
        player.show_inventory()
    # help
    elif command == "help":
        print("Type which direction you wish to move,")
        print("or use one of these commands:")
        print("- Unlock")
        print("- Talk")
        print("- Fight")
        print("- Hug")
        print("- Take")
        print("- Backpack")
    # quit
    elif command == "quit":
        running = False
    # incorrect command
    else:
        print("Enter 'help' for list of commands")
    input("\nPress <Enter> to continue")
    
print("Thank you for playing Darkest Dungeon")