name = "Connor Collins"
age = 25
height = 74 # inches
weight = 230 # lbs
eyes = "Blue"
teeth = "White"
hair = "Blond"

height_cm = height * 2.54
weight_kg = weight * 0.454

print "Let's talk about %s." % name
print "He's %d centimetres tall." % height_cm
print "He's %d kilograms heavy." % weight_kg
print "Actually, that's not too heavy."
print "He's got %s hair, and %s eyes." % (hair, eyes)
print "His teeth are usually %s, depending on the coffee." % teeth

print "If I add %d, %d, and %d, I get %d." % (height, weight, age, height+weight+age)