# A generator function is a special type of function that uses the yield function
# to return values one by one, instead of returning everything at once.

def get_numbers(n):
    return [i for i in range(n)]

#print(get_numbers(10))

def get_number(n):
    for i in range(n):
        yield i # pauses here and good for smaller storage

for num in get_number(10):
    print(num)

