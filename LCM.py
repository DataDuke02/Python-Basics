a = int(input("Enter First Number :"))
b = int(input("Enter Second Number :"))

x,y = a,b
while y !=0:
    x,y = y, x%y

gcd = x
lcm = (a*b) //gcd

print("LCM :",lcm)
