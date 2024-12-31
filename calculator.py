# Add appropriate commenting and documentation for the code below.
"""
Calculator for basic arithmetic operations through command-line.
Perform addition, subtraction, multiplication, and division on two numbers.
Program runs until the user explicitly chooses to stop.
"""

def add(x, y):
    """
    Add two numbers.
    Arguments:
        x (float): The first number to add
        y (float): The second number to add
    Returns: float: The sum of x and y
    """
    return x + y

def subtract(x, y):
    """
    Subtract one number from another.
    Arguments:
        x (float): The number to subtract from
        y (float): The number to subtract
    Returns: float: The result of x minus y
    """
    return x - y

def multiply(x, y):
    """
    Multiply two numbers.
    Arguments:
        x (float): The first number to multiply
        y (float): The second number to multiply
    Returns:
        float: The product of x and y
    """
    return x * y

def divide(x, y):
    """
    Divide one number by another.
    Arguments:
        x (float): The dividend (number to be divided)
        y (float): The divisor (number to divide by)
    Returns: float: The quotient of x divided by y
    Raises: ZeroDivisionError: If the divisor (y) is zero
    """
    if y == 0:
        raise ZeroDivisionError("Division by zero is not allowed")
    return x / y

# Display the menu of available operations
print("Select operation.") 
print("1.Add") 
print("2.Subtract") 
print("3.Multiply") 
print("4.Divide") 

# Main calculation loop
while True: 
    # Get user's choice of operation
    choice = input("Enter choice(1/2/3/4): ")  

    # Process valid operation choices
    if choice in ('1', '2', '3', '4'): 
        # Get input numbers from user
        num1 = float(input("Enter first number: ")) 
        num2 = float(input("Enter second number: ")) 

        # Perform the selected operation and display result
        try:
            if choice == '1':
                print(num1, "+", num2, "=", add(num1, num2)) 
            elif choice == '2':
                print(num1, "-", num2, "=", subtract(num1, num2)) 
            elif choice == '3':
                print(num1, "*", num2, "=", multiply(num1, num2)) 
            elif choice == '4':
                print(num1, "/", num2, "=", divide(num1, num2)) 
        except ZeroDivisionError:
            print("Error: Cannot divide by zero")
            continue

        # Check if user wants to perform another calculation
        next_calculation = input("Would you like to perform another calculation? (yes/no): ") 
        if next_calculation.lower() == "no": 
            break 
    else:
        print("Invalid input. Please select 1, 2, 3, or 4.")