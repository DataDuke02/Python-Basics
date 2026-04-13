with open("notes.txt","w") as f:
    f.write("Hello mate!")

with open("notes.txt","r") as f:
    print(f.read())

#n = input("Enter a string or say something : ")

with open("notes.txt","a") as f:
    f.write("Hi! Man \n")

with open("notes.txt","r") as f:
    print(f.readline())
