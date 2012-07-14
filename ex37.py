from ex37data import *

def start():
    """Asks for and receives direction about which list to print at any given time"""
    print "What do you want to do?"

    definitions = {}
    
    for listname in definition_list:
        definitions[listname[:1]] = listname
        definitions[listname[:1]+"_list"] = listname.lower().replace(" ","_") + "_list"

    for item in definitions:
        if len(item) < 2:
            print "\t\t\tTo print the %s list, press:\t  %s" % (definitions[item],item)

    which_list = raw_input('\t\tThen press <ENTER>\t')
    print_list(which_list,definitions)    

def print_list(which_list,definitions):
    """print the whichever list is chosen"""
    try:
        for item in eval(definitions[which_list+"_list"]):
            if len(item) <= 2:
                print "Keyword:\t%s\t\t%s" % (item)
            else:
                print "Keyword:\t%s\t\t%s" % (item[0],item[1])
                print "Usage Example:"
                for ex_line in item[2]:
                    print "\t\t\t\t\t\t" + ex_line
            print "-"*79
    except KeyError:
        print "Sorry, that is not one of the lists."

# Program Starts Here
start()
