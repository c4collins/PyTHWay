# Learn Python the Hard Way - Exercise 45

## Animal is-a object
class Animal(object):
    pass

## Dog is-a Animal
class Dog(Animal):

    def __init__(self, name):
        ## Dog has-a name
        self.name = name

## Cat is-a Animal
class Cat(Animal):

    def __init__(self, name):
        ## Cat has-a name
        self.name = name

## Person is-a Animal
class Person(Animal):

    def __init__(self, name):
        ## Person has-a name
        self.name = name

        ## Person has-a pet, of some kind
        self.pet = None

## Employee is-a Person
class Employee(Person):

    def __init__(self,name,salary):
        ## Magically, the Employee has-a name
        super(Employee, self).__init__(name)
        ## Employee has-a salary
        self.salary = salary

## Fish is-a Animal
class Fish(Animal):
    pass

## Salmon is-a Fish
class Salmon(Fish):
    pass

## Halibut is-a Fish
class Halibut(Fish):
    pass

## rover is-a Dog
rover = Dog("Rover")

## satan is-a Cat
satan = Cat("Satan")

## mary is-a Person
mary = Person("Mary")

## mary has-a pet Cat who has-a name
mary.pet = satan

## frank is-a Employee
frank = Employee("Frank",120000)

## frank has-a pet Dog who has-a name
frank.pet = rover

## flipper is-a Fish
flipper = Fish()

## crouse is-a Salmon
crouse = Salmon()

## harry is-a Halibut
harry = Halibut()

print frank.salary
print harry
print mary.pet.name
