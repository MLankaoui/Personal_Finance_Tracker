def expenses():
    user_expenses = input('Enter your monthly expenses: ')
    user_expenses = user_expenses.split(' ')
    user_expenses = [float(expense) for expense in user_expenses]
    return user_expenses

def income():
    user_income = input('Enter your monthly earnings: ')
    user_income = user_income.split(' ')
    user_income = [float(earnings) for earnings in user_income]
    return user_income

def calculate_monthly_expenses(user_expenses):
    result = sum(user_expenses)
    return result

def calculate_monthly_income(user_income):
    result = sum(user_income)
    return result


