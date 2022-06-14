# **kwargs allows to pass variable number of keyword arguments like :
#           func_name(key='value',temp='cool')

def kwarg(ht,age,name):
    print(name,age,ht)        #govind 25 5.6
details={'ht':'5.6','age':'25','name':'govind'}
kwarg(**details)


#getting arguments
def user(**values):
    for i,j in values.items():
        print(i,":",j)
user(hit=5.6,ages=25,nam='gov')
#####OUTPUT#######
# hit : 5.6
# ages : 25
# nam : gov