
age = 18

if age >= 18:
    print("You can vote")

num = int(input("Enter a number : "))

if num % 2 == 0:
    print("Even")
else:
    print("Odd")

a = int(input())
b = int(input())
c = int(input())

largest = 0

if b > a:
    largest = b
elif c > b:
    largest = c
else:
    largest = a

print(largest)

year = int(input("Enter a year : "))

if (year  % 4 == 0) or (year % 100 != 0 and year % 400 == 0):
    print(f"Leap year : {year}")
else:
    print("Not a leap Year")


n = int(input("Enter a Number : "))

if n == 0:
    print("zero")
elif n < 1:
    print("negative")
else:
    print("positive")

marks = int(input("Enter a marks : "))

if marks >= 90:
    print("A")
elif marks >= 75 and marks <= 89:
    print("B")
elif marks >= 50 and marks <= 74:
    print("C")
elif marks < 50:
    print("Fail")
