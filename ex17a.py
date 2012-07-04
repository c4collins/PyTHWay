from sys import argv
script, from_file, to_file = argv 

print "Copying from %s to %s." % (from_file, to_file)

open(to_file,'w').write(open(from_file).read()) # open to_file for writing, write what is read from the from_file after opening it.

open(to_file).close()
open(from_file).close() # close both files