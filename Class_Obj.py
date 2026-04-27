"""
class Student:

    def say_hello(self):   #function that written inside the class called method
        print("Hi, I'm a student : Thiru")

s1 = Student()
s1.say_hello() #s1.say_hello(s1)
"""
"""
class Student:
    def __init__(self,fname,age):
        self.name = fname
        self.age = age

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

s1 = Student("Thiru",22)
s1.display()
"""
"""
class Employee:

    def __init__(self,name,aadhaar): #constractor (__init__) which use same data to all method
        self.x = name
        self.y = aadhaar

    def enter_office(self):
        print(f"{self.x} enters using Aadhaar {self.y}")

    def open_bank_account(self):
        print(f"Bank account opened for {self.x} with Aadhaar {self.y}")

employee = Employee("Thiru","1234-5678-9010")
employee.enter_office()
employee.open_bank_account()
"""
class Math:
    def sqr(self,a):
        return a * a

    def cube(self,n):
        return n*n*n

total = Math()
print(total.sqr(4))
print(total.cube(22))
