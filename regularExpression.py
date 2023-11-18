import re

pattern = r"Eggs"

if re.match(pattern, "Eggs Smacks"): #String must start with Eggs
    print("We got eggs baby")
else:
    print("No eggs today")

if re.search(pattern, "Smacks Eggs"): 
    print("We got eggs baby")
else:
    print("No eggs today")

if re.findall(pattern, "Eggs Smacks Eggs"): 
    print("We got eggs baby")
    print(re.findall(pattern, "Eggs Smacks Eggs"))
else:
    print("No eggs today")

string = "My name is John, hi I am John."
pattern = r"John"
newString = re.sub(pattern, "Rob", string)
print(newString)

#MetaCharacter
pattern = r"^Eg.s$" #The dot can be any character, ^ Starts with, $ Ends with.
if re.search(pattern, "Eggs Smacks"): 
    print("We got eggs baby")
elif re.search(pattern, "Eggs"): 
    print("We got some eggs baby")
else:
    print("No eggs today")

#Character class
#pattern = r"[A-Z][A-Z][0-9]"
pattern = r"[.][c][o][m]$"
if re.search(pattern, "AD1"):
    print("Match found")
elif re.search(pattern, ".com"):
    print("Email found")
else:
    print("No match found")

#Star meta character
pattern = r"Eggs(Smacks)*" #Anything before * can repeat zero to infinit times.
if re.match(pattern, "Eggs"): #Here Smacks is repeating 0 times
    print("We got eggs")
elif re.match(pattern, "EggsSmacks"): #This is also true
    print("We got eggs smacks")
else:
    print("No match found")

#Groups are written in between round brackets (group) and * metacharacter is used
#which allows the group of words/characters to repeat 0 to infinit times.