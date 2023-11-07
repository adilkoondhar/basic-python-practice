num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
try:
    print (num1//num2)
except ZeroDivisionError:
    print("Number can't be divided by zero")
finally:
    print ("Finally block")