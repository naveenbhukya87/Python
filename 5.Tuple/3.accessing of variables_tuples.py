# accessing of tuples
tup2 = 1, 2, 3, 5, 4, 3, 33, 333, 55754, 1, 2, 3, 4, "num", 10.5, True
print(tup2[15])  # True
# print(tup2[16]) #tuple index out of range
print(tup2[-5:-2])  # (3, 4, 'num')
# (1, 2, 3, 5, 4, 3, 33, 333, 55754, 1, 2, 3, 4, 'num', 10.5, True)
print(tup2[0:])
