n = int(input())

count = n-1
for i in range(1,n+1):
    zeros = ""
    zeros = "0 " * count
    count = count - 1
    pattern = ""
    ones = "1 " * (2*i - 1)
    pattern = zeros + ones + zeros
    print(pattern)