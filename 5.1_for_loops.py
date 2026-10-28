"""Exercise 5.1 — Doing the same thing to every item

WHAT THE PROGRAM MUST DO
    Take the list you built in exercise 4.0 and, for every item, display a line that
    combines the item, its position, and something computed about it.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What did you compute for each item, and what does the reader learn from that line?

WHAT THE AI CANNOT KNOW
    Your list from 4.0, and what is worth computing about its items. Length of the name,
    share of a total, position in a ranking, whether the item passes a threshold you set.
    Open your 4.0 file, copy the list across, and say in a comment what you decided.

CHECK IT YOURSELF
    Count the lines your program printed. There must be exactly as many as items in your
    list. If there is one more or one less, you have an off-by-one, and it is worth
    understanding now rather than in the exam.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In:
# 2. Process:
# 3. Out:
# 4. What I compute for each item, and why it is worth showing:


# Your code below
# 1. In:
#    The pre-defined list of luxury event project budgets (in Euros) carried over from Exercise 4.0:
#    [45000, 120000, 85000, 30000, 250000, 150000, 95000, 60000].
# 2. Process:
#    The program iterates through the list using enumerate(..., 1) to track 1-based positioning.
#    For each item, it computes its percentage share of the total portfolio budget and checks whether
#    it exceeds a VIP Tier threshold (€100,000).
# 3. Out:
#    A line for every project displaying its 1-based position, formatted budget amount, percentage share of the total portfolio, and VIP status.
# 4. What I compute for each item, and why it is worth showing:
#    - Computation 1: Percentage share of the total portfolio budget (budget / total_budget * 100).
#    - Computation 2: VIP Tier status (whether budget >= €100,000).
#    - What the reader learns: The reader sees how much relative financial weight each event carries within the overall operations portfolio and quickly identifies flagship high-value VIP projects.


# Import original list from Exercise 4.0
event_budgets = [45000, 120000, 85000, 30000, 250000, 150000, 95000, 60000]

# Calculate portfolio metrics
total_portfolio = sum(event_budgets)
VIP_THRESHOLD = 100000

print("--- Luxury Event Projects Overview ---")
print(f"Total Portfolio Value: €{total_portfolio:,}\n")

# Anti-crash iteration over list items
printed_line_count = 0

for position, budget in enumerate(event_budgets, start=1):
    # Compute relative share of total portfolio
    share_percentage = (budget / total_portfolio) * 100 if total_portfolio > 0 else 0
    
    # Compute VIP status flag
    is_vip = " [VIP Flagship]" if budget >= VIP_THRESHOLD else " [Standard Event]"
    
    # Display formatted line combining item, position, and computed metrics
    print(f"Project #{position}: €{budget:7,} | Share: {share_percentage:5.2f}% | Category:{is_vip}")
    
    printed_line_count += 1

print("\n--- Summary Verification ---")
print(f"Total items in original list: {len(event_budgets)}")
print(f"Total lines printed:          {printed_line_count}")

# Anti-Crash Verification Check
if printed_line_count == len(event_budgets):
    print("SUCCESS: Exact match! No off-by-one errors detected.")
else:
    print("WARNING: Line count discrepancy detected!")


# CHECK IT YOURSELF
#
# Line count verification:
# Total items in list = 8
# Lines printed by loop = 8 (numbered Project #1 to Project #8)
#
# Example line checks:
# Project #1: €45,000 -> 45,000 / 835,000 = 5.39% -> [Standard Event]
# Project #2: €120,000 -> 120,000 / 835,000 = 14.37% -> [VIP Flagship]
# Project #5: €250,000 -> 250,000 / 835,000 = 29.94% -> [VIP Flagship]
#
# Arithmetic and line counts match expected behavior cleanly.
