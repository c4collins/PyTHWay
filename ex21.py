def add(a,b):
    print "ADDING %d + %d" % (a,b)
    return a+b

def subtract(a,b):
    print "SUBTRACTING %d - %d" % (a,b)
    return a-b

def multiply(a,b):
    print "MULTIPLYING %d * %d" % (a,b)
    return a*b

def divide(a,b):
    print "DIVIDING %d / %d" % (a,b)
    return a/b

print "Let's do some math with just functions!"

age = add(20.0,5.0)
height = subtract(80.0,6.0)
weight = multiply(23.0,10.0)
iq = divide(1000.0,9.0)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age,height,weight,iq)

#A puzzle for the extra crdit, type it in anyway.
print "Here is a puzzle."
what = add(age,subtract(height, multiply(weight,divide(iq,2.0))))

print "That becomes: ", what, "Can you do it by hand?"
# The equation that would produce these results is (age+height)-(weight*(iq/2))
# Some of those brackets are unnecessary for bedmas but are useful for thinking.

print "Here's my adaptation of the puzzle:"
why = add(age,multiply(age,subtract(age,multiply(weight,divide(iq,height)))))
print "That becomes: ", why

print "What about the formula age*height/weight+iq?"
when = add(iq,divide(multiply(age,height),weight))
print "This is: ", when