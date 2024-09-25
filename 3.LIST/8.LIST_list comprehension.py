# To produce a list on specified condition using only 'for loop' or both 'for and if loops'

# 1. for loop approach
list1 = list(x for x in range(5))
print(list1)  # [0, 1, 2, 3, 4]
listif = list(x for x in range(5) if (x < 5))
print(listif)  # [0, 1, 2, 3, 4]
listf = list(x for x in range(5) if (x > 5))
print(listf)  # []

listeven = list(x for x in range(2, 11, 2))
print(listeven)  # [2, 4, 6, 8, 10]
listevif = list(x for x in range(11) if (x % 2 == 0))  # [2, 4, 6, 8, 10]

listodd = list(x for x in range(1, 10, 2))
print(listodd)  # [1, 3, 5, 7, 9]
listodif = list(x for x in range(11) if (x % 2 != 0))
print(listodif)  # [1, 3, 5, 7, 9]

# listodd
