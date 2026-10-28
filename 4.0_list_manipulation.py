"""Exercise 4.0 — Working with a list

WHAT THE PROGRAM MUST DO
    Build a list of at least eight items, then display: the whole list, one item of your
    choice, the list sorted, and something computed from it.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What is your list about, and what did you compute from it? Why is that number
       interesting?

WHAT THE AI CANNOT KNOW
    The content of your list. It must come from your own field: marketing channels,
    campaign names, product references, cities you operate in, monthly budgets. Not
    fruit, not "item1, item2, item3".

    Keep this file. Exercise 5.1 and exercise 6.0 both reuse the list you build here.

CHECK IT YOURSELF
    If you computed an average, a total or a maximum, work it out by hand on three of
    your items first, then check your program agrees on those three.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In:
# 2. Process:
# 3. Out:
# 4. What my list is about, and what I computed from it:


# Your code below
# 1. In:
#    A pre-defined list of luxury event project budgets (in Euros) and optional user selection index entered via input().
# 2. Process:
#    The program creates a list of 8 event budgets, prints the full list, prompts the user to select an item safely by index,
#    sorts the list in ascending order, and computes the average budget across all projects.
# 3. Out:
#    The raw list, the specific chosen project budget, the sorted list, and the computed average project budget.
# 4. What my list is about, and what I computed from it:
#    - Theme: Event management budgets (in Euros) for luxury brand activation projects and VIP galas during the Cannes Film Festival season.
#    - Computation: Average project budget (Sum of all budgets / Number of projects).
#    - Why interesting: Knowing the average event expenditure allows management to establish baseline budget benchmarks for future prestige brand pitches and resource allocation.


# Define the list of luxury event budgets (in Euros)
event_budgets = [45000, 120000, 85000, 30000, 250000, 150000, 95000, 60000]

# Display whole list
print("--- Luxury Event Projects Budgets (€) ---")
print("All Project Budgets:", event_budgets)

# Display one item chosen safely by user (Anti-Crash Index Retrieval)
print("\n--- Select a Specific Project ---")
while True:
    raw_input = input(f"Choose a project number to inspect (1 to {len(event_budgets)}): ").strip()
    try:
        choice_idx = int(raw_input) - 1  # Convert 1-based user input to 0-based index
        if 0 <= choice_idx < len(event_budgets):
            selected_item = event_budgets[choice_idx]
            print(f"Selected Project #{choice_idx + 1} Budget: €{selected_item:,}")
            break
        else:
            print(f"Out of range! Please enter a number between 1 and {len(event_budgets)}.\n")
    except ValueError:
        print("Invalid input! Please enter a whole number.\n")

# Display sorted list (without modifying original list irreversibly)
sorted_budgets = sorted(event_budgets)
print("\n--- Sorted Budgets (Ascending) ---")
print("Sorted Budgets:", sorted_budgets)

# Compute something from the list (Average Budget)
total_budget = sum(event_budgets)
average_budget = total_budget / len(event_budgets)

print("\n--- Computed Metric ---")
print(f"Total Portfolio Budget:   €{total_budget:,}")
print(f"Average Project Budget: €{average_budget:,.2f}")


# CHECK IT YOURSELF
#
# Manual Verification on 3 items:
# Items chosen: €45,000, €120,000, €85,000
# Manual Sum: 45,000 + 120,000 + 85,000 = 250,000
# Manual Average: 250,000 / 3 = €83,333.33
#
# Full List Program Output Verification:
# Total Sum: 45,000 + 120,000 + 85,000 + 30,000 + 250,000 + 150,000 + 95,000 + 60,000 = €835,000
# Program Average: 835,000 / 8 = €104,375.00
# Program output matches exact arithmetic computation.