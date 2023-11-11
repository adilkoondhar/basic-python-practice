def add(x):
    return x + 2
myList = [10, 20, 30]
result = list(map(add,myList))
print (result)

print (list(map(lambda x: x * 2, myList)))