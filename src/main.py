#!/usr/bin/python3

from handleinput import expenses, calculate_monthly_expenses, calculate_monthly_income, income

def main():
    print('Welcome to Personal Finance Tracker')
    
    # Predefined categories for expenses and income
    expense_categories = ["Food", "Housing", "Transportation", "Utilities", "Entertainment"]
    income_categories = ["Salary", "Freelance", "Investments", "Rental Income", "Other"]

    expenses_by_category = {}  # Empty dictionary to store expenses by category
    earnings_by_category = {}  # Empty dictionary to store earnings by category
    
    # Prompt user to select categories until all predefined categories are used
    while expense_categories:
        print("\nExpense Categories:")
        for index, category in enumerate(expense_categories, start=1):
            print(f"{index}. {category}")
        
        # Prompt for selecting expense category
        choice = input("Select an expense category number (or type 'done' to finish): ").strip()
        if choice.lower() == 'done':
            break
        
        try:
            choice_index = int(choice) - 1
            if 0 <= choice_index < len(expense_categories):
                category = expense_categories.pop(choice_index)
            else:
                raise ValueError
        except ValueError:
            print("Invalid choice. Please select a valid category number.")
            continue
        
        # Input expenses for the selected category
        print(f'Please enter your expenses for {category}')
        expenses_by_category[category] = expenses()
    
    # Prompt user to select income categories until all predefined categories are used
    while income_categories:
        print("\nIncome Categories:")
        for index, category in enumerate(income_categories, start=1):
            print(f"{index}. {category}")
        
        # Prompt for selecting income category
        choice = input("Select an income category number (or type 'done' to finish): ").strip()
        if choice.lower() == 'done':
            break
        
        try:
            choice_index = int(choice) - 1
            if 0 <= choice_index < len(income_categories):
                category = income_categories.pop(choice_index)
            else:
                raise ValueError
        except ValueError:
            print("Invalid choice. Please select a valid category number.")
            continue
        
        # Input earnings for the selected category
        print(f'Please enter your earnings for {category}')
        earnings_by_category[category] = income()

    print('\nYour financial details by category:')
    print('----------------------------------')
    
    # Display expenses by category
    print('Expenses:')
    for category, category_expenses in expenses_by_category.items():
        print(f'{category}:')
        display_expenses(category_expenses)
    print(f'Total expenses: {calculate_monthly_expenses(expenses_by_category)}')
    
    # Display earnings by category
    print('\nEarnings:')
    for category, category_earnings in earnings_by_category.items():
        print(f'{category}:')
        display_income(category_earnings)
    print(f'Total earnings: {calculate_monthly_income(earnings_by_category)}')

def display_expenses(expenses_dict):
    for item, amount in expenses_dict.items():
        print(f'- {item}: {amount}')

def display_income(income_dict):
    for item, amount in income_dict.items():
        print(f'- {item}: {amount}')

if __name__ == "__main__":
    main()
