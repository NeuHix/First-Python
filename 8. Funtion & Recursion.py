# '''                              Functions                                     '''
# '''                              Functions                                     '''
# '''                              Functions                                     '''


def percent(mark):  # Creating a function using 'def'==>'percent'-> function name AND 'mark'-> Parameter of the function
    return ((mark[0] + mark[1] + mark[2]) / 300) * 100  # Giving value to the function 'percent' .


#                                                         Used to refer the value in 'return' anywhere in the program
#                                                         by calling " percent(a_defined_parameter) " .
#                                                    a_defined_parameter replaces 'Parameter' in the return value.
#


''' def percent(mark):                                          
        p = ((mark[0] + mark[1] + mark[2]) / 300) * 100         
        return p                                        '''  # Another way

marks = [45, 56, 67]
average = percent(marks)  # 'percent' (Function) ke value ke andar jaha pe bhi 'mark' hoga waha pe 'marks' replace ho
#                                                                                                            jayega.
marks2 = [45, 56, 67]  # 'percent' (Function) ke value ke andar jaha pe bhi 'mark' hoga waha pe 'marks2' replace ho
#                                                                                                           jayega .
percentage = percent(marks2)  # 'percent'(Function) ke value ke andar jaha pe bhi 'mark' hoga waha pe 'marks2' replace
#                                                                                                        ho   jayega .
print(average, percentage)


# A Function can be reused by the programmer any number of times.

# Quick Quiz
def greet(day):
    return "Good Day!"


user = input("Enter your name: ")
print(greet(user), user)


# Function with Arguments


def length(num1, num2):
    return num2 - num1


height = length(5, 6)  # '5' replaces 'num1' and '6' replaces 'num2' then 'num2 - num1' executes
print(height)


# Default Parameter value
def greet(name="Stranger"):  # Defining the name = 'Stranger'
    print("Good Day, " + name)


greet("Harry")
greet()  # Returns 'Stranger' if Empty.

'''                              Recursions                                     '''
'''                              Recursions                                     '''
'''                              Recursions                                     '''

n = 0
product = 1
for i in range(n):
    product = product * (i + 1)
print(product)


def factorial_iter(n):
    product = 1
    for i in range(n):
        product = product * (i + 1)
    return product


d = factorial_iter(5)
print(d)


def factorial_iter(n):
    if n == 1:
        return 1
    return n * factorial_iter(n - 1)


g = factorial_iter(5)
print(g)

"""             P      R       A      C       T       I       C       E                 S     E       T    """


# Question 1


def maxima(num1, num2, num3):
    if num1 > num2:
        if num1 > num3:
            return num1
        else:
            return num3
    else:
        if num2 > num3:
            return num2
        else:
            return num3


a = maxima(2, 6, 5)
print(a)


# Question 2
def temp(temperature):
    p = temperature * 1.8 + 32
    return p


tempe = int(input("Enter Temperature: "))
t = temp(tempe)
print(f"{tempe}° Celsius equals {t} in Fahrenheit.")

# Question 3
'''     end=""     '''
# Question 4

# Question 5

for i in reversed(range(4)):
    p = ("*" * i)
    print(p)


# Question 6


def inch(cms):
    c = cms * 2.54
    return c


tempi = int(input("Enter height: "))
t = inch(tempi)
print(f"{tempi} inch equals {t} cm")


# Question 7
def remove_strip(word, strip):
    p = word.replace(strip, "")
    return p.strip()


this = "         Whatever Pycharm is         "
n = remove_strip(this, "Pycharm")
print(n)

# Question 8
inp = int(input("Enter the number: "))


def multi(num):
    for i in range(1, 11):
        cd = f"{num} x {i} == {num * i}"
        print(cd)
    return cd


inp2 = int(input("Enter the number: "))
j = multi(inp2)
print(j)
