n = int(input())

for i in range(1, 2*n):
    if i == 1 or i == n or i == (2*n - 1):
        print("* " * n)
    elif i>1 and i < n:
        for j in range(1,n+1):
            if j == 1 or j == n:
                print("* ",end="")
            else:
                print("  ",end="")
        print()
    elif i>n and i < 2*n:
        for j in range(1,n+1):
            if j == n:
                print("* ",end="")
            else:
                print("  ",end="")
        print()