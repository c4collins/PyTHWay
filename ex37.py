from ex37data import *

def start():
    """Asks for and receives direction about which list to print at any given time"""
    print "What definintions list do you wish to see?"

    definitions = {}
    
    for listname in definition_list:
        definitions[listname[:1]] = listname
        definitions[listname[:1]+"_list"] = listname.lower().replace(" ","_") + "_list"

    for item in definitions:
        if len(item) < 2:
            print "\tTo print the %s list, press:\t  %s" % (definitions[item],item)

    which_list = raw_input('\tThen press <ENTER>\t').upper()
    print_list(which_list,definitions)    

def print_list(which_list,definitions):
    """print the whichever list is chosen"""
    try:
        for item in eval(definitions[which_list+"_list"]):
            print "%s:\n\t\t\t%s\n\n\t%s\n" % (definitions[which_list],item[0],item[1])
            if len(item[2])>1:                            # Some definitions have examples
                print "\tUsage Example:"
                for ex_line in item[2]:
                    print "\t\t\t" + ex_line
            print "\n"+"-"*79
    except KeyError:
        print "Sorry, that is not one of the lists."

# Program Starts Here
start()
