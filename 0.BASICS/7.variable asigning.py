#how data can be assigned to variables
#example_1
x=10
y=20
s='welcome'
a='A'
print(x,y,s,a) #o/p: 10 20 welcome A

#above prog can be rewritten in another way
x,y,s,a=10,20,'welcome','A'
#here x,y will be assigned with values 10,20 respectively
print(x,y,s,a)  #o/p 10 20 welcome A

#values can be interchanged or swapped simply like
x,y=20,30
print(x,y) #output 20 30
x,y=y,x
'''at first x,y will be assigned with values 10,20 respectively and with next step x will be assigned with 
y (which is 2) and y with x (which is 1)'''
print(x,y) #output 30 20 i.e values are interchanged

#assigning same value to many variables
x=y=z=150
print(x,y,z) #output is 150 150 150
