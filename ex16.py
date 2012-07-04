from sys import argv

script, filename = argv

print "Opening %r for reading..." % filename
target = open(filename, 'r') # opens the file with the read attribute

print "It currently says:"
print target.read()

print "Closing the file."
target.close() # close the file after reading

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit Enter."
raw_input("?")

print "Opening %r..." % filename
target = open(filename, 'w') # opens the file with the write attribute, which truncates the file

# print "Truncating the file.  Goodbye!"
# target.truncate() # truncate deletes the entire contents of the file.

print "Now I'm going to ask you for three lines."

line1 = raw_input("Line 1: ")
line2 = raw_input("Line 2: ")
line3 = raw_input("Line 3: ")

print "I'm going to write these to the file."

target.write("%s\n%s\n%s" % (line1, line2, line3)) # \n is the newline character

print "And finally we close it."
target.close()