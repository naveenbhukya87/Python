########Bubble sorting in ascending order ######

a = [10,9,8,7,6,5]
n = len(a)
val = int(input("Enter the number to search: "))
for i in range(1,n):
    for j in range(n-i):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1],a[j]

######## Binary Search #########
low,high = 0,n-1
while low <= high :
    mid = int((low+high)/2)
    if val == a[mid]:
        print(val, " is found @ index", mid)
        break
    elif val < a[mid]:
        high = mid-1
    elif val > a[mid]:
        low = mid + 1
if low > high:
    print(val, "is not found")