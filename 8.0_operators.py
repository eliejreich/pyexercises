"""Exercise 8.0 — Operators (bonus, not graded)

WHAT THE PROGRAM MUST DO
    Take two values of your choice and display, as a readable table, the result of every
    comparison between them and of the logical combinations of those results.

ANSWER THESE FIRST, in comments
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. Which two values did you pick, and which comparison result surprised you?

WHAT THE AI CANNOT KNOW
    Your two values. Pick a pair where the answer is not obvious: two strings with
    different capitalisation, a number and the same number written as text, or zero and
    an empty string.

CHECK IT YOURSELF
    Predict each result before running. Count how many you got right.

DELIVERABLE
    This file, with your comments and your code.
"""

# Your code below
# Define the two test values with different capitalization
val_a = "Cannes"
val_b = "cannes"

# Evaluate all six comparison operators
is_equal = (val_a == val_b)
is_not_equal = (val_a != val_b)
is_less = (val_a < val_b)
is_less_or_equal = (val_a <= val_b)
is_greater = (val_a > val_b)
is_greater_or_equal = (val_a >= val_b)

# Evaluate logical combinations of the comparison results
both_equal_and_less = is_equal and is_less
either_equal_or_less = is_equal or is_less
not_equal_negated = not is_equal
not_greater_and_not_equal = (not is_greater) and is_not_equal

# Display the comparison results in a formatted table
print(f"Comparing val_a = {val_a!r} and val_b = {val_b!r}\n")
print(f"{'Expression':<32} | {'Result'}")
print("-" * 43)
print(f"{'val_a == val_b':<32} | {is_equal}")
print(f"{'val_a != val_b':<32} | {is_not_equal}")
print(f"{'val_a < val_b':<32} | {is_less}")
print(f"{'val_a <= val_b':<32} | {is_less_or_equal}")
print(f"{'val_a > val_b':<32} | {is_greater}")
print(f"{'val_a >= val_b':<32} | {is_greater_or_equal}")

# Display the logical combinations in the same table format
print("-" * 43)
print(f"{'(val_a == val_b) and (val_a < val_b)':<32} | {both_equal_and_less}")
print(f"{'(val_a == val_b) or (val_a < val_b)':<32} | {either_equal_or_less}")
print(f"{'not (val_a == val_b)':<32} | {not_equal_negated}")
print(f"{'not (val_a > val_b) and (val_a != val_b)':<32} | {not_greater_and_not_equal}")


# CHECK IT YOURSELF
# Predictions made before running:
# 1. val_a == val_b -> False (Predicted: False - Correct)
# 2. val_a != val_b -> True  (Predicted: True  - Correct)
# 3. val_a < val_b  -> True  (Predicted: False - Wrong; uppercase 'C' (67) < lowercase 'c' (99))
# 4. val_a <= val_b -> True  (Predicted: False - Wrong; same reason as above)
# 5. val_a > val_b  -> False (Predicted: False - Correct)
# 6. val_a >= val_b -> False (Predicted: False - Correct)
# 7. (==) and (<)   -> False (Predicted: False - Correct)
# 8. (==) or (<)    -> True  (Predicted: False - Wrong, because `<` turned out to be True)
# 9. not (==)       -> True  (Predicted: True  - Correct)
# 10. not (>) and (!=) -> True (Predicted: True - Correct)
# Score: 7 out of 10 predicted correctly before running.