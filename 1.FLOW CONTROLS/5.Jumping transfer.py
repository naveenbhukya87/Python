# Jumping transfer is to command with words 'break' and 'continue' either to stop execution or to exclude particular
# numbers. Let's see...
# To print 1-10 numbers
for i in range(1, 10):
    print(i)  # OUTPUT: 1 2 3 4 5 6 7 8 9

# To print 1-5 numbers
for i in range(1, 10):
    if i == 5:
        break
    print(i)  # OUTPUT: 1 2 3 4
# PROGRAM LOGIC: When i=1, if i==5 is false and it doesn't enter if loop and continue with print statement and the same
# continues until i=5 where if i==5 becomes true and it enters into if loop and execution gets break.

# To print 1-10 numbers by excluding a number '5' and for this "CONTINUE" is used:
for i in range(1, 10):
    if i == 5:
        continue
    print(i)  # OUTPUT: 1 2 3 4 6 7 8 9
# PROGRAM LOGIC: When i=1, if i==5 is false and it doesn't enter if loop and continue with print statement and the same
# continues until i=5 where if i==5 becomes true and it enters into if loop and execution gets break and 5 is not printed
# and again for i=6 if loop becomes false and gets printed and continues upto 9
