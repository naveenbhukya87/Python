n = int(input())
temp = n-1
pattern = ""
for i in range(1,n+1):
    spaces = " "*temp
    pattern = pattern+str(i)+" "
    finalPattern = spaces + pattern
    temp = temp - 1
    print(finalPattern)