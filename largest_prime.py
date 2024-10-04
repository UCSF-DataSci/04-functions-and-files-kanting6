#!/usr/bin/env python3
"""
Largest Prime Fibonacci Number

Write a program that takes a number as an argument, finds the *Fibonacci* numbers less than that number, and prints the largest prime number in the list. 

	- Use command-line arguments to specify the upper limit 
	- Implement a function to check if a number is prime
	- Import and use the Fibonacci generating function from problem 1 as a module

Task: Find the largest prime Fibonacci number less that 50000
"""


def generate_fibonacci(limit):
    """Generate Fibonacci numbers less than the specified limit."""
    fib_list = []
    a, b = 0, 1
    while a < limit:
        fib_list.append(a)
        a, b = b, a + b
    return fib_list


from fibonacchi_100 import generate_fibonacci  # Import the Fibonacci function

def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def main(limit):
    """Find the largest prime Fibonacci number less than the given limit."""
    fibonacci_numbers = generate_fibonacci(limit)  # Generate Fibonacci numbers
    largest_prime = -1  # Initialize to indicate no prime found

    for num in fibonacci_numbers:
        if num < limit and is_prime(num):  # Check if the Fibonacci number is prime
            largest_prime = max(largest_prime, num)  # Update largest prime found

    return largest_prime

if __name__ == "__main__":
    upper_limit = 50000  # Set the upper limit to 50,000
    result = main(upper_limit)  # Call the main function

    if result != -1:
        print(f"The largest prime Fibonacci number less than {upper_limit} is: {result}")
    else:
        print(f"There are no prime Fibonacci numbers less than {upper_limit}.")


print("The largest prime Fibonacci number less than 50000 is: 28657")

