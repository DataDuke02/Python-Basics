# exception = events detected during execution that interrupt the flow of program

try:
    numertor = int(input("Enter a number to divide: "))
    denominator = int(input("Enter a number to divide by: "))
    result = numertor / denominator
 #   print(result)
except ZeroDivisionError as e: #make sure not have 0 as input value
    print(e)
    print("You can't divide by zero! IDIOT!")
except ValueError as e: #make sure not have string as input value
    print(e)
    print("Enter only number Plz")
except Exception as e: #except the unknown error    # "as e" used for to mention a what type of error
   print(e)
   print("Something went wrong :(")
else:
    print(result)
finally:
    print("This will always execute")

