class Student:

    def __init__(self, name, contact):
        
        self.name = name

        self.contact = contact

    def setData(self):

        self.name = input("Enter name: ")

        self.contact = input("Enter contact: ")

    def getData(self):
        print("Name is " + self.name + "\nContact is " + self.contact)


#john = Student("","")
#john.setData()
#john.getData()

#Inheritance
class ScienceStudent(Student):

    def science(self):
        print("I am a science student")

#rob = ScienceStudent("", "")
#rob.setData()
#rob.getData()
#rob.science()

#Encapsulation
class Encap:

    __hiddenVariable = 0

    def setGet(self, x):
        self.__hiddenVariable = x
        return self.__hiddenVariable

obj = Encap()
print(obj.setGet(10))