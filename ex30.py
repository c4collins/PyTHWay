people = 50
cars = 40
buses = 45

if cars > people:
    print "We should take the cars."
elif cars < people:
    print "We should not take the cars."
else:
    print "we can't decide"

if buses > cars:
    print "That's too many buses."
elif buses < cars:
    print "Maybe we could take the buses."
else:
    print "We still can't decide."

if people > buses and people > cars:
    print "Alright, let's just take the buses."
else:
    print "Fine, lets stay home then."