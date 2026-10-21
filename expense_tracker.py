"""Simple Expense Tracker
Saves expenses in a file (expenses.json) so data stays after you close the program.
"""

import json
import os
from datetime import date

FILE_NAME = "expenses.json"


def load_expenses():
    """File theke purono expense gulo load kore. File na thakle empty list dey."""
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r") as f:
        return json.load(f)


def save_expenses(expenses):
    """Expense list ta file-e save kore."""
    with open(FILE_NAME, "w") as f:
        json.dump(expenses, f, indent=4)


def add_expense(expenses):
    title = input("Ki-r jonno kharoch? ")
    try:
        amount = float(input("Koto taka? "))
    except ValueError:
        print("Taka-r jaygay shudhu number likho.\n")
        return
    category = input("Category (food/transport/study/other): ")

    expense = {
        "title": title,
        "amount": amount,
        "category": category,
        "date": str(date.today()),
    }
    expenses.append(expense)
    save_expenses(expenses)
    print("Expense add hoyeche!\n")


def view_expenses(expenses):
    if not expenses:
        print("Kono expense nai.\n")
        return
    print("\n--- Shob Expense ---")
    for i, e in enumerate(expenses, start=1):
        print(f"{i}. {e['date']} | {e['title']} | {e['category']} | {e['amount']} taka")
    print()


def show_total(expenses):
    total = sum(e["amount"] for e in expenses)
    print(f"\nMot kharoch: {total} taka")

    # Category onujayi total
    by_category = {}
    for e in expenses:
        by_category[e["category"]] = by_category.get(e["category"], 0) + e["amount"]
    for category, amount in by_category.items():
        print(f"  {category}: {amount} taka")
    print()


def delete_expense(expenses):
    view_expenses(expenses)
    if not expenses:
        return
    try:
        number = int(input("Koto number expense delete korbe? "))
        removed = expenses.pop(number - 1)
    except (ValueError, IndexError):
        print("Vul number.\n")
        return
    save_expenses(expenses)
    print(f"'{removed['title']}' delete hoyeche.\n")


def main():
    expenses = load_expenses()

    while True:
        print("=== Expense Tracker ===")
        print("1. Expense add koro")
        print("2. Shob expense dekho")
        print("3. Total dekho")
        print("4. Expense delete koro")
        print("5. Exit")
        choice = input("Tomar choice: ")

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            show_total(expenses)
        elif choice == "4":
            delete_expense(expenses)
        elif choice == "5":
            print("Bye!")
            break
        else:
            print("1 theke 5-er moddhe choose koro.\n")


if __name__ == "__main__":
    main()
