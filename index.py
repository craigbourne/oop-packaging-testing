"""
Calculate factorial of a non-negative integer.
"""

def factorial (num):
    """
    Calculates the factorial of a non-negative integer.
      Args: number: A non-negative integer
      Returns: The factorial of the input number
    """

    if num == 1:
        return 1
    return num * factorial(num-1)

NUM = 3
print("The factorial of", NUM, "is", factorial(NUM))
