# Prevents a user from creating an object of that class
# * compets a user to override abstract  methods in child class

# abstract class = a class which contains one or more abstract methods.
# abstract method = a method that has a declaration but does have an implementation.

from abc import ABC,abstractmethod

class Vehicles(ABC): #prevent user from creating anything from this class

    @abstractmethod
    def go(self):  #only can be inherited to child if the use the same method of go and stop
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Vehicles):
    def go(self):  # only can be used if the parent cls has this object
        print("You drive the car") #and the child should have is own declaration

    def stop(self):
        print("This car is stopped")

class Motorcycle(Vehicles):
    def go(self):
        print("You drive the motorcycle")

    def stop(self):
        print("This motorcycle is stopped")

#vehicle = Vehicles() #cannot mention this cls because it abstract cls
car = Car()
motorcycle = Motorcycle()

#vehicle.go()
car.go()
car.stop()
motorcycle.go()
motorcycle.stop()
