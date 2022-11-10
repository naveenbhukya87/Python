n = int(input())

for i in range(1,2*n+1):
    for j in range(1,i+1):
        if i < n+1:
            print("* ",end="")
        elif i+j <= 2*n:
            print("* ",end="")
    print()


# for i in range(1,2*n+1):
#     if i < n+1:
#         for j in range(1,i+1):
#             print("* ",end="")
#         print()
#     else:
#         for j in range(1,i+1):
#             if i+j <= 2*n:
#                 print("* ",end="")
#         print()