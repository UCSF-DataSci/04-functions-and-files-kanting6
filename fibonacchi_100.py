#!/usr/bin/env python3
"""
Fibonacci Sequence

Create a program that generates Fibonacci numbers less than a limit and writes them to a file. The _Fibonacci_ sequence is a sequence in which each number is the sum of the two preceding ones: 

`0, 1, 1 (0+1), 2 (1+1), 3 (2+1), 5 (3+2), ...`

	- Use a function to generate Fibonacci numbers as a list
	- Use `with` statements for file operations
	- Handle potential file I/O errors with `try`/`except`
	- Use command-line arguments (via `argparse`) to specify the upper limit and output file name

Task: Generate the Fibonacci numbers less than 100 and write them to `fibonacci_100.txt`
"""
def generate_fibonacci(limit=100):
    """Generate a list of Fibonacci numbers less than the limit."""
    fibonacci_numbers = [0, 1]
    while True:
        next_number = fibonacci_numbers[-1] + fibonacci_numbers[-2]
        if next_number >= limit:
            break
        fibonacci_numbers.append(next_number)
    return fibonacci_numbers

def write_to_file(filename, fibonacci_numbers):
    """Write Fibonacci numbers to a file."""
    try:
        with open(filename, 'w') as file:
            for number in fibonacci_numbers:
                file.write(f"{number}\n")
        print(f"Fibonacci numbers successfully written to {filename}")
    except IOError as e:
        print(f"An error occurred while writing to the file: {e}")

def main():
    output_file = "fibonacci_100.txt"
    
    # Generate Fibonacci numbers less than 100
    fibonacci_numbers = generate_fibonacci(limit=100)
    
    # Write Fibonacci numbers to the file
    write_to_file(output_file, fibonacci_numbers)

if __name__ == "__main__":
    main()