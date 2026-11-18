"""Exercise 10.0 — Checking the shape of text (bonus, not graded)

WHAT THE PROGRAM MUST DO
    Validate three pieces of information typed by the user, and only save them when all
    three are acceptable.

ANSWER THESE FIRST, in comments
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What are your three fields, and what makes a value acceptable for each? Write the
       rule in plain English before writing any pattern.

WHAT THE AI CANNOT KNOW
    Your three rules. "A valid email" is not a rule, it is a wish. Say what you accept
    and what you reject, and be ready to defend a borderline case.

WHAT TO WATCH
    An assistant will hand you a pattern that looks like line noise. Do not accept it
    until it has explained it to you piece by piece, and you have written that
    explanation in your own words above it.

CHECK IT YOURSELF
    For each field, prepare one value that must pass and two that must fail. Run all
    nine. Any surprise goes in a comment.

DELIVERABLE
    This file, with your comments and your code.
"""

# Your code below
# Your code below

# --- PATTERN EXPLANATIONS IN MY OWN WORDS ---

# Pattern 1: r"^[A-Z]{3}-20\d{2}-\d{2}$"
# - ^        : Start of the string (no extra characters allowed before).
# - [A-Z]{3} : Exactly 3 uppercase letters from A to Z (the city/venue prefix).
# - -        : A literal hyphen separator.
# - 20\d{2}  : The digits "20" followed by any 2 digits (\d{2}), matching years 2000-2099.
# - -        : A second literal hyphen separator.
# - \d{2}    : Exactly 2 digits (00 to 99) for the event sequence number.
# - $        : End of the string (no trailing characters allowed).
EVENT_CODE_PATTERN = r"^[A-Z]{3}-20\d{2}-\d{2}$"

# Pattern 2: r"^[a-z0-9._-]{2,}@[a-z0-9-]+\.[a-z]{2,4}$"
# - ^               : Start of the string.
# - [a-z0-9._-]{2,} : At least 2 characters ({2,}) made of lowercase letters, digits, dots, underscores, or hyphens.
# - @               : A literal "@" symbol separating username and domain.
# - [a-z0-9-]+      : One or more (+) lowercase letters, digits, or hyphens for the company domain name.
# - \.              : A literal dot (escaped with \ because a plain dot means "any character" in regex).
# - [a-z]{2,4}      : Between 2 and 4 lowercase letters for the top-level domain (e.g., fr, com, info).
# - $               : End of the string.
EMAIL_PATTERN = r"^[a-z0-9._-]{2,}@[a-z0-9-]+\.[a-z]{2,4}$"

# Pattern 3: r"^202[67]-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01])$"
# - ^                  : Start of the string.
# - 202[67]            : Matches "202" followed by either "6" or "7" (restricting bookings to 2026 or 2027).
# - -                  : A literal hyphen.
# - (0[1-9]|1[0-2])    : Either "0" followed by 1-9 (months 01-09) OR "1" followed by 0-2 (months 10-12).
# - -                  : A second literal hyphen.
# - (0[1-9]|[12]\d|3[01]) : Either 01-09, OR 10-29 ([12]\d), OR 30-31 (3[01]).
# - $                  : End of the string.
DATE_PATTERN = r"^202[67]-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01])$"


# Collect the three inputs from the user
event_code = input("Enter VIP Event Code (e.g., CAN-2026-08): ").strip()
client_email = input("Enter Corporate Client Email (e.g., claire@maison-luxe.fr): ").strip()
event_date = input("Enter Gala Date (YYYY-MM-DD, e.g., 2026-05-19): ").strip()

# Validate each field against its regular expression
code_ok = bool(re.fullmatch(EVENT_CODE_PATTERN, event_code))
email_ok = bool(re.fullmatch(EMAIL_PATTERN, client_email))
date_ok = bool(re.fullmatch(DATE_PATTERN, event_date))

# Display individual validation results
print("\n--- Validation Summary ---")
print(f"Event Code ({event_code}):   {'PASS' if code_ok else 'FAIL'}")
print(f"Client Email ({client_email}): {'PASS' if email_ok else 'FAIL'}")
print(f"Gala Date ({event_date}):    {'PASS' if date_ok else 'FAIL'}")

# Save ONLY when all three fields are acceptable
if code_ok and email_ok and date_ok:
    saved_booking = {
        "event_code": event_code,
        "client_email": client_email,
        "event_date": event_date,
    }
    with open("confirmed_vip_booking.txt", mode="w", encoding="utf-8") as outfile:
        outfile.write(f"Event Code:   {saved_booking['event_code']}\n")
        outfile.write(f"Client Email: {saved_booking['client_email']}\n")
        outfile.write(f"Gala Date:    {saved_booking['event_date']}\n")
    print("\nAll three fields are valid! Booking saved to confirmed_vip_booking.txt.")
else:
    print("\nBooking NOT saved: one or more fields failed validation.")


# CHECK IT YOURSELF
# Tested 3 values per field (1 PASS + 2 FAIL = 9 total test cases):
#
# 1. Event Code (`^[A-Z]{3}-20\d{2}-\d{2}$`):
#    - "CAN-2026-08" -> PASS (Matches 3 uppercase letters, 20xx year, and 2-digit number)
#    - "can-2026-08" -> FAIL (Lowercase prefix rejected)
#    - "CAN-1999-8"  -> FAIL (Year does not start with 20, and trailing number has only 1 digit)
#
# 2. Corporate Client Email (`^[a-z0-9._-]{2,}@[a-z0-9-]+\.[a-z]{2,4}$`):
#    - "claire.dubois@maison-luxe.fr" -> PASS (Valid local part, domain, and 2-letter TLD)
#    - "Claire@Maison-Luxe.fr"        -> FAIL (Uppercase letters rejected by `[a-z]` rule)
#    - "claire@maison-luxe"           -> FAIL (Missing dot and top-level domain extension)
#
# 3. Gala Date (`^202[67]-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01])$`):
#    - "2026-05-19" -> PASS (Valid 2026 year, month 05, day 19)
#    - "19/05/2026" -> FAIL (Wrong order and slashes instead of hyphens)
#    - "2026-13-40" -> FAIL (Month 13 and day 40 rejected)
#
# Surprise noted:
#    "2026-02-31" passes the date regex because regex only checks the shape of digits (01-31)
#    and does not know calendar rules like February having 28 days.