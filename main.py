# main.py

from room import Room
from character import Enemy, Friend
from item import Item
from player import Player
from display import Display

# create display
display = Display()

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
    display.message(current_room.describe())
    
    command = input("> ").lower()
    
    # move
    if command in current_room.get_directions():
        if not current_room.is_locked(command):
            current_room = current_room.move(command)
            display.action(f"You travel {command}")
        else:
            display.action("Room is locked")
    # unlock
    elif command == "unlock":
        door = input("Which room do you want to unlock? > ").lower()
        if door in current_room.get_directions():
            if current_room.is_locked(door):
                if player.item_in_backpack("key"):
                    current_room.unlock(door)
                else:
                    display.action("You do not have a key")
            else:
                display.action("That door is not locked")
        else:
            display.action("There is no door in that direction")
            
    # talk
    elif command == "talk":
        if current_room.character is not None:
            display.converse(current_room.character.talk())
        else:
            display.action("There is no one here to talk to")
    # hug
    elif command == "hug":
        if current_room.character is not None:
            display.converse(current_room.character.hug())
        else:
            display.message("There is no one here to hug")
    # fight
    elif command== "fight":
        if current_room.character is not None:
            display.action("What will you fight with?")
            choice = input("> ").lower()
            weapon = player.item_in_backpack(choice)
            if weapon:
                win, hurt, message = current_room.character.fight(weapon)
                display.fight(message)
                if win and hurt > 0:
                    if Enemy.num_of_enemy == 0:
                        display.fight("You have slain the enemy. You are victorious!")
                        running = False
                else:
                    alive = player.damage(hurt)
                    display.fight(f"You have {player.health} health left.")
                    if not alive:
                        display.fight("You have been killed")
                        running = False
            else:
                display.fight(f"You don't have {choice}")
                display.fight(f"{current_room.character.name} strikes you down.")
                running = False
        else:
            display.action("There is no one here to fight")
    # take
    elif command == "take":
        if current_room.item is not None:
            display.action(player.take_item(current_room.item))
            current_room.item = None
        else:
            display.action("There is nothing here to take")
    # backpack
    elif command == "backpack":
        display.action(player.show_inventory())
    # help
    elif command == "help":
        message = ""
        message += "Type which direction you wish to move,\n"
        message += "or use one of these commands:\n"
        message += " - Unlock\n"
        message += " - Talk\n"
        message += " - Fight\n"
        message += " - Hug\n"
        message += " - Take\n"
        message += " - Backpack"
        display.message(message)
    # quit
    elif command == "quit":
        running = False
    # incorrect command
    else:
        display.message("Enter 'help' for list of commands")
    
display.message("Thank you for playing Darkest Dungeon")