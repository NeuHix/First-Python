
a = open("text.txt", "r")  # Opening a file by using 'open("filename.ext","read_only_mode")'
data = a.read()  # Reading 'a'
b = open("text.txt")  # Takes "r" by default if nothing is specified
default = b.read(5)  # We can also specify how many characters to read
print(data)
print(default)

# binary = open("C:\\Users\\pc\\Downloads\\what-economits-do.jpg", "rb")
# view = binary.read()
# print(view)

read_line = b.readline()  # Read the Second Line of text.txt file
print(read_line)

read_line = b.readline()  # Read the  Third Line of text.txt file
print(read_line)

read_line = b.readline()  # Read the Fourth Line of text.txt file
print(read_line)

a.close()  # Closing the file
b.close()  # Closing the file

# Modes
modes = {
    "r": "open for reading",
    "w": "open for writing",
    "a": "open for appending",
    "+": "open for updating",
}

# Writing Files
file = open("another.txt", "w")  # If the File is absent then it will be created.
file.write("Write this in the file")  # " Stuff " will be written in the created file.
file = open("another.txt", "a")  # Appending the File
file.write("Write this in the file")
file.close()

# With Statement
with open("text.txt", "r") as f:   # No need to write f.close()
    q = f.read()
print(q)
with open("text.txt", "w") as f:   # No need to write f.close()
    q = f.write("whatever")
print(q)  # Number of Characters

'''             P      R       A      C       T       I       C       E                 S     E       T    '''

# Question 1
program = open("poems.txt", "r")
read_program = program.read()

if "Twinkle" in read_program:
    print("Twinkle is Present in poems.txt")
else:
    print("Twinkle is Absent in poems.txt")
program.close()


# Question 2
def game():
    return 457


start = str(game())
hiscore = open("hiscore.txt", "r")
read_me = hiscore.read()
write_score = open("hiscore.txt", "w")
writ_scor = open("hiscore.txt", "w")
if read_me > start:
    writ_scor.write(read_me)
elif read_me < start:
    score = write_score.write(start)
hiscore.close()
write_score.close()

# Question 3

for table in range(2, 21):
    with open(f"Multiplication_Table {table}.txt", "w") as m_table:
        for i in range(1, 11):
            m_table.write(f"{table} x {i} == {table * i}\n")

# Question 4
with open("sample.txt") as f:
    content = f.read()

content = content.replace("donkey", "$%^@$^#")

with open("sample.txt", "w") as f:
    f.write(content)

# Question 5
words = ["donkey", "kaddu", "mote"]

with open("sample.txt") as f:
    content = f.read()

for word in words:
    content = content.replace(word, "$%^@$^#")
    with open("sample.txt", "w") as f:
        f.write(content)

# Question 6
with open("log.txt") as f:
    content = f.read()

if 'python' in content.lower():
    print("Yes it is")

# Question 7
content = True
i = 1
with open("log.txt") as f:

    while content:

        content = f.readline()

        if 'python' in content.lower():
            print(content)
            print(f"Yes Python is present on line number {i}")
            print(i)
        i += 1

# Question 8
with open("this.txt") as f:
    content = f.read()

with open("copy.txt", "w") as f:
    f.write(content)

# Question 9
first = open("first.txt", "r")
first.read()
Second = open("second.txt", "r")
Second.read()

if first.read() == Second.read():
    print("Identical")
else:
    print("Isotope")

# Question 10
wipe = open("Clear.txt", "w")
writ = wipe.write(" ")
wipe.close()

# Question 11
import os

original = open("Old File.txt")
delete = "Old File.txt"
red = original.read()
Duplicate = open("New File.txt", "w")
dup = Duplicate.write(red)

# os.remove("Old File.txt")
