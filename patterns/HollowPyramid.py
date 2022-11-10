n = int(input())
k = n-1
count = 1
for i in range(1, 3):
    spaces = " " * k
    stars = "* " * i
    print(spaces + stars)
    k = k - 1
for i in range(3, n):
    spaces = " " * k
    innerSpace = "  " * count
    count = count + 1
    stars = "* "+innerSpace+"* "
    print(spaces + stars)
    
    k = k - 1
print("* " * n)