#!/usr/bin/python3
from handleinput import expenses, calculate_monthly_expenses, calculate_monthly_income, income

def main():
    print('Welcome to Personal Finance Tracker')
    print('Please enter your expenses')

    user_expenses = expenses()
    print('So your expenses are: ')
    display_expenses(user_expenses)
    print(f'Total amount of {calculate_monthly_expenses(user_expenses=user_expenses)}')
    print('Please enter your earnings')
    user_earnings = income()
    print('So your earnings are: ')
    display_income(user_earnings)
    print(f'Total amount of {calculate_monthly_income(user_earnings)}')

def display_expenses(user_expenses):
    for expense in user_expenses:
        print(expense)
def display_income(user_earnings):
    for earnings in user_earnings:
        print(earnings)
main()
