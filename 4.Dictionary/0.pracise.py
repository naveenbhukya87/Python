# creating dictionary
# ram={"243":143, 555: 343}
# print(type(ram))
# # print(ram)
#
# #retrieving
# key={"govi":'4',"gov":'3',"go":2," ":0,555:"hello"}
# print(key["govi"]) #4
# print(key[" "]) #0
# print(key[555]) #hello
#
# #adding
# key["g"]=1
# print(key) #{'govi': '4', 'gov': '3', 'go': 2, ' ': 0, 555: 'hello', 'g': 1}
#
# #modifying
# key["g"]=2
# print(key) #{'govi': '4', 'gov': '3', 'go': 2, ' ': 0, 555: 'hello', 'g': 2}
#
# #deleting
# del key["g"]
# print(key) #{'govi': '4', 'gov': '3', 'go': 2, ' ': 0, 555: 'hello'}
#
key = {"govi": '4', "gov": '3', "go": 2, " ": 0, 555: "hello",
       "govin": '4', "govj": '3', "goj": 2, "15 ": 0}

print(key.clear())
print(key)
