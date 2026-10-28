"""Exercise 2.1 — Transforming text (homework)

WHAT THE PROGRAM MUST DO
    Ask the user for a sentence, then display four different transformations of it.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. Which four transformations did you choose, and in what situation would each of
       them be useful? One line each.

WHAT THE AI CANNOT KNOW
    Your four transformations. Pick them yourself. Open ../examples/strings/string_methods.py
    to see what is available, then choose, then justify.

    A transformation that produces the same thing as another one does not count as two.

CHECK IT YOURSELF
    Run it with a sentence that has spaces at both ends and a capital in the middle.
    For each of your four results, say in a comment whether it is what you expected.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In:
# 2. Process:
# 3. Out:
# 4. My four transformations, and when each is useful:


# Your code below
# 1. In:
#    A string (a sentence) typed by the user, which may include leading/trailing whitespace, mixed capitalization, or numbers.
# 2. Process:
#    The program repeatedly prompts the user in a while loop until a sentence without digits is provided.
#    It checks for digits using any(c.isdigit() for c in user_sentence). If digits are found, it displays an error
#    and prompts the user to rewrite the sentence. Once valid, it applies four distinct string methods to transform the text.
# 3. Out:
#    An error/re-prompt message whenever numbers are entered, followed eventually by the original valid sentence and its four transformed versions.
# 4. My four transformations, and when each is useful:
#    - strip(): Useful for cleaning up user input by removing accidental leading/trailing spaces before storing or processing.
#    - lower(): Useful for standardizing text so case-insensitive comparisons can be made (e.g., matching search terms or commands).
#    - title(): Useful for formatting titles, headings, or name fields cleanly for display.
#    - replace(" ", "_"): Useful for converting plain text into safe, space-free identifiers such as filenames or URL slugs.


# Loop until the user provides a sentence without numbers
while True:
    user_sentence = input("Please enter a sentence: ")

    # Check if the input contains any numbers
    if any(char.isdigit() for char in user_sentence):
        print("Sorry, we have to put a sentence without numbers. Please rewrite your sentence.\n")
    else:
        break  # Valid input received, exit loop

# Apply four distinct transformations
cleaned = user_sentence.strip()
lowercase = user_sentence.lower()
title_case = user_sentence.title()
snake_style = user_sentence.replace(" ", "_")

# Display results
print("\n--- Results ---")
print("Original:       ", repr(user_sentence))
print("1. strip():     ", repr(cleaned))
print("2. lower():     ", repr(lowercase))
print("3. title():     ", repr(title_case))
print("4. replace():   ", repr(snake_style))


# CHECK IT YOURSELF (Example run)
#
# Attempt 1 (Invalid Input): "I have 2 cats."
# Output: "Sorry, we have to put a sentence without numbers. Please rewrite your sentence."
# Expectation check: Matches expectation — rejected input with numbers and asked to rewrite.
#
# Attempt 2 (Valid Input): "   hello World!   "
# Result 1: 'hello World!'
# Expectation check: Matches expectation — leading and trailing spaces were successfully stripped.
# Result 2: '   hello world!   '
# Expectation check: Matches expectation — all uppercase letters converted to lowercase while maintaining whitespace.
# Result 3: '   Hello World!   '
# Expectation check: Matches expectation — the first letter of each word was capitalized.
# Result 4: '___hello_World!___'
# Expectation check: Matches expectation — every space character was replaced with an underscore.