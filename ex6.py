# sets x to be the setyp line of the joke, using a format character to insert the 10
x = "There are %d types of people." % 10
# assigns string values to variables
binary = "binary"
do_not = "don't"
# Uses another format character to insert key words into a string
y = "Those who know %s and those who %s." % (binary, do_not)
# output the above two lines constructed
print x
print y
# repeat for emphasis
print "I said: %r." % x
print "I also said: '%s'." % y
# conclude that the joke is unfunny
hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"
# and say so
print joke_evaluation % hilarious
# express the ability to use mathematical operations on strings
w = "This is the left side of..."
e = "a string with a right side."
print w + e
