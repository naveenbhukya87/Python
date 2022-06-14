#Adding elements can be done by 2 ways,viz:
#1).add(): to add 'ONE' element at a time
# set={"apple",1,10.5,"true"}
# set.add("doctor")
# print(set)
#{1, 'apple', 10.5, 'doctor', 'true'}   doctor was added

#2).update([]): to add 'MORE THAN ONE' element at a time
#NOTE: It also helps in joining of 2 or more sets
set={"apple",1,10.5,"true"}
# set.update(["nurse","pine_apple",1,2,3])
# print(set)
#{1, 2, 3, 'apple', 'pine_apple', 10.5, 'nurse', 'true'}
# set.update("nurse","pine_apple")  #{'apple', 1, 'e', 's', 10.5, 'u', 'true', 'p', 'a', 'r', '_', 'n', 'l', 'i'}
# print(set)
# print(len(set)) #14
'''set.update("nurse","pine_apple",1,3)  #TypeError: 'int' object is not iterable'''

