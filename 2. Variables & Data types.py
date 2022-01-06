"""              -> Variables <-          """

'''Variables'''  # -> '''Data Types'''

a = "candy"  # String Variable
b = 42  # Integer Variable
c = 42.8  # Float Variable
d = True  # Boolean Variable
e = None  # None Variable

print(type(a))  # Checking type of Variable
print(type(b))  # Checking type of Variable
print(type(c))  # Checking type of Variable
print(type(d))  # Checking type of Variable
print(type(e))  # Checking type of Variable

'''             -> Operators <-           '''

# Arithmetic Operators

print("The value of 3+4 is ", 3 + 4)
print("The value of 3-4 is ", 3 - 4)
print("The value of 3*4 is ", 3 * 4)
print("The value of 3/4 is ", 3 / 4)

# Assignment Operators

a = 34
a -= 12
a *= 12
a /= 12
print(a)

# Comparison Operators

b = (14 <= 7)
b = (14 >= 7)
b = (14 < 7)
b = (14 > 7)
b = (14 == 7)
b = (14 != 7)
print(b)

# Logical Operators

bool1 = True
bool2 = False
print("The value of bool1 and bool2 is", (bool1 and bool2))
print("The value of bool1 or bool2 is", (bool1 or bool2))
print("The value of not bool2 is", (not bool2))

'''               -> Typecasting <-                '''

a = "35"
a = int(a)
print(type(a))
print(a + 5)

'''               -> Input Function <-             '''

a = input("Who the F you are !? -  ")
a = int(a)  # Convert a to an Integer(if possible)
print(type(a))

# '''                P      R       A      C       T       I       C       E                 S     E       T '''


# Question 01

print("Wanna Add Numbers ? I'm here to help you !")
a = input("What's the First one ? - ")
a = int(a)
b = input("The Second One ? - ")
b = int(b)
print(a + b)

# Question 02

a = 458
b = 15
print("The remainder when a is divided by b is", a % b)

# Question 03

a = input("Enter first number: ")
b = input("Enter second number: ")
a = int(a)
b = int(b)
avg = (a + b) / 2
print("The average of a and b is", avg)

# Question 04

a = input("Put the Number That you wanna be squared -  ")
a = int(a)
print("Your Mehnat ka FAL is", a * a)
