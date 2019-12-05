from room import Room
from player import Player
import textwrap
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

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player(input("Please enter your name:  "), room['outside'], [])
 
while True:
   print(f"Current Location: {player.player_location.room_name[0]}\nDescription:  {player.player_location.room_description}" )
   print("\nTo move north enter 'n', south enter 's', east enter 'e', or to move west enter 'w'\n")
   player_move = input("Where would you like to go?  ")

   if(player_move == "n"):
    player.player_location = player.player_location.n_to
   elif(player_move == "s"):
    player.player_location = player.player_location.s_to
   elif(player_move == "e"):
    player.player_location = player.player_location.e_to
   elif(player_move == "w"):
    player.player_location = player.player_location.w_to
   elif(player_move == "q"):
       print('You have quit the game')
       break
       
    

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
