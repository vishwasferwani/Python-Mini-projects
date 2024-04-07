#calculator
from replit import clear
from art import logo

def add(n1,n2):
    return n1 + n2

def subtract(n1,n2):
    return n1-n2

def multiply(n1,n2):
    return n1*n2

def divide(n1,n2):
    return n1/n2

# key is operator and value is name of function
def calculator():
    print(logo)
    operations={
        "+": add,
        "-": subtract,
        "*": multiply,
        "/": divide,
    }
    num1 = float(input("Enter 1st num "))
    
    for operators in operations:
        print(operators)
    further_choice = True
    while further_choice:
        choice = input("Enter operation ")
        num2 = float(input("Enter next num "))
        calculator_function = operations[choice]
        answer = calculator_function(num1,num2)
        print(f"{num1} {choice} {num2} = {answer}")
    
        
        further = input(f"type y to calculate with {answer} or type n to start a new calculation: ")
        num1 = answer
        if further ==  "n":
            further_choice= False
            clear()
            calculator()

calculator()
    