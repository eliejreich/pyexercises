"""Exercise 7.1 — Loading a file, cleaning it, saving the result (homework)

This is the direct rehearsal for the final exam. Session 8 starts with it.

WHAT THE PROGRAM MUST DO
    Load names.txt, clean what is inside, sort it by last name, and write the result to
    a new file. The original file must not be modified.

DO THIS BEFORE ANYTHING ELSE
    Open names.txt and read it with your eyes. Then write, in comments at the top of
    your file, everything that is wrong with it. There are at least four different
    problems. Find them yourself.

    This step is not optional and it is graded. An assistant cannot see your file.

ANSWER THESE, in comments, after the list of problems
    1. What goes in?
    2. What happens to it?  (one line per problem you found, and how you deal with it)
    3. What comes out?
    4. What does "sort by last name" mean when a line contains two words, and how you
       know which one is the last name?

WHAT THE AI CANNOT KNOW
    The actual content of names.txt. If you paste this brief into an assistant without
    describing the file, it will write a program for a clean file, and that program will
    crash or produce nonsense on the real one.

    Describe the file to it. That description is the exercise.

CHECK IT YOURSELF
    Count the lines in names.txt, then in your output file. The numbers should differ,
    and you should be able to say exactly why. Then check the first and last name of
    your sorted list by hand.

DELIVERABLE
    This file, plus the output file your program produced.
"""

# What is wrong with names.txt (found by reading it, not by guessing):
# - Problem 1: Blank lines (lines 3 and 9 are empty).
# - Problem 2: Leading spaces before some names ("  alan TURING" and "  linus torvalds").
# - Problem 3: Inconsistent casing across names (all lowercase, ALL CAPS last names, and "GUIDO van rossum").
# - Problem 4: One name has three words ("GUIDO van rossum") instead of two, so the last name has two words ("van rossum").

# 1. In:
#    The raw text file `names.txt`, containing 10 lines (8 messy full names and 2 blank lines).
# 2. Process, problem by problem:
#    - Leading/trailing spaces & newlines: Removed from each line using `.strip()`.
#    - Blank lines: Ignored by skipping any line where `clean_line == ""`.
#    - Inconsistent casing: Standardized to Title Case using `.title()` (e.g., "ada LOVELACE" -> "Ada Lovelace").
#    - Sorting by last name (including "Van Rossum"): Each cleaned name is split into words, and a helper function extracts everything from the second word onward (`" ".join(parts[1:])`) as the sort key.
# 3. Out:
#    A new file named `cleaned_names.txt` containing the 8 cleaned names sorted alphabetically by last name, one per line.
# 4. How I decide which word is the last name:
#    Every entry in `names.txt` is written in "FirstName LastName" order. For a two-word name, the first word (index 0) is the first name and the second word (index 1) is the last name. To also handle multi-word last names like "Guido Van Rossum", I treat the first word as the first name and everything after the first word (`parts[1:]`) as the last name.


def get_last_name(full_name):
    """Return the last name portion of a 'First Last' string for sorting."""
    parts = full_name.split()
    return " ".join(parts[1:])


# 1. Load names.txt in read mode ("r")
cleaned_names = []

with open("names.txt", mode="r", encoding="utf-8") as infile:
    for line in infile:
        # Remove leading/trailing whitespace and newline characters
        stripped_line = line.strip()

        # Skip blank lines
        if stripped_line == "":
            continue

        # Standardize capitalization (e.g., "ada LOVELACE" -> "Ada Lovelace")
        formatted_name = stripped_line.title()
        cleaned_names.append(formatted_name)

# 2. Sort the cleaned list alphabetically by last name
sorted_names = sorted(cleaned_names, key=get_last_name)

# 3. Write the result to a new file without modifying names.txt
with open("cleaned_names.txt", mode="w", encoding="utf-8") as outfile:
    for name in sorted_names:
        outfile.write(name + "\n")

print("Done! Saved cleaned and sorted names to cleaned_names.txt.")


# CHECK IT YOURSELF
# - Line count comparison:
#   `names.txt` has 10 lines total (8 names + 2 blank lines).
#   `cleaned_names.txt` has 8 lines total because the 2 blank lines were removed.
# - Hand-check of sorted order by last name:
#   Hamilton, Hopper, Johnson, Liskov, Lovelace, Torvalds, Turing, Van Rossum
#   First name in output file: Margaret Hamilton
#   Last name in output file:  Guido Van Rossum