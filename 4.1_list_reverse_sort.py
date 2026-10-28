"""Exercise 4.1 — Reordering without losing the original (homework)

WHAT THE PROGRAM MUST DO
    Starting from the list you built in exercise 4.0, display it in four different
    orders, and prove at the end that the original list has not been damaged.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. Which four orders did you choose, and in which of them is your original list
       modified rather than copied?

WHAT THE AI CANNOT KNOW
    That your original must survive. Some ways of reordering a list change it in place,
    others return a new one. Find out which is which, and say so in your comments.
    That distinction is the entire exercise.

CHECK IT YOURSELF
    The last line of your program must display the original list. Compare it, item by
    item, with what you wrote in 4.0. If it has moved, your program is wrong even
    though it ran.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: a list of 8 monthly digital marketing campaign budgets (in EUR): [4500, 12000, 8500, 3200, 15000, 9100, 6800, 11400].
# 2. Process: the program displays the list in 4 different orders (ascending, descending, reversed, and sorted via copy) using sorted(), slicing, and .sort(), then prints the original list to prove it was not modified.
# 3. Out: four different ordered views of the campaign budgets printed to the terminal, followed by the intact original list.
# 4. My four orders, and which ones modify the original:
#  Order 1: Ascending order using sorted() -> Creates a NEW list (does NOT modify original).
#  Order 2: Descending order using sorted(..., reverse=True) -> Creates a NEW list (does NOT modify original).
#  Order 3: Reversed order using slicing [::-1] -> Creates a NEW list (does NOT modify original).
#  Order 4: Sorted order using .sort() -> MODIFIES the list in place! To protect the original list, we execute .sort() on a copy (.copy()).


# Your code below
# Original list built in exercise 4.0
# 1. In:
#    A pre-defined list of luxury event project budgets (in Euros) from Exercise 4.0: [45000, 120000, 85000, 30000, 250000, 150000, 95000, 60000].
# 2. Process:
#    The program creates four distinct reordered views of the list using both non-destructive methods (sorted(), slicing)
#    and a destructive method (.sort()) safely executed on a shallow copy (.copy()). It then displays the original list to verify it remains unchanged.
# 3. Out:
#    The four differently ordered versions of the event budgets, followed by the intact original list.
# 4. My four orders, and which ones modify the original:
#    - Order 1: Ascending order using sorted() -> Creates a NEW list (does NOT modify original).
#    - Order 2: Descending order using sorted(..., reverse=True) -> Creates a NEW list (does NOT modify original).
#    - Order 3: Reversed order using slicing [::-1] -> Creates a NEW list (does NOT modify original).
#    - Order 4: Sorted in-place using .sort() -> MODIFIES the list in-place! To protect the original list, we must execute .sort() on a separate copy created via .copy().


# Define original list from Exercise 4.0
event_budgets = [45000, 120000, 85000, 30000, 250000, 150000, 95000, 60000]

print("--- Original Initial List ---")
print("Original:", event_budgets)
print()

# Order 1: Ascending (Non-destructive using sorted())
ascending_budgets = sorted(event_budgets)
print("1. Ascending order (sorted()):             ", ascending_budgets)

# Order 2: Descending (Non-destructive using sorted(..., reverse=True))
descending_budgets = sorted(event_budgets, reverse=True)
print("2. Descending order (sorted(reverse=True)):", descending_budgets)

# Order 3: Reversed (Non-destructive using slicing [::-1])
reversed_budgets = event_budgets[::-1]
print("3. Reversed order (slicing [::-1]):        ", reversed_budgets)

# Order 4: Sorted via .sort() (In-place modification applied safely to a COPY)
copied_budgets = event_budgets.copy()  # Prevents modifying original event_budgets
copied_budgets.sort()
print("4. In-place sorted copy (.copy().sort()):   ", copied_budgets)

# Proof that original list remains completely undamaged
print("\n--- FINAL VERIFICATION ---")
print("Original list after operations:", event_budgets)

# Anti-Crash Proof Check
if event_budgets == [45000, 120000, 85000, 30000, 250000, 150000, 95000, 60000]:
    print("SUCCESS: Original list matches Exercise 4.0 exactly item-by-item!")
else:
    print("ERROR: Original list was modified!")


# CHECK IT YOURSELF
#
# Original list in Exercise 4.0: [45000, 120000, 85000, 30000, 250000, 150000, 95000, 60000]
# Order 1 (Ascending):  [30000, 45000, 60000, 85000, 95000, 120000, 150000, 250000]
# Order 2 (Descending): [250000, 150000, 120000, 95000, 85000, 60000, 45000, 30000]
# Order 3 (Reversed):   [60000, 95000, 150000, 250000, 30000, 85000, 120000, 45000]
# Order 4 (Copy Sort):  [30000, 45000, 60000, 85000, 95000, 120000, 150000, 250000]
#
# Final Verification Output:
# [45000, 120000, 85000, 30000, 250000, 150000, 95000, 60000]
# Item-by-item comparison proves the original list was not altered or damaged.