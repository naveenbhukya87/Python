# .union():
# set1={"apple",1,10.5,"true"}
# set2={"a",1,2,3,4}
# set1=set1.union(set2)
# print(set1)              #{1, 2, 3, 4, 10.5, 'apple', 'true', 'a'}
# set2=set2.union(set1)
# print(set2)              #{1, 2, 3, 4, 10.5, 'apple', 'true', 'a'}


# .update():
set1 = {"apple", 1, 10.5, "true"}
set2 = {"a", 1, 2, 3, 4}
set1.update(set2)
print(set1)  # {1, 'true', 2, 3, 4, 10.5, 'apple', 'a'}
