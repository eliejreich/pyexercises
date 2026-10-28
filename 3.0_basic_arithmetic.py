"""Exercise 3.0 — Computing with what the user typed

WHAT THE PROGRAM MUST DO
    Ask for two numbers and display the result of the four operations.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What should your program do when the second number is zero? Decide, write your
       decision down, and only then implement it.

WHAT THE AI CANNOT KNOW
    Your answer to question 4. There are at least three defensible ones: refuse the
    value and ask again, display a message instead of a result, or stop the program.
    Pick one and be able to defend it.

CHECK IT YOURSELF
    Compute 7 divided by 2 in your head. Run your program with 7 and 2. If your program
    shows 3, it is not wrong by accident: find out why, and write the reason in a comment.
    Then run it with 0 as the second number.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In:
# 2. Process:
# 3. Out:
# 4. What happens when the second number is zero, and why:


# Your code below
# 1. In:
#    Two numbers entered by the user via the input() function.
# 2. Process:
#    The program prompts for two inputs, converts them to floats (with validation loops to prevent crashes on non-numeric input),
#    calculates addition, subtraction, and multiplication, and handles division separately to avoid division by zero.
# 3. Out:
#    The results of the four arithmetic operations (addition, subtraction, multiplication, and division or an error message for division).
# 4. What happens when the second number is zero, and why:
#    Decision: Display a clear message ("Division by zero is undefined") specifically for division, while still showing the valid results for addition, subtraction, and multiplication.
#    Defense: This is user-friendly because a zero second number is completely valid for +, -, and *, so stopping the whole program or rejecting the input entirely would unnecessarily discard useful calculations.


# Helper function to prompt and validate numeric input (anti-crash)
def get_valid_number(prompt):
    while True:
        user_input = input(prompt).strip()
        try:
            return float(user_input)
        except ValueError:
            print("Invalid input! Please enter a valid number (e.g., 5 or 3.14).\n")


# Get validated numbers from the user
num1 = get_valid_number("Enter the first number: ")
num2 = get_valid_number("Enter the second number: ")

# Compute operations
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2

# Display results
print("\n--- Results ---")
print(f"Addition ({num1} + {num2}):       ", addition)
print(f"Subtraction ({num1} - {num2}):    ", subtraction)
print(f"Multiplication ({num1} * {num2}): ", multiplication)

# Handle division safely
if num2 == 0:
    print(f"Division ({num1} / {num2}):       Undefined (Cannot divide by zero)")
else:
    division = num1 / num2
    print(f"Division ({num1} / {num2}):       ", division)


# CHECK IT YOURSELF
#
# Test 1: 7 divided by 2
# Inputs: 7 and 2
# Expected: 3.5
# Reason note: If a Python program displays 3 instead of 3.5 for 7 / 2, it is because integer division (//) was used instead of float division (/),
# or in older Python versions (Python 2), dividing two integers automatically truncated the decimal result to an integer.
# Using standard division `/` in Python 3 yields 3.5 directly.
#
# Test 2: Second number as 0
# Inputs: 7 and 0
# Addition: 7.0
# Subtraction: 7.0
# Multiplication: 0.0
# Division: Undefined (Cannot divide by zero) — program executes cleanly without throwing a ZeroDivisionError crash.