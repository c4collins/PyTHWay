# This is a simple text-based game

# start setting up variables
room1 = [1, "Entryway", "Three fat [M]ice", "A small wooden door to outside to the [N]orth", "A passageway leading [S]outh", "A stone door blocked off by the fat mice going [E]ast"]
room1_mice = True
room2 = [2, "Garage", "Two [C]loth sacks", "Two [V]enomous snakes", "A stone door leading [W]est, back to the Entryway", "A passageway leading [E]ast.", "A rope bridge leading to the [S]outh."]
room2_snakes = True
room2_sacks = True
room3 = [3, "Hallway", "One UGLY [O]gre", "A passage going east at the [N]orth end of the room", "A passage going east at the [S]outh end of the room", "A passage going [W]est"]
room3_ogre = True
room4 = [4, "Storage Closet", "One large ooze... no, wait... Six small [O]ozes.", "A passage going [E]ast"]
room4_ooze = True
room5 = [5, "Secret Stash", "Three crates of Sandorian [W]hiskey.  Woohoo!", "A return passage through the shattered [M]irror"]
room5_whiskey = True
room6 = [6, "Cathouse", "A huge three-headed [L]ion.", "A passageway leading [N]orth"]
room6_lion = True
room7 = [7, "Courtyard", "A bowl of petunias that appears to have fallen from the sky."]
room8 = [8, "Pinnacle", "A [D]ragon.", "If there is anything else in the room, it's behind the fucking dragon."]
room8_dragon = True
room9 = [9, "Treasure Room", "A large chest overflowing with Gold [C]oins!"]
room9_coins = True
room10 = [10, "Gauntlet", "Two [P]ikemen", "Two [A]rchers", "A [B]alrog - A spirit of fire born from the ancient world"]
room10_pikemen = True
room10_archers = True
room10_balrog = True
room11 = [11, "Hidden Funds", "A small [S]afe."]
room11_safe = True
current_room = 0
# Stop setting up variables

# Start setting up functions
def start():
    """Initialies the game, essentially just showing the title, and that little blurb about how I'm not sure I'm doing this right, but could eventually include randomized rooms or loot or something too, so as to give a new game every time instead of the same map."""
    print "\n\n\t\t    Welcome to The Dungeon!"
    print """
    There are some basic rules that need to be followed here because I'm not a great programmer.  
    From each room, you might have the option of going in a direction, or taking any number of 
    other options to respond to whatever is in the room - monsters, or treasure, or anything 
    else!\n
    * For now, simple directions will be bracketed, as in, 'You can travel [N]orth or [S]outh 
    from here, you can also [F]ight the snakes or [L]ook through the bags.' 
    """

def enter_room(room_contents):
    """This function splits the room's list of data into the current_room, room_name, and room_contents. current_room is the room's ID number, room_name is the name of the room, "Entryway" for example, and room_contents is a list containing all of the items seen when you look around the room, i.e. ["Cleese", "Gilliam", "Jones"]"""
    global current_room
    current_room = room_contents.pop(0)
    room_name = room_contents.pop(0)
    print "\n As you stand in the doorway of The %s, you look around and see:\n" % room_name
    for x in room_contents:
        print "  * ", x
    print "\n"

def dead(cause):
    """Ends the game and answers the question - How did you die?"""
    global current_room
    current_room = "dead"
    print "\n\tYou have died from: %r\n\n" % cause
    print "\t\tGAME OVER\n\n"
        
# Stop setting up functions

#Start of active code

start()

