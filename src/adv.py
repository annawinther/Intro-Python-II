from room import Room
from player import Player
# Declare all the rooms


name = input("What is the name of your character: ")

print(f"Let's begin your adventure, {name}!")

room = {
    'outside': Room("Outside Cave Entrance",
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

#
# Main
#


player = Player(name, room['outside'])
starting_room = player.room
print(f'You start here: {starting_room}')
# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

while True:
    direction = input("Where do you want to go? Enter [n] North, [s] South, [e] East, or [w] West. Press [q] Quit to quit.\n")
    print(f"You're here: {player.room}")

    if direction == "n":
        if player.room.n_to != 0:
            player.room = player.room.n_to
        else: 
            print("There is no room that direction. Please select another direction")
        
    if direction == "e":
        if player.room.e_to != 0:
            player.room = player.room.e_to
        else: 
           print("There is no room that direction. Please select another direction")
        
    if direction == "w":
        if player.room.w_to != 0:
            player.room = player.room.w_to
        else: 
            print("There is no room that direction. Please select another direction")

    if direction == "s":
        if player.room.s_to != 0:
           player.room = player.room.s_to
        else: 
           print("There is no room that direction. Please select another direction")
 
    if direction == "q":
            break