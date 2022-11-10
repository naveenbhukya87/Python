n = int(input())

for i in range(1,n+1):
    pattern = ""
    revpattern = ""
    for j in range(1,i+1):
        pattern = pattern + str(j)
        if j < i :
            revpattern = str(j) + revpattern
    print(pattern + revpattern)