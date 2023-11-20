from tkinter import *

root = Tk()

label1 = Label(root, text="Hey there")

label1.pack()

myFrame = Frame(root)
myFrame.pack()

myFrame1 = Frame(root)
myFrame1.pack(side=BOTTOM)

myButton = Button(myFrame, text="Click me", fg="RED")
myButton.pack()

myButton1 = Button(myFrame1, text="Click me", fg="BLUE")
myButton1.pack()

root.mainloop()