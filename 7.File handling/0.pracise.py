#file opening, reading,writing,and appending text to the file and closing
#file location: D:\Dairy
#file name: py test.txt

################_______________WRITING_________________################
# file1=open('D:\Dairy\py test.txt','w')
# file1.write("Qwerty keyboard is feasible and easy to handle in writing text on the monitor\n")
# file1.close()
#Qwerty keyboard is feasible and easy to handle in writing text on the monitor
#NOTE: When you opens file for writing and if that file has any data, it gets delete before it opens.
#file1=open('D:\Dairy\py test.txt','w')
# file1.write("Qwerty keyboard is feasible and easy to handle in writing text on the monitor...\n")
# file1.close()

################_______________READING_________________################
# file1=open('D:\Dairy\py test.txt','r')
# print(file1.read())
# file1.close()
#Qwerty keyboard is feasible and easy to handle in writing text on the monitor...

################_______________READING_________________################
# file1=open('D:\Dairy\py test.txt','r')
# print(file1.read(11)) #Q for (1)   #Qwerty keyb for (11)
# file1.close()

################_______________READING_________________################
# file1=open('D:\Dairy\py test.txt','r')
# print(file1.readline()) #Qwerty keyboard is feasible and easy to handle in writing text on the monitor...
# file1.close()

################_______________READING_________________################
# file1=open('D:\Dairy\py test.txt','r')
# ree=print(file1.readlines()) #['Qwerty keyboard is feasible and easy to handle in writing text on the monitor...\n']
# print(type(ree)) #<class 'list'>
# file1.close()

################_______________APPENDING_________________################
# file1=open('D:\Dairy\py test.txt','a')
# file1.write("This line is from appending function.")
# file1.close()
'''Qwerty keyboard is feasible and easy to handle in writing text on the monitor...
This line is from appending function.This line is from appending function.'''


################_______________Looping(READING)_________________################
file1=open('D:\Dairy\py test.txt','r')             #only in reading mode only looping can be made
for i in file1:
    print(i)
file1.close()

#Qwerty keyboard is feasible and easy to handle in writing text on the monitor...

#This line is from appending function.









