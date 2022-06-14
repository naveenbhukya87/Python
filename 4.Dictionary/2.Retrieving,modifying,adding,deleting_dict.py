ram={"243":143, 555: 343}
#print(key) #O/P{'govind': '21---5', 'dob': '2-5-8-9'}

#retrieving of elements
print(ram[555]) #343
print(ram["243"]) #143
#NOTE: .get() also used to retrieve the value

#adding of elements
ram['good']="better-best"
print(ram)  #{'243': 143, 555: 343, 'good': 'better-best'}

#modifying
ram["good"]="better"
print(ram) #{'243': 143, 555: 343, 'good': 'better'}

#deleting
del ram["good"]
print(ram) #{'243': 143, 555: 343}
