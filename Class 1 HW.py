import math
#Task 1

name = input("Please enter a name:")
print("Hello "+name)

#Task 2
number1 = float(input("Please enter 1st number:"))
number2 = float(input("Please enter 2nd number:"))
answer = number1/number2
print(math.ceil(answer))

#or num1 = input("1st number")
#num2 = input("2nd number")
#num1 = int(num1)
#num2 = int(num2)
#result = num1/num2
#result = int(result+0.5)
#print("Result: "+str(result))

#Task 3
from math import pi
r = float(input("Please enter the radius of the circle:"))
print("The area is: "+str(r)+str(pi*r**2))