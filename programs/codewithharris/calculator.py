""" Write a calculator program which does basic calculations liek addition, substraction, multiplication and division"""

def calculator(num1,num2,operation):
    if operation == '+':
        print("Performing addition of two numbers")
        return num1+num2
    elif operation == '-':
        print("Performing substraction of two numbers")
        return num1-num2
    elif operation == '*':
        print("Performing muliplication of two numbers")
        return num1*num2
    elif operation == '/':
        print("Performing division of two numbers")
        return num1/num2
    else:
        print("Incorrect operation passed")

print(calculator(2,4,''))