name = 'Connor P. Collins'
age = 25 # not a lie
height = 74 # inches
cm_height = height * 2.54
weight = 230 # pounds
kg_weight = weight * .454
eyes = 'Blue'
teeth = 'White'
hair = 'Blond'

print "Let's talk about %s." % name
print "He's %d cm tall." % cm_height
print "He's %d kg heavy." % kg_weight
print "Actually, that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are unusually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d, I get %d." % ( age, height, weight, age + height + weight)

# Other string format characters:
# d   - decimal integer
# i   - decimal integer
# o   - octal integer
# u   - OBSOLETE - is the same as d
# x/X - hexadecimal value
# e/E - floating point exponential value
# f/F - floating point decimal value
# g/G - floating point general - decimal unless exponent is <-4
# c   - single character
# r   - String (converts any Python object using repr())
# s   - String (converts any Python object using str())
# %   - print the % character
