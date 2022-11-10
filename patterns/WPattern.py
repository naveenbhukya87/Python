n = int(input())
count = 1
innerCount = 0
for i in range(n,0,-1):
    pattern = ""
    if i == n:
        print("* " * (2*n - 1))
    else:
        outerSpaces = " " * count
        count = count + 1
        innerSpace = "  " * innerCount
        innerCount = innerCount + 1
        stars = "* " * i
        pattern = outerSpaces + stars + innerSpace + stars + outerSpaces
        print(pattern)