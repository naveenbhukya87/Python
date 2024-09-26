i = 1
for i in range(0, 5):
    i += 1
    j = 1
    for j in range(0, 9):
        j += 1
        if i+j >= 6 and j-i <= 4:
            print("*", end=" ")
        else:
            print(" ", end=" ")
