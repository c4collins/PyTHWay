# This version was converted to use floating point numbers, but there's only one place that it's wrong, so I only changed that line.

print "I will now count my chickens:" # prints

print "Hens", 25 + 30 / 6	# calculates 25+(30/6)
print "Roosters", 100 - 25 * 3 % 4 # calculates 100-(25*3)R4  
# The % symbol stands for modulo which is a fancy way of saying divide by this number and return the remainder.  I use the term R when writing this from old CS class structure.
# In this case, the operation performed is 75R4, so 75/4 is 18 with a remainder of 3, so a 3 gets returned.

print "Now I will count the eggs:" # prints

print 3.0 + 2.0 + 1.0 - 5.0 + 4.0 % 2.0 - 1.0 / 4.0 + 6.0
# I'll do this in steps with brackets around what's calculated in the next step:
#  3+2+1 -5 +(4R2)-(1/4)+6
# (3+2+1)-5 +  0  - .25 +6 - 4R2 is 2 with a remainder of 0
#   (6   -5)+  0 (- .25 +6)
#     (1    +  0        +5.75)
#	6.75

   
print "is it true that 3 + 2 < 5 - 7?" # Forms hypothesis

print 3 + 2 < 5 - 7 # checks if 5 is less than -2, determines experiment

print "What is 3 + 2?", 3 + 2	# checks what 3 + 2 is, performs experiment
print "What is 5 - 7?", 5 - 7	# checks what 5 - 7 is, collects data

print "Oh, that's why it's False."	# draws conclusion

print "How about some more."	# Performs more experiments

print "Is it greater?", 5 > -2	# checks if 5 is greater than -2
print "Is it greater or equal?", 5 >= -2 # checks if 5 is greater than or equal to -2
print "Is it less or equal?", 5 <= -2 # checks if 5 is less than or equal to -2,  Verifies accuracy of results

