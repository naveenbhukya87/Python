# clearing set
# set={"apple",1,10.5,"true"}
# set.clear()
# print(set)
# OUTPUT: set() i.e set is cleared but set with empty set still exists


# deleting set
set = {"apple", 1, 10.5, "true"}
del set
print(set)  # <class 'set'>

for i in set:
    print(i)  # TypeError: 'type' object is not iterable
