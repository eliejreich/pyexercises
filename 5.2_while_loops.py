"""Exercise 5.2 — Repeating until something changes

WHAT THE PROGRAM MUST DO
    Keep asking the user something until a condition you define is met, then display a
    summary of what happened during the loop.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What is your stop condition, what is your maximum number of attempts, and what
       does your summary contain?

WHAT THE AI CANNOT KNOW
    Your stop condition and your safety limit. An assistant asked for a while loop will
    write one that can run for ever if the user never gives the expected answer. Decide
    how many attempts you allow, and what your program does when that limit is reached.

    Accepting "Yes", "yes" and " yes " as the same answer is your decision too. Make it
    and write it down.

CHECK IT YOURSELF
    Run it and never give the expected answer. If your program is still running after
    your stated maximum, it is wrong. Then run it and answer with capitals and extra
    spaces.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In:
# 2. Process:
# 3. Out:
# 4. My stop condition, my attempt limit, my summary:

i = 0
while i < 10:
    print("This is attempt number:", i + 1)
    i = i + 1

print("This is the end of the loop. The maximum number of attempts has been reached.")

# Your code below
# 1. In:
#    User text inputs prompted repeatedly inside a loop (confirming attendance/guest list confirmation for a VIP event).
# 2. Process:
#    The program prompts the user for confirmation ("yes" or "no"). Each input is sanitized using .strip().lower() to handle extra spaces and capital letters.
#    The loop keeps track of the number of attempts and continues until either a valid "yes" response is given OR the maximum limit of 5 attempts is reached.
# 3. Out:
#    Immediate feedback after each attempt, followed by a final summary detailing total attempts, successful confirmation status, and normalized user input.
# 4. My stop condition, my attempt limit, my summary:
#    - Stop Condition: User enters "yes" (case-insensitive, ignoring leading/trailing spaces) OR attempt count reaches MAX_ATTEMPTS.
#    - Maximum Attempts Limit: 5 attempts. If reached without confirmation, the program safely halts the loop to prevent infinite repetition.
#    - Summary Contains: Total attempts made, final confirmation status (Confirmed vs. Timed Out/Failed), and last input received.


# Configuration constants
MAX_ATTEMPTS = 5
EXPECTED_CONFIRMATION = "yes"

# Tracking variables
attempt_count = 0
is_confirmed = False
last_raw_input = ""

print("--- VIP Guest List Confirmation Prompt ---")
print(f"Please confirm your attendance. You have a maximum of {MAX_ATTEMPTS} attempts.\n")

# Anti-crash repeating while loop with safety counter
while attempt_count < MAX_ATTEMPTS and not is_confirmed:
    attempt_count += 1
    
    # Prompt user for input
    last_raw_input = input(f"Attempt {attempt_count}/{MAX_ATTEMPTS} — Confirm attendance (yes/no)? ")
    
    # Sanitize input: remove leading/trailing whitespace and convert to lowercase
    clean_input = last_raw_input.strip().lower()
    
    if clean_input == EXPECTED_CONFIRMATION:
        is_confirmed = True
        print("-> Attendance successfully confirmed!\n")
    elif clean_input == "no":
        print("-> You entered 'no'. Please type 'yes' when you are ready to confirm.\n")
    else:
        print(f"-> Unrecognized input '{last_raw_input.strip()}'. Please respond with 'yes' or 'no'.\n")

# Display final summary after loop terminates
print("========================================")
print("             SUMMARY REPORT             ")
print("========================================")
print(f"Total Attempts Used: {attempt_count} / {MAX_ATTEMPTS}")
print(f"Last Raw Input:      {repr(last_raw_input)}")
print(f"Confirmation Status: {'CONFIRMED' if is_confirmed else 'FAILED (Max attempts reached)'}")

if not is_confirmed:
    print("\nNote: Maximum attempt limit was reached without valid confirmation. Session terminated safely.")


# CHECK IT YOURSELF
#
# Test 1: Never giving the expected answer ("no", "maybe", "abc")
# Inputs: 5 invalid responses in a row.
# Result: Loop stopped automatically after Attempt 5/5. Output: "FAILED (Max attempts reached)". Program did not loop infinitely.
#
# Test 2: Input with capitals and extra spaces (" YES ", "Yes", "  yes  ")
# Input: "  YES  "
# Result: Sanitized cleanly to "yes". Loop recognized confirmation on attempt 1 and terminated successfully.