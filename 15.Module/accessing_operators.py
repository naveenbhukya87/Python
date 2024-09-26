# Approach_(1)
# Importing module directly and Accessing contents from module
from operators import add, mult  # Importing contents from module directly
from operators import *  # Importing contents from module directly
import operators  # Importing module directly
print("Importing module directly and Accessing contents from module")
operators.add(10, 20)  # 30        #Accessing contents from module
operators.mult(10, 15)  # 150       #Accessing contents from module

# Approach_(2)
# Importing contents from module directly
print("Importing contents from module directly")
add(10, 20)  # 30          #Assigning elements to the accessed content
mult(10, 15)  # 150         #Assigning elements to the accessed content

# Approach_(3)
# Importing all contents from module directly by just "*" instead of calling required content
print(
    r"Importing all contents from module directly by just [*] instead of calling required content")
add(10, 20)  # 30          #Assigning elements to the accessed content
mult(10, 15)  # 150         #Assigning elements to the accessed content
