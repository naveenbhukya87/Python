num = int(input('Enter num: '))

for i in range(1,num+1):
    for j in range(1,num+1):
        if(i+j>=num+1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print("")