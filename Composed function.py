# Composed function is when the put of one functions becomes the input of another - like
# f(g(x))

def add(x):
    return x + 2 # 10 + 2 = 12

def multi(x):
    return x * 5 # 2 * 5 = 10

def composed(x):
    return add(multi(x))  # f(g(x)) -> add of (x + 2)

print(composed(2))
