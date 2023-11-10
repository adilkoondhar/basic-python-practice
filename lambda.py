x = lambda a: a + 10
print (x(10))

print ((lambda b: b + 5)(5))

def func(x):
    return lambda c: c * x

doubler = func(2)

print (doubler(20))
print (func(3)(10))