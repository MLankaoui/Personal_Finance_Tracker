#!/usr/bin/python3
from handleinput import *

def main():
    print('Welcome to Personal Finance Tracker')
    print('Please enter your expenses')

    user_expenses = expenses()
    print('So your expenses are: ')
    display_expenses(user_expenses)

def display_expenses(user_expenses):
    for expense in user_expenses:
        print(expense)

main()
