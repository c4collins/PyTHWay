from sys import argv

script, top = argv
print top

def list_of_numbers(x):
    i = 0
    numbers = []
    while i < int(x):
        print "At the top i is %d" % i
        numbers.append(i)
        
        i += 3.1415926
        print "Numbers now: ", numbers
        print "At the bottom i is %d." % i

    print "The numbers: "

    for num in numbers:
        print num
        
print list_of_numbers(top)
