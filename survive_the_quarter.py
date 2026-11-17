 # First and last name: Elie Jreich
# Group: A
#
# 1. What goes in?
# The file scenarios_A.csv uses commas as separators and has 14 columns:
# ID, Scenario, OptionA/B/C, BudgetA/B/C, ReputationA/B/C, and FeedbackA/B/C.
# Budget and reputation values are positive or negative integers.
#
# 2. What happens each day?
# First, display the day number, current budget, and current reputation.
# Second, show the scenario and options A, B, and C.
# Third, ask the player for A, B, or C until the input is valid.
# Fourth, update budget and reputation, cap reputation at 100, and show feedback.
# Fifth, stop the game right away if budget or reputation is 0 or less.
#
# 3. What comes out?
# At the end, print whether the player is fired or their final title and score,
# plus the best and worst reputation moves, and append one line to results.csv
# with: name, budget, reputation, title, date.
#
# 4. What could go wrong?
# - Wrong key typed: keep asking until the player enters A, B, or C.
# - Gauge drops to 0 or below: break out of the loop immediately (Fired).
# - Missing scenario file: catch FileNotFoundError and print a clear message.
#
# Mandatory feature chosen: b (The algorithm)
# On one random day out of 10, the reputation change is doubled.
# I chose this feature because it adds surprise and forces the player to adapt.

import csv
import random
from datetime import date


# Load all scenarios from scenarios_A.csv and store each option as a tuple
def load_scenarios(filename):
    scenarios = []
    with open(filename, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            options = {
                "A": (row["OptionA"], int(row["BudgetA"]), int(row["ReputationA"]), row["FeedbackA"]),
                "B": (row["OptionB"], int(row["BudgetB"]), int(row["ReputationB"]), row["FeedbackB"]),
                "C": (row["OptionC"], int(row["BudgetC"]), int(row["ReputationC"]), row["FeedbackC"]),
            }
            scenarios.append({
                "situation": row["Scenario"],
                "options": options
            })
    return scenarios


# Ask the player for A, B, or C until they type a valid letter
def ask_choice():
    while True:
        choice = input("Your choice (A, B or C): ").strip().upper()
        if choice in ("A", "B", "C"):
            return choice
        print("Please type A, B or C:")


# Apply the selected option and return the updated (budget, reputation) tuple
def apply_choice(budget, reputation, option, multiplier):
    text, budget_change, reputation_change, feedback = option
    budget = budget + budget_change
    reputation = reputation + (reputation_change * multiplier)
    if reputation > 100:
        reputation = 100
    return budget, reputation


# Return the player's final title based on gauges and score
def get_title(budget, reputation):
    if budget <= 0 or reputation <= 0:
        return "Fired", 0
    score = reputation + budget // 200
    if score < 95:
        return "Eternal Intern", score
    elif score < 120:
        return "Growth Hacker", score
    elif score < 140:
        return "CMO Material", score
    else:
        return "Viral Legend", score


# Append one completed game to results.csv
def save_result(name, budget, reputation, title):
    with open("results.csv", mode="a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([name, budget, reputation, title, date.today().isoformat()])


# Main game loop
def play_game():
    try:
        scenarios = load_scenarios("scenarios_A.csv")
    except FileNotFoundError:
        print("Error: scenarios_A.csv was not found.")
        return

    name = input("Enter your name: ").strip()
    random.shuffle(scenarios)

    budget = 10000
    reputation = 50
    history = []
    algorithm_day = random.randint(1, 10)

    for day in range(1, 11):
        scenario = scenarios[day - 1]
        print(f"\nDay {day}")
        print(f"[Budget: {budget} EUR | Reputation: {reputation}/100]")
        print(scenario["situation"])
        print(f"A: {scenario['options']['A'][0]}")
        print(f"B: {scenario['options']['B'][0]}")
        print(f"C: {scenario['options']['C'][0]}")

        multiplier = 2 if day == algorithm_day else 1
        if multiplier == 2:
            print("THE ALGORITHM: Reputation change is doubled today!")

        choice = ask_choice()
        chosen_option = scenario["options"][choice]
        old_rep = reputation

        budget, reputation = apply_choice(budget, reputation, chosen_option, multiplier)
        rep_diff = reputation - old_rep

        print(chosen_option[3])
        print(f"Budget {chosen_option[1]:+d} EUR, Reputation {rep_diff:+d}")

        history.append((rep_diff, day, chosen_option[0]))

        if budget <= 0 or reputation <= 0:
            break

    print("=" * 30)
    title, score = get_title(budget, reputation)

    if title == "Fired":
        if budget <= 0 and reputation <= 0:
            print("You are fired! Both your budget and reputation hit zero.")
        elif budget <= 0:
            print("You are fired! Your budget hit zero.")
        else:
            print("You are fired! Your reputation hit zero.")
    else:
        print("Quarter survived!")
        print(f"Budget left: {budget} EUR, reputation: {reputation}/100")
        print(f"Final score: {score}")

    print(f"{name}, your title: {title}")

    best_move = max(history)
    worst_move = min(history)
    print(f'Best move: day {best_move[1]}, "{best_move[2]}" ({best_move[0]:+d})')
    print(f'Worst move: day {worst_move[1]}, "{worst_move[2]}" ({worst_move[0]:+d})')

    save_result(name, budget, reputation, title)
    print("Saved in results.csv")


play_game()