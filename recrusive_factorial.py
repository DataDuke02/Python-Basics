n = int(input("Enter a non-negative integer: ")) # Validate user input
def factorial(n):
    """
    Calculate the factorial of n using recursion.

    Args:
        n (int): A non-negative integer

    Returns:
        int: The factorial of n
    """
    if n == 0 or n == 1:  # Base cases for recursion
        return 1
    else:  # Recursive case
        return n * factorial(n - 1)

print(factorial(n))
