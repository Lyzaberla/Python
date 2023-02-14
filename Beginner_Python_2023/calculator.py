#building a basic calculator
from unittest import result


num1 = input("Enter a number: ")
num2 = input("Enter another number: ")
result = int(num1) + int(num2) #int will convert the input into numbers
print(result)

print("")

num1 = input("Enter a number: ")
num2 = input("Enter another number: ")
result = float(num1) + float(num2) 
#float allows for decimal inputs unlike the int
print(result)