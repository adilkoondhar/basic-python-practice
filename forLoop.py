list = ["Chicken sandwich", "Ice cream sandwich", "Pizza"]
#Using end = " " in print statement to show output on same row, however it's not part of forLoop syntax.
for x in list:
    print (x, end = " ")
print ()
r = (range(0, 10))
for x in r:
    print (x, end = " ")
print ()
rep = int(input('Enter number of reps in loop: '))
for x in range(rep):
    print (x + 1, end = " ")
print ()