#using the return statement in python functions
#the return keywords helps python return a value back to the caller

from unittest import result


def cube(num):
    return num*num*num
#you cannot add any code after the return it ends at return

result = cube(4)
print(result)   
