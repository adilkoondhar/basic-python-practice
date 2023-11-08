d = {"A": "It's A" + "\nFirst alphabet", "B": 2}
print (d["A"])
print (d.get("B"))
print (d.get("C"))
print (d.get("C", "There's no C"))
d2 = {
    input("Enter name: "): "Cast: " + input("Enter cast: ") + "\nAge: " + input("Enter Age: ")
}
print (d2.get(input("Enter name to print data: "), "There's no such name"))