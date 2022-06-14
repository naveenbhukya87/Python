#TRAVERSE means horizontal
list=[1,2,3,4,5]
for i in list:
    print(i)
    # 1
    # 2
    # 3
    # 4
    # 5
    print(list)
    # [1, 2, 3, 4, 5]
    # [1, 2, 3, 4, 5]
    # [1, 2, 3, 4, 5]
    # [1, 2, 3, 4, 5]
    # [1, 2, 3, 4, 5]
    print(i, end=" ") #1 2 3 4 5
    print(i, end="0 ") #10 20 30 40 50
    print(i, end="time print") #1time print2time print3time print4time print5time print
    print(list,end=" ") #[1, 2, 3, 4, 5] [1, 2, 3, 4, 5] [1, 2, 3, 4, 5] [1, 2, 3, 4, 5] [1, 2, 3, 4, 5]