#We want to get a list with square numbers.
list = [x**2 for x in range(10)]
print (list)
#List with even square numbers only.
list2 = [x**2 for x in range(10) if x**2 % 2 == 0]
print (list2)