import os

source = "Thiru2802"
destination = "C:\\Users\\THIRUGNANASAMBANTHAM\\Desktop\\Thiru2802" #by using this we can also move folders

try:
    if os.path.exists(destination): #check the file is there or not
        print("There is already a file there")
    else:
        os.replace(source,destination) #moved file source and destination to another file
        print(source+" was moved")
except FileNotFoundError: #print the input if file not founded
    print("Source is not founded")

