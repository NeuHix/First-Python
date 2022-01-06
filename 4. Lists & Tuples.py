"""         ->  Lists <-      """

# List are created using []


a = [2, 3, 4, 4, 5]

# Print List and Access any index using []
print(a[3])
# List supports item assignment
a[2] = 45
print(a)

# List can contain all types of Variables
d = [45, "Dad", False, 9.7]

# List slicing
Friends = ["Harry", "Potter", "Alpha", "Gamma", "Radiation", "45"]
print(Friends[0:4])
print(Friends[-4:7])

#  List Methods

L1 = [4, 5, 7, 2, 3]
L1.sort()  # Sorts the List
L1.reverse()  # Reverse the List
L1.append(34)  # Add Something to End of The List
L1.insert(2, 34)  # Insert 34 at index 2
L1.pop(3)  # Deleted the Element at Index 3
L1.remove(2)  # Removes 2 from the List

'''             ->  Tuples <-          '''

# Creating a tuple using ()
t = (1, 2, 4, 5)

# t1 = () # Empty tuple
# t1 = (1) # Wrong way to declare a Tuple with Single element
t1 = (1,)  # Tuple with Single element
print(t1)

# Printing the elements of a tuple
# print(t[0])

# Cannot update the values of a tuple
# t[0] = 34 # throws an error

# Tuple Methods
T2 = (1, 8, 5, 6)
print(T2)

print(T2.count(1))
print(T2.index(8))

'''             P      R       A      C       T       I       C       E                 S     E       T    '''

# Question 01

Fruit1 = input("Hey There ! What are fruits Do you Like 1 ? : ")
Fruit2 = input("Hey There ! What are fruits Do you Like 2 ? : ")
Fruit3 = input("Hey There ! What are fruits Do you Like 3 ? : ")
Fruit4 = input("Hey There ! What are fruits Do you Like 4 ? : ")
Fruit5 = input("Hey There ! What are fruits Do you Like 5 ? : ")
Fruit6 = input("Hey There ! What are fruits Do you Like 6 ? : ")
Fruit7 = input("Hey There ! What are fruits Do you Like 7 ? : ")
Empty_List = [Fruit1, Fruit2, Fruit3, Fruit4, Fruit5, Fruit6, Fruit7]
print("Here is your List of Fruits : ", Empty_List)

# Question 02
markFIRST = int(input("Enter Marks achieved by the FIRST student : "))
markSECOND = int(input("Enter Marks achieved by the SECOND student : "))
markTHIRD = int(input("Enter Marks achieved by the THIRD student : "))
markFOURTH = int(input("Enter Marks achieved by the FOURTH student : "))
markFIFTH = int(input("Enter Marks achieved by the FIFTH student : "))
markSIXTH = int(input("Enter Marks achieved by the SIXTH student : "))

list1 = [markFIRST, markSECOND, markTHIRD, markFOURTH, markFIFTH, markSIXTH]
list1.sort()
print("These are the marks achieved by the 6 students :", list1)
print("Total Marks : ", (sum(list1)))
