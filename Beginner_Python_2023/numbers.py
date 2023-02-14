#working with numbers
print(1)
print(0)
print(-1)
#making calculations
print(1+1)
print(1*0)
print(0-1)
#making a little complex calculations
print(1+0*2)
#but
print((1+0)*2)
#module calculations --returns the remainder
print(10%3)
#storing numbers 
my_num = 23
print(my_num)
#to make the number a string
print(str(my_num) + " is my age")
#note that without calling it a string it becomes an error
# this line will yield an error: print(my_num + " is my age")

my_num = -8
print(abs(my_num)) #absolute number of my_num
print(pow(2,128)) #IPv6 #pow simply means raise to the power
print(max(2, 128)) #returns maximum number
print(min(2,128)) #returns the smaller number
print(round(2.7237)) #rounds to the nearest whole number 

#we have serveral import methods in python - using import
from math import *
my_num = 7
print(floor(7.9)) #this floor prints out the number before the decimal
print(ceil(7.9)) #this ceil prints out the rounded figure
print(sqrt(128)) #this prints out the square root


