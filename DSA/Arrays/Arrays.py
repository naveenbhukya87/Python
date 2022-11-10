arr = [12, 34, 14, 67, 45, 54, 68, 93, 8, 81, 39]
small = arr[0]
large = arr[0]
for a in arr:
    if a < small:
        small = a
    if a > large:
        large = a

print("Smallest of the array is: ", small)
print("largest of the array is: ", large)
