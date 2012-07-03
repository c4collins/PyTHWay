from sys import argv # import argument variables from sys module

script, filename = argv # unpack argv into variables

txt = open(filename) # use file's open method and assign the opened file to txt

print "Here's your file for %r:" % filename
print txt.read() # use file's read command (which reads the file's entire contents)

print "Type the filename again:"
file_again = raw_input("> ") # collect another file name

txt_again = open(file_again) # open that new file

print txt_again.read() # use file's read to print the file's contents