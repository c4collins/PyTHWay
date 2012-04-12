cars = 100
space_in_a_car = 4.0
# A floating point number here was used to allow the average based on this to not be an integer.
drivers = 30.0
# But really this number has to be a float too for that to work, so I changed it.
passengers = 90
cars_not_driven = cars - drivers # 100 - 30
cars_driven = drivers # 30
carpool_capacity = cars_driven * space_in_a_car # 30 * 4.0
average_passengers_per_car = passengers / cars_driven # 90 / 30

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."

