#Looping is used for reading elements in dictionary by
key={'243': 143, 555: 343, 'good': 'better-best'}
for i in key:
    print(i, ':', key[i])
    # 243: 143
    # 555: 343
    # good: better - best
    print(i,':',key[i],end=" ") #243 : 143 555 : 343 good : better-best
print(len(key))  #Length of Dictionary: 3