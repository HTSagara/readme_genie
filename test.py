# A simple Python program to test complexity analysis

def calculate_factorial(n):
    """Returns the factorial of a number."""
    if n == 0:
        return 1
    else:
        return n * calculate_factorial(n-1)

def is_prime(num):
    """Checks if a number is prime."""
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

print(calculate_factorial(5))
print(is_prime(11))
