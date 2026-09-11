def main():
    calculator()
    
    
def calculator():
    try:
        number1 = float(input("Enter number 1: "))
        number2 = float(input("Enter number 2: "))
        operator = input("Enter operator (+, -, *, /): ")
        
        if operator == "+":
            print(f"Addition is: {get_add(number1,number2)}")
        
        elif operator == "-":
            print(f"Subtraction is: {get_subtraction(number1,number2)}")
        
        elif operator == "*":
            print(f"Multiplication is: {get_multiplication(number1,number2)}")
        
        elif operator == "/":
            print(f"Division is: {get_division(number1,number2)}")

        else:
            print("Invalid operator.")
        
    except ValueError:
        print("Invalid number. Please enter a numeric value.")
    
def get_add(a,b):
    addition = a + b
    return addition

def get_subtraction(a,b):
    subtraction = a - b
    return subtraction

def get_multiplication(a,b):
    multiplication = a * b
    return multiplication

def get_division(a,b):
    while True:
        try:
            division = a/b
            return division
        except ZeroDivisionError:
            print("Can't divide by 0")
            
            try:
                b = float(input("Enter number 2 again: "))
            except ValueError:
                print("Invalid number. Please enter a numeric value.")
                b = 0

    
main()