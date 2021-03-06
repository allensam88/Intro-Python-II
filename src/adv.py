import os
from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

# Initialize new player object that is currently in the 'outside' room.


# Initialize items

item = {
    'garbage': Item("garbage", "a steaming hot pile."),
    'bayonet': Item("bayonet", "a long, sharp bayonet, but with no rifle..."),
    'rifle': Item("rifle", "an M-16 A2 service rifle."),
    'grenade': Item("grenade", "is it live or a dud?"),
    'trap': Item("tripwire", "watch yourself, it's a booby trap."),
    'boot': Item("boot", "a single left boot, size 9."),
    'skull': Item("skull", "a dried cracked skull, many have been here before..."),
    'mushroom': Item("mushroom", "does it possess magical powers?")
}
# Link items to rooms
room['outside'].items.append(item['garbage'])
room['foyer'].items.append(item['bayonet'])
room['overlook'].items = [item['rifle'], item['grenade']]
room['narrow'].items = [item['trap'], item['boot']]
room['treasure'].items = [item['skull'], item['mushroom']]

# Initialize the game to begin with True (False to quit)
game = True
# Opening message
print('\n***** WELCOME TO HEARTBREAK CAVE... ENTER AT YOUR OWN RISK! *****\n')
new_player = Player(input('Enter player name: '), room['outside'])
print('-----------------------------------------------------------------\n')
print(f"Location: {room['outside'].name}\n")
print(f"{room['outside'].description}\n")
room['outside'].display_items()

while game:
    os.system('cls')
    print(
        'Where to next, Marine? [n] North, [e] East, [s] South, [w] West')
    print('(or press [q] to GIVE UP!)\n')
    command = input('Enter command ~~> ')
    if command in ['n', 'e', 's', 'w']:
        new_player.move(command)
    elif command.startswith('grab'):
        item = command.split(' ')[1]
        new_player.grab_item(item)
    elif command.startswith('drop'):
        item = command.split(' ')[1]
        new_player.drop_item(item)
    elif command == 'i':
        new_player.display_inventory()
    elif command == 'q':
        print('\nMany have tried and failed. Better luck next time!\n')
        game = False
    else:
        print('Lost? Try again you piece of amphibian slime!\n')
