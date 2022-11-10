num = int(input('Enter num: '))

for i in range(1,num+1):
    for j in range(1,2*num+1):
        if(j>=i and j+i<=2*num):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print("")



# coaching code:
n = int(input())
temp = 0
for i in range(n,0,-1):
    spaces = " " * temp
    pattern = "* " * i
    pattern = spaces + pattern
    temp = temp +1 
    print(pattern)