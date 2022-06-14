#removing elements can be done by two ways:
#1).remove()
# set={"apple",1,10.5,"true"}
# set.remove("apple")
# print(set)    #{1, 10.5, 'true'}
# set.remove("carrot")
# print(set)   #KeyError: 'carrot'

#2).discard()
#set={"apple",1,10.5,"true"}
# set.discard("apple")
# print(set)     #{1, 10.5, 'true'}
# set.discard("carrot")
# print(set)       #{'apple', 1, 10.5, 'true'}  #It throws no error unlike .remove()



