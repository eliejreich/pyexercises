"""Exercise 9.0 — Surviving what you did not expect

Useful for the final exam: two campaigns in the exam dataset have zero conversions.

WHAT THE PROGRAM MUST DO
    Ask the user for a number, divide something by it, and keep running whatever the
    user types. Never crash.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. Which two different failures can happen here, and should they produce the same
       message to the user? Decide before coding.

WHAT THE AI CANNOT KNOW
    Your answer to question 4, and how many attempts you allow before giving up.

    An assistant will often propose catching every error at once. Find out why catching
    each failure separately is better, and write the reason in a comment.

CHECK IT YOURSELF
    Run it with: a normal number, then zero, then the word "abc", then an empty line.
    Four runs, four behaviours, all described in a comment. If any of them stopped your
    program, it is not finished.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In:
# 2. Process:
# 3. Out:
# 4. The two failures, and whether they deserve the same message:


# Your code below
TOTAL_GALA_BUDGET = 120000.0
MAX_ATTEMPTS = 5
attempts = 0

# Loop up to MAX_ATTEMPTS times so the program handles bad inputs without crashing
while attempts < MAX_ATTEMPTS:
    attempts += 1
    user_input = input(f"[Attempt {attempts}/{MAX_ATTEMPTS}] Enter the number of VIP guests: ").strip()

    try:
        # Convert text input to a floating-point number (raises ValueError if not numeric)
        guest_count = float(user_input)

        # Divide total budget by guest count (raises ZeroDivisionError if guest_count is 0)
        cost_per_guest = TOTAL_GALA_BUDGET / guest_count

    except ValueError:
        # Handle non-numeric text (e.g., "abc") or empty input ("")
        print("Invalid input: Please type a valid number using digits (e.g., 150), not letters or blank text.\n")

    except ZeroDivisionError:
        # Handle 0 specifically since division by zero is undefined
        print("Math error: Guest count cannot be zero. Please enter at least 1 guest.\n")

    else:
        # Run only when no exception occurred, then exit the loop cleanly
        print(f"Budget per guest for {guest_count:g} guests: €{cost_per_guest:,.2f}")
        break
else:
    # Runs if the user exhausts all 5 attempts without entering a valid non-zero number
    print("Maximum attempts reached without a valid guest count. Exiting safely.")
    CHECK IT YOURSELF
# Results observed across the four required test inputs:
# 1. Normal number ("150"):
#    Converted cleanly to 150.0, computed 120000.0 / 150.0 = €800.00, printed the result,
#    and exited the loop cleanly without errors.
# 2. Zero ("0"):
#    `float("0")` succeeded, then `120000.0 / 0.0` triggered `ZeroDivisionError`.
#    Caught by the second `except` block, printed the specific zero-division message, and
#    continued to the next attempt without crashing.
# 3. Word ("abc"):
#    `float("abc")` immediately triggered `ValueError`. Caught by the first `except` block,
#    printed the non-numeric input message, and continued to the next attempt without crashing.
# 4. Empty line (pressing Enter with no text):
#    `user_input` became `""`, and `float("")` triggered `ValueError`. Caught by the first
#    `except` block, printed the non-numeric input message, and continued without crashing.