#######Calculator#######

def main():
    calculator()

def calculator():
    number1 = float(input("Enter number 1: "))
    number2 = float(input("Enter number 2: "))
    operator = input("Enter Operator: ").strip()
    
    if operator == "+":
        print(f"Addition = {add(number1, number2)}")
    elif operator == "-":
        print(f"Subtraction = {subtract(number1, number2)}")
    elif operator == "*":
        print(f"Multiplication = {multiply(number1, number2)}")
    elif operator == "/":
        print(f"Division = {divide(number1, number2)}")
        
    '''The only known problem is that: 10 / 0 will crash, 
    but that's fine for now. When you reach Exceptions, 
    we can return to this calculator and improve it.'''
    
def add(a,b):
    result = a + b
    return result

def subtract(a,b):
    result = a - b
    return result

def multiply(a,b):
    result = a * b
    return result

def divide(a,b):
    result = a / b
    return result
    

main()