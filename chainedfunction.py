# method chaining = calling mutiple methods sequentially
#                   each call performs an action on the same object and returns self

class Car:

    def turn_on(self):
        print("You Ture on the engine")
        return self

    def drive(self):
        print("You drive the car")
        return self
    def brake(self):
        print("You step on the breaks")
        return self

    def turn_off(self):
        print("You turn off the engine")
        return self

car = Car()

#car.turn_on().drive()

#car.drive()

car.turn_on().drive().brake().turn_off()   #its diffcult to read in lot of method chaining so we use different method
#\is a line continue character
car.turn_on().\
    drive().\
    brake().\
    turn_off()  #\is a line continue character
