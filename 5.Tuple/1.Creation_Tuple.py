#Tuples are very similar to list but are immutable. Tuple uses ()

#creation of tuple:
tup1=(1,2,3,4,"num",10.5,True) #(1, 2, 3, 4, 'num', 10.5, True)
print(tup1)
tup2=() #() i.e. empty set
print(tup2)
tup3=([1,2,3])
print(tup3)
tup4=tuple("abc") #('a', 'b', 'c') #tuple("abc",1,2) is not valid
print(tup4)
tup5=1,2,3,"abc" #(1, 2, 3, 'abc')
print(tup5)