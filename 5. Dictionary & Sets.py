# '''                              DICTIONARY                                      '''
# '''                              DICTIONARY                                      '''
# '''                              DICTIONARY                                      '''

# '''        Dictionary Syntax       '''

myDict = {
    "Fast": "In a quick manner",
    "Harry": "A coder",
    "Marks": [1, 2, 3],
    "SecondDict": {'value': 'Fruit'},  # You can have a Dictionary inside a Dictionary.
    1: 3
}

print(myDict['Fast'])
print(myDict['Marks'])
print(myDict['Harry'])
print(myDict['SecondDict']['value'])  # Here's how to print

myDict['Harry'] = ['harry']  # We can manipulate the dictionary.
v = {}  # An Empty Dictionary
print(type(v))  # Returns Dictionary
# '''          Dictionary Methods          '''

print(myDict.keys())  # Used to print the keys inside the dictionary
print(type(myDict.keys()))  # Returns <class 'dict_keys'>
print(myDict.values())  # Prints the values the of the keys in the dictionary.
print(myDict.items())  # Prints the (key:value) pairs of the list.
updateDict = {
    "Red": "Tomato",
    "Blue": "Sky",
    "Harry": "A Singer"
}
myDict.update(updateDict)  # updates myDict by adding key:value pairs from updateDict
print(myDict)
print(myDict.get("harry2"))  # Prints the value of harry2 if present in the dictionary
''' print(myDict["harry2"]) '''  # Prints the value of harry2 from the dictionary

# Difference between .get and [] syntax
print(myDict.get("harry2"))  # Returns NONE as harry2 is not in the dictionary
'''print(myDict["harry2"])'''  # throws error as harry2 is not in the dictionary

# '''                             SETS                                      '''
# '''                             SETS                                      '''
# '''                             SETS                                      '''

z = {1, 2, 4, 5, 4}  # Set is a Collection of Non-repetitive values. Hence, 4 will be printed only one time.
print(z)
t = set()  # Empty Set
print(type(t))

# '''          Set Methods          '''

t.add(4)  # Adding values in the Set
t.add(6)
t.add(6)
t.add(4)
print(t)  # Set strictly prohibits repetitive words

'''t.add([2, 3, 7])'''  # We can't add LIST in the Set.
t.add((1, 2, 7))  # We can add TUPLE in the Set.
'''t.add({1: 3})'''  # We can't add a Dictionary in the Set.
print(t)

# Sets are unordered # Element's order doesn't matter.
# Sets are unIndexed # Cannot access elements by Index
# There is no way to change items in Sets.
# Sets cannot contain duplicate values.
print("newSet")
newSet = {1, 4, 6, 7, 3}
print(newSet)
print(len(newSet))  # Prints Number of values inside the Set.

newSet.remove(4)  # Removes 4 from Set. and Updates the set
# t.remove(32)  # Throws an error cause' 32 isn't present in the Set.
print(newSet)
print(newSet.pop())  # Removes an arbitrary element from the set and returns the element removed.
print(newSet.intersection({6, 4, 7}))  # Returns a new set which contains only items in both sets.
print(newSet.union({5, 7}))  # Returns a new set with all items from both sets
newSet.clear()  # Empties the set.
print(newSet)

'''             P      R       A      C       T       I       C       E                 S     E       T    '''

# Question 1

ShipraDict = {
    "Aanand": "Fun",
    "Ganit": "Mathematics",
    "Prithvi": "Earth",
    "Surya": "Sun",
    "Aam": "Mango",
}

print("This is Shipra's Dictionary. \n Get Hindi to english Translation of Words")

print("Your Options are: \t ", ShipraDict.keys())
d = input("Enter the Word in Hindi and get the translation in English: \t")
print("The english word for", d, "is", ShipraDict.get(d))

# Question 2

q = int(input("Enter at least 8 Numbers of any combination you want: "))
w = int(input("Enter at least 8 Numbers of any combination you want: "))
e = int(input("Enter at least 8 Numbers of any combination you want: "))
r = int(input("Enter at least 8 Numbers of any combination you want: "))
t = int(input("Enter at least 8 Numbers of any combination you want: "))
y = int(input("Enter at least 8 Numbers of any combination you want: "))
u = int(input("Enter at least 8 Numbers of any combination you want: "))
i = int(input("Enter at least 8 Numbers of any combination you want: "))
program = {q, w, e, r, t, y, u, i}
print("Your Numbers are: \t", program)

# Question 3

g = {1, "1"}  # Int and Str are not same in Python
print(g)

# Question 4

proto = set()
proto.add(20)
proto.add("20")
proto.add(20.0)
print(len(proto))  # Kyo chauk gaye na? - Agar Do Integer aur Float same hai to Set v unhe Equal consider karega

# Question 4

sa = {}
print(type(sa))  # - Its Dictionary

# Question 5

EmpDict = {}
Harry = input("Harry's favourite language: ")
Rick = input("Rick's Fav language: ")
Deck = input("Deck's Fav language: ")
upadatesdict = {
    "Harry's": Harry,
    "Rick's": Rick,
    "Deck's": Deck,
}
EmpDict.update(upadatesdict)
print(EmpDict)
