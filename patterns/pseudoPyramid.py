num = int(input('Enter num: '))

for i in range(1,num+1):
    k=1
    for j in range(1,2*num+1):
        if(j+i>=num+1 and j-i<=num-1 and k):
            print("*",end=" ")
            k=0
        else:
            print(" ",end=" ")
            k=1
    print("")