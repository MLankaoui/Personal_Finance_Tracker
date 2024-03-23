def expenses():
    user_expenses = input('Enter your expenses')
    user_expenses = float(user_expenses)
    user_expenses = user_expenses.split(' ')

    return user_expenses


def income():
    user_income = input('Enter your monthly earnings')
    user_income = float(user_income)
    user_income = user_income.split(' ')

    return user_income