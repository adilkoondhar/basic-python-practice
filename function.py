def func():
    print ("func() was called")
func()
def add(num1, num2):
    return num1 + num2
print (add(1, 2))
def sq(num1):
    return num1*num1
print (sq(add(1, 2)))

def addTen (x, y):
    return x + 10 + y
def twice (fun, x, y):
    return fun(fun(x, y), fun(x, y))
print (twice (addTen, 0, 1))