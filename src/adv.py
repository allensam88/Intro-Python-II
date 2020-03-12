from room import Room
from player import Player

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

# Make a new player object that is currently in the 'outside' room.
new_player = Player(
    "Senior Drill Instructor Gunnery Sergeant Hartmann", room['outside'])

# Initialize the game to begin with True (False to quit)
game = True

while game:
    print("Welcome to Heartbreak Cave!")
    # Waits for user input and decides what to do.
    coordinate = input(
        "Where to, Marine? [n] North, [e] East, [s] South, [w] West, or [q] Give up!   ")
    # If the user enters a cardinal direction, attempt to move to the room there.
    if coordinate in ['n', 'e', 's', 'w']:
        new_player.move(coordinate)
    # If the user enters "q", quit the game.
    elif coordinate == 'q':
        print("Many have tried and failed. Better luck next time!")
        game = False
    # If the user enters an invalid key stroke.
    else:
        print("Lost? Try again you piece of amphibian slime!")
