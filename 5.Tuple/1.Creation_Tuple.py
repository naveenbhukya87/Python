# Tuples are very similar to list but are immutable. Tuple uses ()

# creation of tuple:
tup1 = (1, 2, 3, 4, "num", 10.5, True)  # (1, 2, 3, 4, 'num', 10.5, True)
print(tup1)
tup2 = ()  # () i.e. empty set
print(tup2)
tup3 = ([1, 2, 3])
print("tup3: ",tup3) #tup3:  [1, 2, 3]
print("tup3Type: ",type(tup3)) #tup3Type:  <class 'list'>
tup4 = tuple("abc")  # ('a', 'b', 'c') 
print(tup4)
tup5 = 1, 2, 3, "abc"  # (1, 2, 3, 'abc')
print(tup5)
tup6 = tuple("abc",1,2)
try:
    print("tup6: ", tup6) # TypeError: tuple expected at most 1 argument, got 3
except TypeError:
    print("tuple expected at most 1 argument, got 3")
