#we can compare numbers, string, boolean...etc

def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

print(max_num(29, 23, 57))  
#in the above, we are comparing for the maximum number
# the first if statement checks if true for num1 else
# it moves to the second statement for num2 
# else it execute num3 as the max 
# the condition is satisfied wherever the condition is met 
