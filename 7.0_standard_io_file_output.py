"""Exercise 7.0 — Collecting data and saving it

WHAT THE PROGRAM MUST DO
    Ask the user for the information needed to record one entry, then save it to a CSV
    file. Running the program twice must produce two entries, not overwrite the first.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?  (name your file, and list your columns)
    4. Which columns did you choose, and what would you actually do with this file once
       it has two hundred rows in it?

WHAT THE AI CANNOT KNOW
    Your columns. They must be the ones you would really need to collect for a purpose
    you can state. See 7.0_student_data.csv for the shape of a header line, not for
    the columns to use.

    Two behaviours are yours to decide, and an assistant will guess them wrong:
    what happens the very first time, when the file does not exist yet and needs its
    header line, and what happens when a value the user typed is not acceptable.

CHECK IT YOURSELF
    Run your program three times with different values. Then open the file and count
    the lines. You should have three entries and exactly one header line. If you have
    three header lines, or one entry, your program is wrong.

DELIVERABLE
    This file, plus the CSV your program produced.
"""

# 1. In:
# 2. Process:
# 3. Out, file name and columns:
# 4. Why these columns, and what this file is for:


# Your code below
import csv
import os

# 1. In:
#    User-typed details for a single luxury event inquiry via input():
#    client/brand name, event type, estimated guest count, and estimated budget in Euros.
# 2. Process:
#    The program validates each input (rejecting blank text or non-positive numbers and
#    asking again), checks whether the CSV file already exists so it writes the header
#    only on the very first run, and appends the new row to the CSV file.
# 3. Out, file name and columns:
#    - File name: `event_inquiries.csv`
#    - Columns: `client_name`, `event_type`, `guest_count`, `budget_eur`
# 4. Why these columns, and what this file is for:
#    - Why these columns: Every event proposal needs to identify who is inquiring
#      (`client_name`), the format (`event_type`, e.g., Gala, Launch, Private Dinner),
#      venue capacity requirements (`guest_count`), and financial scope (`budget_eur`).
#    - Purpose at 200 rows: Once this file reaches 200 inquiries, I can open it in Excel
#      or analyze it with Python to calculate average budgets per event type, forecast
#      seasonal venue demand, and see which client segments generate the highest revenue.

FILENAME = "event_inquiries.csv"
COLUMNS = ["client_name", "event_type", "guest_count", "budget_eur"]

# --- 1. COLLECT AND VALIDATE USER INPUT ---

# Validate client_name (must not be empty)
client_name = input("Enter client or brand name: ").strip()
while client_name == "":
    print("Error: Client name cannot be empty.")
    client_name = input("Enter client or brand name: ").strip()

# Validate event_type (must not be empty)
event_type = input("Enter event type (e.g., Gala, Product Launch, VIP Dinner): ").strip()
while event_type == "":
    print("Error: Event type cannot be empty.")
    event_type = input("Enter event type (e.g., Gala, Product Launch, VIP Dinner): ").strip()

# Validate guest_count (must be a positive whole number)
while True:
    raw_guests = input("Enter estimated guest count: ").strip()
    try:
        guest_count = int(raw_guests)
        if guest_count > 0:
            break
        else:
            print("Error: Guest count must be greater than 0.")
    except ValueError:
        print("Error: Please enter a valid whole number (e.g., 120).")

# Validate budget_eur (must be a positive number)
while True:
    raw_budget = input("Enter estimated budget in Euros (€): ").strip()
    try:
        budget_eur = float(raw_budget)
        if budget_eur > 0:
            break
        else:
            print("Error: Budget must be greater than 0.")
    except ValueError:
        print("Error: Please enter a valid number (e.g., 85000).")


# --- 2. CHECK IF FILE EXISTS & APPEND DATA ---

# Check if the file already exists BEFORE opening it in append ("a") mode
file_exists = os.path.exists(FILENAME)

with open(FILENAME, mode="a", newline="", encoding="utf-8") as csv_file:
    writer = csv.writer(csv_file)

    # Write the header row ONLY if the file did not exist yet
    if not file_exists:
        writer.writerow(COLUMNS)

    # Append the new user entry as a single row
    writer.writerow([client_name, event_type, guest_count, budget_eur])

print(f"\nSaved entry for '{client_name}' to {FILENAME}.")