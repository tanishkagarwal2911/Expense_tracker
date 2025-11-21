# expense_tracker.py

import csv
import os
from datetime import datetime

# File to store expenses
FILE_NAME = "expenses.csv"

# Ensure the CSV file exists
if not os.path.exists(FILE_NAME):
    with open(FILE_NAME, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Date", "Category", "Amount", "Description"])

# Function to add an expense
def add_expense():
    date = input("Enter date (YYYY-MM-DD) or press Enter for today: ")
    if not date:
        date = datetime.today().strftime("%Y-%m-%d")
    category = input("Enter category (Food, Travel, Bills, etc.): ")
    amount = float(input("Enter amount: "))
    description = input("Enter description: ")

    with open(FILE_NAME, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount, description])
    print("Expense added successfully!\n")

# Function to view all expenses
def view_expenses():
    print("\n=== All Expenses ===")
    with open(FILE_NAME, mode='r') as file:
        reader = csv.reader(file)
        next(reader)  # skip header
        expenses = list(reader)
        if not expenses:
            print("No expenses found.")
            return
        total = 0
        for row in expenses:
            print(f"Date: {row[0]}, Category: {row[1]}, Amount: ₹{row[2]}, Description: {row[3]}")
            total += float(row[2])
        print(f"\nTotal Expenses: ₹{total}\n")

# Function to view summary by category
def summary_by_category():
    print("\n=== Expense Summary by Category ===")
    with open(FILE_NAME, mode='r') as file:
        reader = csv.reader(file)
        next(reader)  # skip header
        summary = {}
        for row in reader:
            category = row[1]
            amount = float(row[2])
            summary[category] = summary.get(category, 0) + amount
        if not summary:
            print("No expenses found.")
            return
        for category, amount in summary.items():
            print(f"{category}: ₹{amount}")
        print()

# Main menu
def menu():
    while True:
        print("=== Mini Expense Tracker ===")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Summary by Category")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")
        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            summary_by_category()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please select 1-4.\n")

if __name__ == "__main__":
    menu()
