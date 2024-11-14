#pyqt5
# This framework can be expanded with more operations or a GUI in future versions.
def runCalc():
    print("Calculator - \n\nOptions:")
    print("Addition - press 1")
    print("Subtraction - press 2")
    print("Multiplication - press 3")
    print("Division - press 4")
    
    # Getting the user input for operation
    menuInput = int(input("Choose an operation by entering the corresponding number: "))
    
    # Getting numbers for the calculation
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # Conditional statements to perform the chosen operation
    if menuInput == 1: 
        result = addition(num1, num2)
    elif menuInput == 2:
        result = subtraction(num1, num2)
    elif menuInput == 3:
        result = multiplication(num1, num2)
    elif menuInput == 4:
        result = division(num1, num2)
    else:
        print("Invalid selection.")
        return

    print(f"The result is: {result}")


# Define operation functions
def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b

# Run the calculator
runCalc()