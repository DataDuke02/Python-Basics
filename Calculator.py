try:
    a = int(input("Enter a first Number : "))
    b = int(input("Enter a Second Number : "))

    print("Choose Caluculation to perform \n"
        "1.Add (+) \n"
        "2.Subtract (-) \n"
        "3.Multiply (*) \n"
        "4.Divide (/) \n"
        "5.Square Root (**) \n"
        "6.Reminder (%) \n"
        "7.Roundup (//)")

    cal =str(input().strip())

    if cal == "+":
        ans = a + b
    elif cal == "-":
        ans = a - b
    elif cal == "*":
        ans = a * b
    elif cal == "/":
        if b == 0:
            print("Error : Can not divide by zero! IDOIT!")
            ans = None
        else :
            ans = a / b
    elif cal == "**":
        ans = a ** b
    elif cal == "%":
        ans = a % b
    elif cal == "//":
        ans = a // b

    else:
        print("Invalid Error")
        ans = None

    if ans is not None:
        print(f"The answer is : {ans}")

except ValueError:
    print("INVALID INPUT! Please Enter Valid Number")
