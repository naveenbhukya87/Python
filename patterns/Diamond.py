n = int(input())

def oddPrintBlock():
    if i % 2 == 0 and j % 2 == 0:
        print("*", end="")
    elif i % 2 != 0 and j % 2 != 0:
        print("*", end="")
    else:
        print(" ", end="")

def evenPrintBlock():
    if i % 2 == 0 and j % 2 != 0:
        print("*", end="")
    elif i % 2 != 0 and j % 2 == 0:
        print("*", end="")
    else:
        print(" ", end="")


for i in range(1, n + 1):
    for j in range(1, 2 * n):
        if i + j >= (n + 1) and j - i <= (n - 1):
            if n % 2 != 0:
                oddPrintBlock()
            elif n % 2 == 0:
                evenPrintBlock()
        else:
            print(" ", end="")
    print()

for i in range(n + 1, 2 * n):
    for j in range(1, 2 * n):
        if i - j <= (n - 1) and j + i <= (3 * n - 1):
            if n % 2 != 0:
                oddPrintBlock()
            elif n % 2 == 0:
                evenPrintBlock()
        else:
            print(" ", end="")
    print()

# Coaching code:
n = int(input("Mad code: "))

k = n - 1
for i in range(1, n + 1):
    spaces = " " * k
    stars = "* " * i
    print(spaces + stars)
    k = k - 1

k = 1
for i in range(n - 1, 0, -1):
    spaces = " " * k
    stars = "* " * i
    print(spaces + stars)
    k = k + 1
