cars = 100 # there are 100 cars
space_in_a_car = 4.0 # each car contains space for 4 passengers
drivers = 30 # there are 30 drivers
passengers = 90 # there are 90 passengers
cars_not_driven = cars - drivers # only as many cars can be driven as there are drivers
cars_driven = drivers # one driver for each car driven
carpool_capacity = cars_driven * space_in_a_car # passenger capacity for cars being driven
average_passengers_per_car = passengers / cars_driven # how crammed do the passengers need to be

print "There are", cars, "cars available."
print "There are only", drivers, "available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."