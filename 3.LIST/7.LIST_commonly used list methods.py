# Commonly used list methods in python are:
#append(),extend(),insert(),pop(),remove(),reverse(),sort() are to be separately performed and printed
#count(),index() can be directed from print()

#1. append(): adds an element to the list
list = [2, 1, 3, 5, 74, 5, 78, 3, 7, 8, 8, 6, 8, 9, 9, 9, 9, 9, 90]
list.append(91)  # [2, 1, 3, 5, 74, 5, 78, 3, 7, 8, 8, 6, 8, 9, 9, 9, 9, 9, 90, 91]
print(list)
# WRONG SYNTAX: print(list.append(20)) #OUTPUT:NONE

#2. count(): counts how many times a number repeated in a given list
print(list.count(9))  # 5
print(list.count(45))  # 0

#3. index(): gives the index of a given number
print(list.index(9))  # 13 i.e 9 having least index number is returned
"""print(list.index(45)) #ValueError: 45 is not in list """

#4. insert(index number,number): inserts a number in said index value and rest other values are not affected.
list.insert(1, 12)
print(list)  # [2, 12, 1, 3, 5, 74, 5, 78, 3, 7, 8, 8, 6, 8, 9, 9, 9, 9, 9, 90, 91]

#5. extend(): extends 1 list with another list
list1 = [0, 0, 0]
list.extend(list1)  # SYNTAX meaning: list is extended with list 1
print(list)  # [2, 12, 1, 3, 5, 74, 5, 78, 3, 7, 8, 8, 6, 8, 9, 9, 9, 9, 9, 90, 91, 0, 0, 0]
list1.extend(list)  # SYNTAX meaning: list1 is extended with list.
print(list1)  # [0, 0, 0, 2, 12, 1, 3, 5, 74, 5, 78, 3, 7, 8, 8, 6, 8, 9, 9, 9, 9, 9, 90, 91, 0, 0, 0]
# WRONG SYNTAX:
"""list=list.extend(list1)
   print(list)"""

#6. pop(): removes a number from input index number and returns that value.
lista=[1,2,3,4,5]
print(list.pop(1)) #2
print(lista) #[1,3,4,5]

#7. remove(): removes mentioned number from the list
lista=[1,2,3,4,5]
lista.remove(1)
print(lista) #[2, 3, 4, 5]
"""print(lista.remove(2)) ERROR: None"""

#8. reverse(): reverse the order of elements from 'left to right' to 'right to left'
listc=[1,2,3,4,5]
listc.reverse()
print(listc) #[5, 4, 3, 2, 1]
#Reversing can also be done by using slicing operatior:
#SYNTAX: print(listc[-length:empty])
print(listc[-5:]) #[5, 4, 3, 2, 1]
print(listc[-len(listc):]) #[5, 4, 3, 2, 1]

#9. sort(): sort the elements in a list in ascending order
listd=[1,99,33,5,1,555,33,88,33,24]
listd.sort()
print(listd) #[1, 1, 5, 24, 33, 33, 33, 88, 99, 555]