#perform basic arthmetric operations +-*/

print("Welcome to my calculator pro edition!")

num1 = float(input("Enter a number: "))
operator = input("Enter an operator: ")
num2 = float(input("Enter another number: "))

if operator == "/" :
    print(num1 / num2)
elif operator == "*" :
    print(num1 * num2)   
elif operator == "+" :
    print(num1 + num2)
elif operator == "-" :
    print(num1 - num2)
else:
    print("Input a valid operator + - * / ") 
