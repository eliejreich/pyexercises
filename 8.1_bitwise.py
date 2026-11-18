"""Exercise 8.1 — Bitwise operators (bonus, not graded)

WHAT THE PROGRAM MUST DO
    Represent a set of permissions as bits, combine two of them, test whether a third is
    present, then add it and remove one.

ANSWER THESE FIRST, in comments
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What are your permissions about? Not files: invent a set from your own field,
       such as who may view, edit and publish a campaign.

WHAT THE AI CANNOT KNOW
    Your permission set and what each one means in your context.

CHECK IT YOURSELF
    Display the value in binary at each step and read the bits yourself.

DELIVERABLE
    This file, with your comments and your code.
"""

# Your code below
# Define individual permissions as distinct bit flags
VIEW_GUESTLIST = 1 << 0  # 1 (0b0001)
EDIT_SEATING   = 1 << 1  # 2 (0b0010)
APPROVE_BUDGET = 1 << 2  # 4 (0b0100)
SEND_INVITES   = 1 << 3  # 8 (0b1000)

# Step 1: Combine two permissions (VIEW_GUESTLIST + EDIT_SEATING) using bitwise OR (|)
coordinator_role = VIEW_GUESTLIST | EDIT_SEATING
print(f"1. Combined (View + Edit):      {coordinator_role:>2} -> {format(coordinator_role, '04b')}")

# Step 2: Test whether a third permission (APPROVE_BUDGET) is present using bitwise AND (&)
can_approve_budget = bool(coordinator_role & APPROVE_BUDGET)
print(f"2. Has APPROVE_BUDGET?:         {can_approve_budget} (mask: {format(coordinator_role & APPROVE_BUDGET, '04b')})")

# Step 3: Add the third permission (APPROVE_BUDGET) using bitwise OR (|=)
coordinator_role |= APPROVE_BUDGET
print(f"3. After adding APPROVE_BUDGET: {coordinator_role:>2} -> {format(coordinator_role, '04b')}")

# Verify that APPROVE_BUDGET is now present
can_approve_budget = bool(coordinator_role & APPROVE_BUDGET)
print(f"   Has APPROVE_BUDGET now?:     {can_approve_budget}")

# Step 4: Remove one permission (EDIT_SEATING) using bitwise AND + NOT (&= ~)
coordinator_role &= ~EDIT_SEATING
print(f"4. After removing EDIT_SEATING: {coordinator_role:>2} -> {format(coordinator_role, '04b')}")


# CHECK IT YOURSELF
# Reading the 4 bits from left to right: [SEND_INVITES | APPROVE_BUDGET | EDIT_SEATING | VIEW_GUESTLIST]
# - Step 1: 0011 -> Bit 0 (View) = 1, Bit 1 (Edit) = 1. Both permissions are active (1 + 2 = 3).
# - Step 2: 0011 & 0100 = 0000 -> Bit 2 (Approve Budget) is 0, so the check returns False.
# - Step 3: 0011 | 0100 = 0111 -> Bit 2 flips to 1. View, Edit, and Approve Budget are active (1 + 2 + 4 = 7).
# - Step 4: 0111 & ~0010 = 0101 -> Bit 1 flips back to 0. Only View (1) and Approve Budget (4) remain (1 + 4 = 5).