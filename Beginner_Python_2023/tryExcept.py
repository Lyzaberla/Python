#catching errors in python and working round errors

#number = int(input("Enter a number: "))
#print(number)

#using the tryexcept method
try:
    number = int(input("Enter a number: "))
    print(number)
except: 
    print("Invalid Input")

#to specify error in python use
try:
    number = int(input("Enter a number: "))
    print(number)
except ValueError: 
    print("Invalid Input")

#we can store the exception in variable
try:
    answer = 10/0
except ZeroDivisionError as error: 
    print(error)

#using just except is too broad so always specify
 

