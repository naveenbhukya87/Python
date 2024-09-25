# For loop
n = int(input("enter n: "))
i = 1
j = 1

for i in range(n+1):
    for j in range(i):
        j += 1
        print(str(i)+"*"+str(j)+"=", i*j)
    print("\n")
    i += 1

# while loop
num = int(input("enter num: "))
i = 1
while i <= num:
    j = 1
    while j <= i:
        print(str(i) + "*" + str(j) + "=", i * j)
        j += 1
    print("\n")
    i += 1
