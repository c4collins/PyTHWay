from sys import argv # import argv

script, input_file = argv # unpack argv

def print_all(f):
    print f.read() # print entire file

def rewind(f):
    f.seek(0) # revert to file beginning

def print_a_line(line_count, f):
    print line_count, f.readline() # print a number and then the next line in the file

current_file = open(input_file) # open input file, for reading

print "First, lets print the whole file:\n"

print_all(current_file) # call print_all

print "Now, let's rewind, kind of like a tape:"

rewind(current_file) # call rewind

print "Let's print three lines."

current_line = 1
print_a_line(current_line, current_file) # print single lines

current_line += 1 # x += 1 is the same as x = x + 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)