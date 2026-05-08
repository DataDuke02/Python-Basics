import random

x = random.randint(1,6) #print any random one number from 1 to 6
y = random.random() #print any random float values

mylist = ['Rock','Scissors','Paper']
z = random.choice(mylist) #print randomly

cards = [1,2,3,4,5,6,7,8,9,"K","Q","A","J"]
random.shuffle(cards)  #shuffle the cards

print(x)
print(y)
print(z)
print(cards)
