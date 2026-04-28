from file import add

"""
def add(a,b):
    return  a+b

result = add(1,3)
print(result)
"""
result = add(9.267,5.43)
print((round(result/3.0)))

def add(*args):
    total = 0
    for num in args:
        total += num

    return total

print(add(1,2,3,4,5))


def profile(**kwargs):
    print("user profile")
    for key,value in kwargs.items():
        print(f"{key}:{value}")

profile(name="thiru",age=23)
