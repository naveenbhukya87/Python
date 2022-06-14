#Checking the list using "in" and "not in" operator
from operator import index

list1=[1,2,3,4,5,6,7,8,9,0]
print(2 in list1) #True i.e., if 2 is there in list then it returns "True"
print(2 not in list1) #False i.e., if 2 is not there in list is false then it returns "False"
print(12 in list1) #False i.e., if 12 is not there in list then it returns "False"
print(12 not in list1) #False i.e., 12 is not there in list is true so returned True"

#Length of list: len()
print(len(list1)) #10 i.e 10 elements are there
list2=["good","goood","good","goood"]
print(len(list2)) #4
list3=list("govind")
print(len(list3)) #6
print(len("govind")) #6

#maximum of list: max()
print(max(list1)) #9
print(max(list2)) #goood
print(list2.index(max(list2))) #1
print(max(list3)) #v
print(list3.index(max(list3))) #2

#Minimum of list: min()
print(min(list1)) #0
print(min(list2)) #good
print(list2.index(min(list2))) #0
print(min(list3)) #d
print(list3.index(min(list3))) #5

#Sum of elements in a list: sum()
print(sum(list1)) #45=1+2+3+4+5+6+7+8+9+0
'''print(sum(list2))''' #Since these are strings, OUTPUT: error
'''print(sum(list3))''' #Since these are strings, OUTPUT: error

#Slicing: using [start:end] where start and end are index numbers
print(list1[0:5]) #[1, 2, 3, 4, 5]
print(list1[0:]) #[1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(list1[0:-1]) #[1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list1[:9]) #[1, 2, 3, 4, 5, 6, 7, 8, 9]