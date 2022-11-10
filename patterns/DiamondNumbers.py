n = int(input())
topGapsCount = n-1
bottomGapsCount = 1


for i in range(1,n+1):
    numberPattern = ""
    topSpaces = " " * topGapsCount
    topGapsCount = topGapsCount - 1
    for j in range(1,i+1):
        numberPattern = numberPattern + str(j)+" "
        fullPattern = topSpaces + numberPattern
    print(fullPattern)

for i in range(n-1,0,-1):
    numberPattern = ""
    botSpaces = " " * bottomGapsCount
    bottomGapsCount = bottomGapsCount + 1
    for j in range(1,i+1):
        numberPattern = numberPattern + str(j)+" "
        fullPattern = botSpaces + numberPattern
    print(fullPattern)
        