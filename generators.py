def func():
    count = 0
    while count < 5:
        yield count
        count += 1
for x in func():
    print (x)

def evenNum(x):
    for e in range(x):
        if e % 2 == 0:
            yield e
myList = list(evenNum(9))
print (myList)