age = int(input("Enter Your Age : "))
citizen = input("Are You a Indian Citizen [Y/N]?: ").lower()

if citizen == "y":
    if age == 100:
        print("You are too old to vote")
    elif age >= 100:
        print("You are not death yet!")
    elif age <= 17:
        print("You can not vote")
    else:
        print("You can vote")
elif citizen == "n":
       print("you can not vote")
else:
    print("Get Lost!!!")
