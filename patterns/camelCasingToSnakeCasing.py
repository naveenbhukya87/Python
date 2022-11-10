word = input()
wordList = []
count = -1
for letter in word:
    count = count + 1
    if letter.isupper():
        wordList.append(count)

length = len(wordList)
finalWord = ""
for i in range(0,length):
    if i < length-1:
        finalWord = finalWord + word[wordList[i]:wordList[i+1]].lower() +"_"
    elif i == length-1:
        finalWord = finalWord + word[wordList[i]:].lower() + "_"
print(finalWord.strip("_"))