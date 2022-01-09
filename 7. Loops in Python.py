# '''                              While loop                                      '''
# '''                              While loop                                      '''
# '''                              While loop                                      '''

i = 4  # variable 'i' has the literal 4
while i < 10:  # While Loop
    print("Yes")  # While loop checks the condition given and
    i = i + 1  # if it is true then the body statement is executed
print("Done!")  # And the Loop will keep executing until the Condition becomes False.
print('i became = 10.')  # After executing i = i + 1 , value of i eventually becomes i = 10
print('While Loop stops')  # and the condition becomes false and While loop stops.

# Quick Quiz
program = 0
while program < 50:
    program = program + 1
    print(program)

# Example
i = 0
while i < 5:
    print("Harry")
    i = i + 1  # If the condition never becomes False the loop keeps getting executed.
else:
    print("I can use 'else' with while loop")
# Quick Quiz
deck = ["Loop", "has", "begun"]
i = 0
while i < len(deck):
    print(deck[i])
    i = i + 1

# '''                              For loop                                      '''
# '''                              For loop                                      '''
# '''                              For loop                                      '''

group = ["Loop", "has", "begun"]
for item in group:  # Assigns the value at index 0 in 'group' to 'item' and iterates
    print(item)  # the sequence everytime by using next index till all the indexes are exhausted.

# Range
for i in range(8):  # Assigns the values from "0 to 7" to 'i' and iterates the sequence till assigning '7' to 'i'
    print(i)  # prints the value of 'i' after assigning '0' to 'i' from range(8) , iterates by assigning next
#                     values and prints the value.
for i in range(1, 8):  # Now start assigning from '1 to 7' to 'i' and then iterates and prints values of 'i'
    print(i)

for i in range(1, 8, 2):  # Now iteration occurs leaving every two values and then assigns the values to 'i' and prints.
    print(i)  # range(start, stop, step_size)

for i in range(10):
    print(i)
else:  # Executed after the for-loop is exhausted.
    print("This is inside 'else' of 'for', ", "For_Loop exhausted")

# Break
for i in range(10):
    print(i)
    if i == 5:  # now while iterating the loop,  when 'i' becomes equal to 5, the code inside 'if' is executed
        break  # stops the loop intentionally.
else:
    print("If loop is stopped intentionally,", "'else' statement will not be executed.")

# Continue
even = ()
for i in range(10):
    if not (i % 2 == 0):  # If 'i' becomes equal to 5, then 'continue' is executed
        continue  # skips the current condition in 'if' , only 5 will not be printed
    print(i, "code")

# Pass
i = 0
for i in range(8):
    pass  # Do Nothing
if i > 5:
    pass  # Do Nothing
while i > 0:
    pass  # Do nothing


def sum(a, b):
    pass  # Do Nothing


"""             P      R       A      C       T       I       C       E                 S     E       T    """

# Question 1
num1 = int(input("Enter the number: "))
for c in range(1, 11):
    #     print(num1, "x", c, "=", num1*c)
    print(f"{num1} x {c} = {num1 * c}")  # F-strings , {} used to put variable
# Question 2
l1 = ["Harry", "Sohan", "Sachin", "Rahul"]
name_input = input("Enter name: ")
cap_name_inp = name_input.capitalize()
if cap_name_inp in l1:
    for cap_name_inp in l1:
        if cap_name_inp.startswith("S"):
            print("Hey!", cap_name_inp)
else:
    print("Name Absent")
# Question 3
i = int(input('Give the number for the multiplication table: '))
b = 1
while b < 11:
    print(i, "X", b, "=", i * b)
    b = b + 1
# Question 4
prime_num = int(input("Enter your number: "))
prime = True
for i in range(2, prime_num):
    if prime_num % i == 0:
        prime = False
    break
if prime:
    print(prime_num, "is a prime.")
else:
    print(prime_num, "is not a prime")
# Question 5
n = int(input("Enter the Number: "))
i = 1
while i in range(1, n):
    i = n * (n + 1) / 2
    print(f"The sum of first {n} natural numbers is {i}")
# Question 6
n = int(input("Enter the Number: "))
s = 1
for i in range(1, n + 1):
    s = s * i
print(f"Factorial of {n} is {s}")
# Question 7
p = 3
for i in range(3):
    print(" " * (p - i - 1), end="")  # end=""  is used to not print new line after print statement.
    print("*" * (2 * i + 1), end="")
    print(" " * (p - i - 1))
# Question 8
for i in range(0, 3, 1):
    print("*" * (i + 1))
# Question 9
m = 3
for i in range(1):
    print("* * *")
    print("*   *")
    print("* * *")
# Question 10
table = int(input("Enter the Number:"))
for i in reversed(range(1, 11)):
    deck = f"{table} x {i} == {table * i}"
    print(deck)
