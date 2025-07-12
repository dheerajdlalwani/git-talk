a = 5
b = 5

def some_new_function:
    return "some value"


def add(a, b):
    return a + b

def sub(a, b):
    return a-b

def mul(a, b):
    return a*b

def div(a, b):
    if b != 0:
        return a/b
    else:
        return None



def series_addition(some_list):
    total = 0
    for i in some_list:
        total += i
    return total

print(add(a,b))
print(sub(a,b))
print(mul(a,b))

