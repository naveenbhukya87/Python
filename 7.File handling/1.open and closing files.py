#File handling is used to read and write data to and from a file.
#opening files: #SYNTAX: f=open(fileaddress\name,mode)
#Closing a file: file.close()
#TYPES OF MODES:
   #'r': open a file for READ only
   #'w': open a file for WRITING, if a file has data before its opening, the data will be deleted before
#           opening.otherwise new file will be created.
   #'a': open a file in APPEND mode i.e to write a data to the end of a file.
'''file1=open('D:\Dairy\py test.txt','w')
file1.write("line is printed")
file1.close()'''


#Reading data from the file:
#1) Reading all data at once:
#SYNTAX:  file=open(fileaddress\name,r)
          #print(file.read(number))
          #number: () , all text in the file will be printed in the concole window
          #number: (something), that many characters will be printed
# file=open('D:\Dairy\The Hindu Vocab.txt','r')
# print(file.read())
#pedagogy : principles and methods of instruction
#Prudent : Careful and sensible
#Onus : Responsibility.......................
# print(file.read(12)) #pedagogy : p
# print(file.read(33)) #pedagogy : principles and methods
# file.close()


#2)readline(): return next line of a file
# file=open('D:\Dairy\The Hindu Vocab.txt','r')
# print(file.readline()) #pedagogy : principles and methods of instruction (1st line of the file)
# print(file.readline())
#pedagogy : principles and methods of instruction
#Prudent : Careful and sensible #returns next line
#file.close()


#3)readlines(): read all lines as a LIST OF STRINGS in the file
# file=open('D:\Dairy\The Hindu Vocab.txt','r')
# print(file.readlines()) #pedagogy : principles and methods of instruction (1st line of the file)
#['pedagogy : principles and methods of instruction\n', 'Prudent : Careful and sensible\n', 'Onus : Responsibility\n',...
#file.close()

#APPENDING DATA:
# file=open('D:\Dairy\The Hindu Vocab.txt','a')
# file.write("iconoclast = who breaks the taboo")
# file.close()































