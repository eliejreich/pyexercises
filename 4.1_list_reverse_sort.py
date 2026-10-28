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
campaign_budgets = [4500, 12000, 8500, 3200, 15000, 9100, 6800, 11400]
print("0. Original list at the start:")
print(campaign_budgets)
print("-" * 50)

# Order 1: Ascending order using sorted() -> returns a NEW list
order_1_ascending = sorted(campaign_budgets)
print("1. Displayed in Ascending order (using sorted()):")
print(order_1_ascending)
print("-" * 50)

# Order 2: Descending order using sorted(..., reverse=True) -> returns a NEW list
order_2_descending = sorted(campaign_budgets, reverse=True)
print("2. Displayed in Descending order (using sorted(..., reverse=True)):")
print(order_2_descending)
print("-" * 50)

# Order 3: Reversed order using slicing [::-1] -> returns a NEW list
order_3_reversed = campaign_budgets[::-1]
print("3. Displayed in Reversed order (using slicing [::-1]):")
print(order_3_reversed)
print("-" * 50)

# Order 4: In-place sorted order using .sort()
# .sort() modifies the target list directly. We apply it on a COPY to protect the original.
budgets_copy = campaign_budgets.copy()
budgets_copy.sort()
order_4_in_place_sort = budgets_copy
print("4. Displayed using .sort() on a copy (demonstrating in-place modification):")
print(order_4_in_place_sort)
print("-" * 50)

# PROOF: Display the original list to show it has not been modified or damaged
print("PROOF: Original list at the end (must match exercise 4.0 exactly):")
print(campaign_budgets)
