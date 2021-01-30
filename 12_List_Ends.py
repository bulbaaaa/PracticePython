import random
a = [random.randint(0,100) for i in range(5)]

def list_ends(a):
    return print([a[0], a[-1]])

list_ends(a)