while current_room != "dead":
    if current_room == 0:
        print "\tYou come across a small wooden door embedded in a boulder on the side of a hill."
        print "\tYou say, 'Strange, I don't remember seeing that before.'  Of course, you just appeared here in front of the door just now, and haven't ever seen anything before.  So there's that.\n"
        print "\tDo you [K]nock on the door, [B]odyslam the door open, [S]neak in quietly, or [R]un away?"
        command = raw_input(" > ")
        if command == "K":
            print """
            A huge, three-headed lion answers the door, and politely asks you to please leave 
            the premises before he is forced to call upon the authorities.  Taking advantage 
            of his perceived docility, you cheekily reply, 'What authorities?  I'm the 
            goddamned Emperor!'
            
            The lion flashes you a grin and jumps on you with a ferocious roar.
            """
            dead("being a lion's breakfast.")
        elif command == "B":
            print """
            You bounce right off the door, making a very loud noise, almost as if you'd tried 
            knocking on the door.
            """
            print """
            A huge, three-headed lion answers the door, and politely asks you to please leave 
            the premises before he is forced to call upon the authorities.  Taking advantage 
            of his perceived docility, you cheekily reply, 'What authorities?  I'm the 
            goddamned Emperor!'
            
            The lion flashes you a grin and jumps on you with a ferocious roar.
            """
            dead("being a lion's breakfast.")
        elif command == "S":
            print "\tYou sneak into the cave very quietly.  Good work!"
            enter_room(room1)
        elif command == "R":
            print "\tCoward"
            dead("Old age. PSH.")
        else:
            print "\tThat's not one of the commands.  They're in braces and capitals."
    elif current_room == 1:
        print "\tWhat do you do?\n"
        command = raw_input(" > ")
        if command == "E":
            if room1_mice == True:
                print "There are fat mice in the way."
            else:
                print "You walk past the dosed mice and push open the door, and stride bravely into the next room."
                enter_room(room2)
        elif command == "S":
            print "You take the passageway south"
            enter_room(room6)
        elif command == "N":
            print "As you flee you stub your toe."
            dead("Gangrene")
        elif command == "M":
            print "The fat mice appear to be sleeping quite soundly, so you employ the old 'chloroform trick' to make sure they stay that way."
            room1_mice = False
        else:
            print "\tThat's not one of the commands.  They're in braces and capitals."
    elif current_room == 2:
        print "\tWhat do you do?\n"
        command = raw_input(" > ")
        if command == "C":
            if room2_snakes == True:
                dead("The venomous snakes killed, ate, and enjoyed you.")
            else:
                print "In the first sack you find a pair of pants and a shirt, and in the second sack you find some shoes."
                print "\n--- You have obtained - Clothing ---\n--- You put on Clothing ---\n"
                print "Isn't that better?"
        elif command == "W":
            if room2_snakes == True:
                dead("The venomous snakes killed, ate, and enjoyed you.")
            else:
                print "You travel through the westward passage."
                enter_room(room1)
        elif command == "E":
            if room2_snakes == True:
                dead("The venomous snakes killed, ate, and enjoyed you.")
            else:
                print "You travel through the eastward passage."
                enter_room(room3)
        elif command == "S":
            if room2_snakes == True:
                dead("The venomous snakes killed, ate, and enjoyed you.")
            else:
                print "You travel through the southward passage."
                enter_room(room7)
        elif command == "V":
            if room2_snakes == True:
                print "You rush up to the snakes and stomp them both quickly.  They explode and destroy all your clothes."
                room2_snakes = False
                room2[3] = "Snake bits everywhere."
            else:
                print "You've already destroyed the snakes."
        else:
            print "\tThat's not one of the commands.  They're in braces and capitals."
    elif current_room == 3:
        print "\tWhat do you do?\n"
        command = raw_input(" > ")
        if command == "O":
            if room3_ogre == True:
                print "The ogre sees you running towards him and pulls out his wand.  Oh no, this is an ogre mage!"
                print "Then the ogre dematerializes himself, leaving you stunned."
                room3_ogre = False
                room3[2] = "A slight mist"
            else:
                print "The ogre has already been destroyed."
        elif command == "N":
            print "this command is not yet implemented"
        elif command == "W":
            print "this command is not yet implemented"
        elif command == "S":
            print "this command is not yet implemented"
        else:
            print "\tThat's not one of the commands.  They're in braces and capitals."
    elif current_room == 4:
        print "\tWhat do you do?\n"
        command = raw_input(" > ")
        if command == "O":
            print "this command is not yet implemented"
        elif command == "F":
            print "this command is not yet implemented"
        elif command == "E":
            print "this command is not yet implemented"
        else:
            print "\tThat's not one of the commands.  They're in braces and capitals."
    elif current_room == 5:
        print "\tWhat do you do?\n"
        command = raw_input(" > ")
        if command == "M":
            print "this command is not yet implemented"
        elif command == "W":
            print "this command is not yet implemented"
        else:
            print "\tThat's not one of the commands.  They're in braces and capitals."
    elif current_room == 6:
        print "\tWhat do you do?\n"
        command = raw_input(" > ")
        if command == "L":
            print "this command is not yet implemented"
        elif command == "N":
            print "this command is not yet implemented"
        elif command == "U":
            print "this command is not yet implemented"
        else:
            print "\tThat's not one of the commands.  They're in braces and capitals."
    elif current_room == 7:
        print "\tWhat do you do?\n"
        command = raw_input(" > ")
        if command == "N":
            print "this command is not yet implemented"
        elif command == "W":
            print "this command is not yet implemented"
        elif command == "E":
            print "this command is not yet implemented"
        elif command == "S":
            print "this command is not yet implemented"
        else:
            print "\tThat's not one of the commands.  They're in braces and capitals."
    elif current_room == 8:
        print "\tWhat do you do?\n"
        command = raw_input(" > ")
        if command == "D":
            print "this command is not yet implemented"
        elif command == "W":
            print "this command is not yet implemented"
        elif command == "N":
            print "this command is not yet implemented"
        elif command == "S":
            print "this command is not yet implemented"
        else:
            print "\tThat's not one of the commands.  They're in braces and capitals."
    elif current_room == 9:
        print "\tWhat do you do?\n"
        command = raw_input(" > ")
        if command == "C":
            print "this command is not yet implemented"
        elif command == "N":
            print "this command is not yet implemented"
        else:
            print "\tThat's not one of the commands.  They're in braces and capitals."
    elif current_room == 10:
        print "\tWhat do you do?\n"
        command = raw_input(" > ")
        if command == "N":
            print "this command is not yet implemented"
        elif command == "W":
            print "this command is not yet implemented"
        elif command == "E":
            print "this command is not yet implemented"
        elif command == "P":
            print "this command is not yet implemented"
        elif command == "A":
            print "this command is not yet implemented"
        elif command == "B":
            print "this command is not yet implemented"
        else:
            print "\tThat's not one of the commands.  They're in braces and capitals."
    elif current_room == 11:
        print "\tWhat do you do?\n"
        command = raw_input(" > ")
        if command == "D":
            print "this command is not yet implemented"
        elif command == "W":
            print "this command is not yet implemented"
        else:
            print "\tThat's not one of the commands.  They're in braces and capitals."
     
