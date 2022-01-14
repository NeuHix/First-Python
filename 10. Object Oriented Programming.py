# Object-Oriented Programming in Python
x = "Hello"
print(type(x))  # <class 'str'>
# this string that we typed in is actually an object of the class 'str'
x = 1
print(type(x))  # <class 'int'>


# x is equal to an object of the <class 'int'>  of  value 1
# these different data types are actually a part of a  class


def hello():
    print("hello")


print(type(hello))  # <class 'function'>

x = 2
#  2 is an object belonging to the class 'int ' and it is equal to x

# so pretty much everything we work with in python is actually an object with some kind of class


# what we're gonna do is make our own 'classes' so that we have our own specific types. Just understand that whenever
# you create something in python you are really creating an object which is an instance of a specific class,
#  that class defines the way in which that object can interact with other things in our program

# Experiment
''' a = 1
    b = "hello"

    print(a + b)  '''
# The error we gonna get -->
# TypeError: unsupported operand type(s) for +: 'int' and 'str'

# because our object 'a' is in 'int' and our object 'b' is in 'str' we cannot add them because the program does not
# know how to work with object of those two types or in better words the addition operation is not defined for
# objects of 'int' and object of 'str' at being added together
string = "Hello"
print(string.upper())
# We're allowed to use this what we call 'method' whenever you have this dot operator This is a method that is
# acting on a specific object. A method 'upper' that is acting on the object of type 'str' that is stored in this
# string variable and the reason we're allowed to use this method on it is because this is a string
# Now I can't do
'''    r = 1
    print(r.upper()  '''


# The error ->
# AttributeError: 'int' object has no attribute 'upper'
# The things we can do with these objects is based on the type of class that they are


# Creating a Class  -->


class Dog:  # We've created a 'class'
    def __init__(self, name):
        self.name = name  # An Attribute of class Dog which is name.

    def meow(self):
        return "meow"  # I can even return something

    def add(self, x):  # I can have these methods take arguments
        return x + 1  # take the argument and return 'argument' + 1

    def bark(self):  # We are gonna define the operations that a dog is able to do
        print("bark")  # In this case I've created a method now a method is essentially just a funtion that goes
        # goes inside of a class

    def get_name(self):
        return self.name


d = Dog("Jin")  # Assigning the variable D to an instance of the class Dog
print(type(d))  # <class '__main__.Dog'>
# The reason we have these underscores is that this telling us what module this class was defined in,
# now by default the module that you run is called the 'main' module this is again an object of the class dog and
# that means that whatever we define inside class is going to be what is allowed or the operations that can be
# performed by a Dog and one of those operations are Bark.
d.bark()  # Using the method that we defined earlier in the class Dog.
print(type(d))
print(d.add(8))  # Gave the argument '8' and it returned 8 + 1
# When I call this method I need to pass a specific value so that can operate.
# This is how the methods work.
d2 = Dog("Bill")
print(d2.name)


# init => Special method
# Get called as soon as instantiating the class

class Sachin:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_age(self):
        return self.age

    def get_name(self):
        return self.name

    def set_age(self, age):  # Writing a function that can manipulate the age
        self.age = age


S = Sachin("Rick", "46")
print(S.get_name())
S2 = Sachin("Nick", "35")
print(S2.get_age())
S.set_age(23)
print(S.get_age())

'''             P      R       A      C       T       I       C       E                 S     E       T    '''


# Question 01


class Programmer:
    firm = "Microsoft"

    def __init__(self):
        self.list = []

    def add_pro(self, name, position):
        self.list.append(name)
        self.list.append(":")
        self.list.append(position)


pro = Programmer()
pro.add_pro("Nick", "Post man")
print(pro.list)


# Question 02


class Calculator:

    def __init__(self, number):
        self.number = number

    def cube(self):
        cube = self.number * self.number * self.number
        return cube

    def square(self):
        square = self.number * self.number
        return square

    def root(self):
        root = self.number ** 0.5
        return root


number = Calculator(6)
print(number.cube())
print(number.square())
print(number.root())


# Question 04

class Calculator:

    def __init__(self, number):
        self.number = number

    def cube(self):
        cube = self.number * self.number * self.number
        return cube

    def square(self):
        square = self.number * self.number
        return square

    def root(self):
        root = self.number ** 0.5
        return root

    @staticmethod
    def greet():
        print(f"Hello! Here's a static method preview.")


number = Calculator(6)
print(number.cube())
print(number.square())
print(number.root())


# Question 05
class Train:
    def __init__(self, name, status, fare):
        self.status = status
        self.fare = fare
        self.name = name

    def getstatus(self):
        print(f"About the Train :-")
        print(f"\n \t The Train is {self.name}")
        print(f"\t (Currently)Available no. of seats in {self.name} is {self.status}")

    def getfare(self):
        print(f"\t {self.name} costs a {self.fare} bucks.")

    def bookmyticket(self):

        if self.status > 0:
            print(f"Your seat is reserved. Your seat no. is {self.status}")
            self.status = self.status - 1
        else:
            print("Train Occupied. Try Again later.")

    def cancelmyticket(self):

        if self.status < 4:
            print(f"Your Ticket is cancelled.")
            self.status = self.status + 1
        else:
            print(f"Ticket is not yet reserved.")


train = Train("Bihar Express", 4, 100)

print("\n \t Welcome! to Indian Railways Bihar Express.")
user_name = input("\n Enter Your Name Sir: ")
print(f'''\n \t Our Services for you {user_name}: 
(a) Get Status 
(b) Cost of Travel
(c) Book my Ticket
(d) Cancel my Ticket''')

ser = input(f"Select your service {user_name}: ")
service = ser.lower()

if service == "a" or service == "get status":
    train.getstatus()
elif service == "b" or service == "cost of travel":
    train.getfare()
elif service == "c" or service == "book my ticket":
    train.bookmyticket()
elif service == "d" or service == "cancel my ticket":
    train.cancelmyticket()
else:
    print("Please Select an Appropriate Service. ")

print("Thanks for using our Service!")



