def print_definition_list(list):
    for item in list:
        if len(item) <= 2:
            print "Keyword:\t %s\t\t%s" % (item)
        else:
            print "Keyword:\t %s\t\t%s" % (item[0],item[1])
            print "Usage Example:"
            for ex_line in item[2]:
                print "\t\t\t\t\t\t" + ex_line
        print "-"*79


definition_list = [
    ('and',         "Boolean operator for AND"),
    ('del',         "Deletes an item from memory",          ("del foo[4]",)),
    ('from',        "Keyword used in import statements",    ("from sys import argv",)),
    ('not',         "Boolean operator for NOT"),
    ('while',       "Indicates the beginning of a while-loop"),
    ('as',          "Designate new names for imported modules",         ("from sys import argv as argument_variables",)),
    ('elif',        "Else-if instruction, for branching more than one option in an if statement."),
    ('global',      "Allows you to set a variable to be global from inside a function (or anywhere that the variable would not normally be global)",         ("(i.e. global me = \"locally defined\" )",)),
    ('or',          "Boolean operator for OR"),
    ('with',        "Creates an object from an unmanaged resource, and iterated against it.  It's a special kind of loop that opens and closes the file automagically",        ("with A() as a:","\tdo something",)),
    ('assert',      "Used to verify the state of the variables in the program, essentially if the assert statement is False it will throw an AssertionError",       ("max = 0","if a < b:","\tmax = b","if b > a:","\tmax = a","assert (max == a or max ==b) and max >= a and max >= b",)),
    ('else',        "Final statement in an if-statement, acting as a catch-all for anything didn't find a True condition in one of the if or elif branches."),
    ('if',          "Indicates an if statement.",       ("if a == b:", "\tdo something",)),
    ('pass',        "Does nothing. Is useful to put in code blocks where something is required syntactically, but no actions need to be performed.  Is also useful as a placeholder while writing code allowing for structure without requiring content."),
    ('yield',       "Is used to return a generator statement (that is, an iterable object which can only be used once and is not stored in memory, so the list can be exceptionally long.  There is a great explanation on StackOverflow of what it is and how to use it."),
    ('break',       "Is used to end a loop.",       ("while True:","\tbreak",)),
    ('except',      "Deals gracefully with error messages.  Instead of crashing the program immediately, \"except\" allows for catching the Exception, and returning an error message to the user.",        ("(i.e. while True:","\ttry:","\t\tx = int(raw_input(\"Please enter a number: \"))","\t\tbreak","\texcept ValueError:","\t\tprint \"Oops!  That was not a valid number.  Try again...\"",)),
    ('import',      "Used when importing other modules for use in a particular piece of code.",     ("from sys import argv as argument_variables",)) ,
    ('print',       "Boolean operator"),
]

print_definition_list(definition_list)
