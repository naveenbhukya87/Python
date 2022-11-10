a = [10,9,8,7,6,5]
n = len(a)
# val = int(input("Enter the number to search: "))
for i in range(1,n):
    temp = a[i]
    for j in range(i,-1):
        if j>0 and temp < a[j-1]:
            a[j] = a[j-1]
    a[i-1] = temp

print(a)
