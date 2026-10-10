import json
from pathlib import Path

DATA_FILES = Path(__file__).with_name("Expense.json")

class Tracker:
    """Manage expenses for a simple command-line expense tracker."""

    def __init__(self):
        # Each expense is stored as a dictionary inside this list.
        self.trackers = []
        self.load_data()

    def save_data(self):
        with DATA_FILES.open("w", encoding="utf-8") as file:
            json.dump(self.trackers, file, indent=4)

    def load_data(self):
        if not DATA_FILES.exists():
            self.trackers = []
            return

        try:
            with DATA_FILES.open("r", encoding="utf-8") as file:
                saved_data = json.load(file)

            if isinstance(saved_data, list):
                self.trackers = saved_data
            else:
                print("Invalid expense data. Starting with an empty list.")
                self.trackers = []

        except (json.JSONDecodeError, OSError):
            print("Could not load saved expenses. Starting with an empty list.")
            self.trackers = []

    def menu(self):
        """Display the menu and run the user's selected action."""
        print(
            "\nWelcome to Expense Tracker\n"
            "1. Add Expense\n"
            "2. View Expenses\n"
            "3. Total Amount Spent\n"
            "4. Search Expense by Name\n"
            "5. Exit"
        )

        try:
            user = int(input("Enter your choice: ").strip())
        except ValueError:
            print("Please enter a number from 1 to 5.")
            return True

        if user == 1:
            self.expense_add()
        elif user == 2:
            self.view_expense()
        elif user == 3:
            self.add_amount()
        elif user == 4:
            self.search_expense()
        elif user == 5:
            print("Thank you for using Expense Tracker. Goodbye!")
            return False
        else:
            print("Invalid choice. Please choose a number from 1 to 5.")

        return True

    def expense_add(self):
        """Collect and save one expense."""
        category = input("Enter expense category: ").strip().title()
        while not category:
            print("Category cannot be empty.")
            category = input("Enter expense category: ").strip().title()

        name = input("Enter expense name: ").strip().title()
        while not name:
            print("Expense name cannot be empty.")
            name = input("Enter expense name: ").strip().title()

        while True:
            try:
                amount = float(input("Enter expense amount: $").strip())
                if amount <= 0:
                    print("Expense amount must be greater than zero.")
                    continue
                break
            except ValueError:
                print("Please enter a valid number, such as 150 or 12.50.")

        self.storing_expense(category=category, name=name, amount=amount)
        print("Expense added successfully.")

    def storing_expense(self, category, name, amount):
        """Store one complete expense record."""
        details = {
            "category": category,
            "name": name,
            "amount": amount,
        }
        self.trackers.append(details)
        self.save_data()

    def add_amount(self):
        """Calculate and display the total of all recorded expenses."""
        if not self.trackers:
            print("No expenses have been recorded yet.")
            return 0

        amount = 0.0
        for expense in self.trackers:
            amount += expense["amount"]

        print(f"Total amount spent: ${amount:.2f}")
        return amount

    def view_expense(self):
        """Display all recorded expenses."""
        if not self.trackers:
            print("No expenses have been recorded yet.")
            return

        print("\n--- Your Expenses ---")
        for number, expense in enumerate(self.trackers, start=1):
            print(f"\nExpense #{number}")
            print(f"  Category: {expense['category']}")
            print(f"  Name:     {expense['name']}")
            print(f"  Amount:   ${expense['amount']:.2f}")

    def search_expense(self):
        """Search for expenses by name, ignoring letter case."""
        if not self.trackers:
            print("No expenses have been recorded yet.")
            return

        search_name = input("Enter the expense name to search: ").strip().casefold()
        if not search_name:
            print("Expense name cannot be empty.")
            return

        found = False
        for expense in self.trackers:
            if expense["name"].casefold() == search_name:
                print("\nExpense found:")
                print(f"  Category: {expense['category']}")
                print(f"  Name:     {expense['name']}")
                print(f"  Amount:   ${expense['amount']:.2f}")
                found = True

        if not found:
            print(f"No expense found matching '{search_name}'.")
