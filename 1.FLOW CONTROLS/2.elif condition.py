# Here we learn to check multiple conditions using elif statement
a = int(input("enter the value of a:"))
# Here a can be assigned with particular value also but I used user input model also
if a == 10:
    print("a is TEN")  #
elif a == 20:
    print("a is TWENTY")
elif a == 30:
    print("a is THIRTY")
# enter the value of a:10 a is TEN
# enter the value of a:20 a is TWENTY
# enter the value of a:30 a is THIRTY
# enter the value of a:40 ___________
# else statement is optional, even if nothing is mentioned and above total result is 0, answer will be nothing
else:
    print("a is SOMETHING_ELSE")
    # enter the value of a:40 a is SOMETHING_ELSE
