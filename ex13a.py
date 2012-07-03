from sys import argv

script, height, width, length = argv

height, width, length = int(height), int(width), int(length)

av = raw_input("Do you want the surface area, or the volume? A/V ")
printed = False

if av=="A":
	print "The area is %i." % ((height*width+width*length+height*length)*2)
	printed = True
elif av=="V":
	print "The volume is %i." % (height*width*length)
	printed = True
else:
	print "Wrong answer, chump."
