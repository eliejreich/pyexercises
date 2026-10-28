"""Exercise 3.1 — Odd or even (homework)

WHAT THE PROGRAM MUST DO
    Ask the user for a number N, then say for every number from 1 to N whether it is
    odd or even.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What should happen if the user types 0, a negative number, or 5000?
       Decide the three behaviours before writing anything.

WHAT THE AI CANNOT KNOW
    Your three decisions. An assistant asked for "odd or even from 1 to N" will produce
    a program that behaves absurdly on 0 and on -4, and will happily print five thousand
    lines. Those are your calls, not its.

CHECK IT YOURSELF
    Run it with 6. You should see three odd and three even. Count them.
    Then run it with your three edge cases and confirm each does what you decided.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In:
# 2. Process:
# 3. Out:
# 4. What happens on 0, on a negative number, on a very large number:


# Your code below
# 1. In:
#    A number N entered by the user via the input() function (can be an integer or a decimal/float).
# 2. Process:
#    The program converts the input to a float to handle non-integers like 5.5, truncates or rounds down float inputs using math.floor()
#    to establish the upper integer boundary, then iterates from 1 up to floor(N) checking i % 2 == 0 for each number.
# 3. Out:
#    A brief notice if a float was entered, followed by a message for every whole number from 1 to floor(N) stating whether it is "Odd" or "Even".
# 4. What happens on 0, on a negative number, on a very large number:
#    - 0: Display a clear message stating that N must be greater than 0, since the sequence starts at 1.
#    - Negative number (e.g., -4): Display an error message explaining that the program only counts upwards from 1.
#    - Very large number (e.g., 5000): Cap the maximum limit at 100 to avoid flooding the console output.

import math

# Anti-crash prompt accepting whole numbers and decimals
while True:
    raw_input = input("Enter a positive number N (e.g., 6 or 5.5): ").strip()
    try:
        raw_N = float(raw_input)
        break
    except ValueError:
        print("Invalid input! Please enter a valid number.\n")

# Convert float input to nearest lower integer boundary (e.g., 5.5 becomes 5)
N_limit = math.floor(raw_N)

if raw_N != N_limit and raw_N > 0:
    print(f"Note: You entered {raw_N}. Counting up to whole number {N_limit}.")

# Edge Case Decisions
MAX_LIMIT = 100

if N_limit <= 0:
    print(f"Error: N must be at least 1 (you entered {raw_N}). No whole numbers to display from 1 to {N_limit}.")
elif N_limit > MAX_LIMIT:
    print(f"Warning: {raw_N} is too large to display line-by-line cleanly. Capping output to 1..{MAX_LIMIT}.\n")
    N_limit = MAX_LIMIT

# Main Loop: Check odd/even from 1 to N_limit
if N_limit > 0:
    print(f"\n--- Checking whole numbers 1 to {N_limit} ---")
    for i in range(1, N_limit + 1):
        if i % 2 == 0:
            print(f"{i} is Even")
        else:
            print(f"{i} is Odd")


# CHECK IT YOURSELF
#
# Test 1: Float input N = 5.5
# Output: "Note: You entered 5.5. Counting up to whole number 5."
# Results: 1 is Odd, 2 is Even, 3 is Odd, 4 is Even, 5 is Odd.
# Verification: 3 odd numbers (1, 3, 5) and 2 even numbers (2, 4).
#
# Test 2: Standard integer input N = 6
# Output: 1 is Odd, 2 is Even, 3 is Odd, 4 is Even, 5 is Odd, 6 is Even.
# Verification: 3 odd and 3 even.
#
# Test 3: Edge case N = 0
# Output: "Error: N must be at least 1 (you entered 0.0)."
#
# Test 4: Edge case N = -4
# Output: "Error: N must be at least 1 (you entered -4.0)."
#
# Test 5: Edge case N = 5000
# Output: "Warning: 5000.0 is too large... Capping output to 1..100."