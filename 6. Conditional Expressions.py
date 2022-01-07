a = 0
if a > 4:                                       # IF_ELSE Ladder
    print("A is greater than 4")                # IF_ELSE Ladder
elif a < 3:                                     # IF_ELSE Ladder
    print("A is less than 3")                   # IF_ELSE Ladder
elif a >= 4:                                    # IF_ELSE Ladder
    print("A is greater than or equal to 4")    # IF_ELSE Ladder
elif a <= 4:                                    # IF_ELSE Ladder
    print("A is less than or equal to 4")       # IF_ELSE Ladder
elif a == 4:                                    # IF_ELSE Ladder
    print("A is equal to 4")                    # IF_ELSE Ladder
else:                                           # IF_ELSE Ladder
    print("Sorry!")                             # IF_ELSE Ladder

b = 4
if b == 4:  # Another if-else statement
    print("B is equal to 4")

if b > 4:  # Another if-else statement
    print("B is greater than 4")

if b >= 4:  # Another if-else statement
    print("B is greater than or equal to 4")

if b <= 4:  # Another if-else statement
    print("B is less than or equal to 4")
else:
    print("Sorry!")

# Quick Quiz
d = int(input("What's you age Man?: "))
if d >= 18 and d <= 15:                        # And
    print("Yes!")
else:
    print("No!")

d = int(input("What's you age Man?: "))
if d >= 18 or d <= 15:                         # Or
    print("Yes!")
else:
    print("No!")

d = int(input("What's you age Man?: "))
if not(d >= 18):                               # Not
    print("It Works!")

d = True
if d is True:                                  # is
    print("D is True")
else:
    print("D is not true")

d = [1, 2, 5, 6]
if 1 in d:                                     # in
    print("1 in D")
else:
    print("1 not in D")


g = 4
if g == 4:                                       # Else is Optional.
    print("G equals 4")                          # Else is Optional.
elif g >= 4:                                     # Else is Optional.
    print("G is greater than or equal to 4")     # Else is Optional.

# There can be infinite elif statements.
# Last 'Else' is executed only if all the statements inside elifs fail.

'''             P      R       A      C       T       I       C       E                 S     E       T    '''
#
# Question 1
c1 = int(input("Enter Number 1: "))
c2 = int(input("Enter Number 2: "))
c3 = int(input("Enter Number 3: "))
c4 = int(input("Enter Number 4: "))
if c1 >= c2:
    python = c1
elif c1 <= c2:
    python = c2
if c3 >= c4:
    python1 = c3
elif c3 <= c4:
    python1 = c4
if python >= python1:
    print(python, "is greatest.")
elif python1 >= python:
    print(python1, "is greatest.")

# Question 2
student1 = int(input("Enter marks in subject 1: "))
student2 = int(input("Enter marks in subject 2: "))
student3 = int(input("Enter marks in subject 3: "))

totalmarks = student1 + student2 + student3
reqper = (totalmarks/300*100)

if totalmarks > 300:
    print("Your overall marks could not be greater than 300.")

elif student1 > 100 or student2 > 100 or student3 > 100:
    print("Marks in any subject couldn't be greater than 100.")

elif reqper >= 40.0 and student1 >= 33.0 and student2 >= 33.0 and student3 >= 33.0:
    print(" \n \t Pass")
else:
    print("Fail")

# Question 3
s = input("Tell me a commment. - ")
if "make a lot of money" in s or "buy now" in s or "subscribe this" in s or "click this" in s:
    print("Your comment is a spam!")
else:
    print("Go ahead!")

# Question 4
username = input("Enter the username.\n(At least 10 characters): ")
length = len(username)
if length <= 10:
    print("Accepted!")
elif length > 10:
    print("Recheck!")

# Question 5
EntName = input("Enter your Name if it is present in the list: ", )
capital = EntName.capitalize()
List = ["Deck", "Rick", "Nick", "Jack"]
if capital in List:
    print("You are accepted!")
else:
    print("Your name is not present in the list.")

# Question 6
marks = int(input("Enter your Marks: "))
if marks > 100:
    print("Marks couldn't be greater than 100.")
elif 100 >= marks >= 90:
    print("Excellent!")
elif 90 >= marks >= 80:
    print("You deserve A!")
elif 80 >= marks >= 70:
    print("You deserve B!")
elif 70 >= marks >= 60:
    print("You deserve C!")
elif 60 >= marks >= 50:
    print("You deserve D!")
elif 50 > marks:
    print("You deserve F!")

# Question 7
post = input("What's in your mind?: ")
cappost = post.title()
if "Harry" in cappost:
    print("You are talking about Harry? Na!?")
else:
    print("What the heck are you talking about?")
