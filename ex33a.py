def build_numbers_list(top_num, bottom_num=0,step=1):
    """
    Builds a list out of a given range of numbers (which is silly because you can assign it) and prints it out and returns the value.
    Takes an argument of the top of the list, an optional argument of the bottom of the list, and an optional argument of the step the is used when generating the list.
    """
    i = bottom_num
    numbers = []
    while i < top_num+1:
        print "\nAt the top, i is %d." % i
        numbers.append(i)
        
        i += step
        print "Numbers now: ", numbers
        print "At the bottom, i is %d" % i
    
    print "The numbers: "

    for num in numbers:
        print num,
    return numbers
        
build_numbers_list(6)
build_numbers_list(34,32)
build_numbers_list(4522,4500,6)