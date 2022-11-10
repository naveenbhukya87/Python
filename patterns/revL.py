num = int(input('Enter num: '))

for i in range(1,num+1):
    for j in range(1,num+1):
        if(j>=i):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print("")