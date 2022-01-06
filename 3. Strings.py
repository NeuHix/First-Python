#               -> Strings <-
a = '''  "Chocolate's Sweetness and Candy's Cream"   '''
print(a)
print(type(a))

#               -> String Slicing <-

Greeting = " Good Morning !"
Name = " Vector "
c = Greeting + Name  # Concatenation
print(c)

print(Name[1])

# Name[1] = "e" --> Doesn't work

print(Name[1:3])

print(Name[1:4])
print(Name[:4])  # is same as name[0:4]
print(Name[1:])  # is same as name[1:5]
c = Name[-4:-1]  # is same is name[1:4]
print(c)

name = "HarryIsGood"
# d = name[0::3]
d = name[:0:-1]
print(d)

#               -> String Functions ->

story = "once upon there was Bharat"

print(len(story))
print(story.endswith("Bharat"))
print(story.count("e"))
print(story.count("upon"))
print(story.capitalize())
print(story.find("there"))
print(story.replace("Bharat", "Finland"))

#             -> Escape Sequence <-

duck = "Everything\' \nis \t Fuc \\ ked"
print(duck)

'''                P      R       A      C       T       I       C       E                 S     E       T    '''

# Question 01

a = input("Welcome ! We are deligted to know your name : ")
print("Good Morning ! ", a)


# Question 02

v = input('''\t \tHey B*tch ! \n 
\t \t There's A F*cking News .... 
\t \t Waiting For You !!! 
\t \t Can't You Enter your Name !? :  ''')

d = input(" \t \t Date (day) : ")
cv = input(" \t \t Date (Month) : ")
vc = input(" \t \t Date (year) : ")
print(" \n \n \t \t Dear", v, ".",
      '''\n \t \t You are Fired !!! ''',
      "\n \t \t  \t \t  ", d, "th", cv, vc,

      '''\n \t \t Thanks For Your F*cking Support ! ''')

# Question 03

print("I'll tell you where the word you want is in the Sentence! Isn't it amazing? Now!")

a = input("What's that Sentence ? : ")
b = input("What's The Word ? : ")
d = a.find(b)
print(b, "is at index", d)
f = a.count(b)
print(b, "is repeated", f, "times !")
