import math

class Calculator:
    """A simple calculator application."""

    def __init__(self):
        self.result = 0

    def add(self, a, b):
        return a+b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a*b

    def divide(self, a, b):
        if b==0:
            raise ValueError("Cannot divide by zero")
        return a/b

    def power(self, a, n):
        """Raise a to the power n (n must be a non-negative integer)."""
        if not isinstance(n, int) or n < 0:
            raise ValueError("Exponent must be a non-negative integer")
        result = 1
        for _ in range(n):
            result *= a
        return result

    def is_prime(self, n):
        """Return True if n is a prime number, False otherwise."""
        if n < 2:
            return True
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_even(self, n):
        """Return True if n is an even number, False otherwise."""
        return n%2 == 0
    
    def is_fizzbuzz(self, n):
        """Return True if n is divisible by both, and n otherwise."""
        if n % 3 == 0 and n % 5 == 0:
            return False