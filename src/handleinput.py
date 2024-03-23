def expenses():
    user_expenses = input('Enter your monthly expenses')
    user_expenses = float(user_expenses)
    user_expenses = user_expenses.split(' ')

    return (user_expenses)


def income():
    user_income = input('Enter your monthly earnings')
    user_income = float(user_income)
    user_income = user_income.split(' ')

    return (user_income)

def calculate_monthly_expenses():
    user_expenses = expenses()
    user_expenses = user_expenses.split(' ')
    result = 0
    
    for element in user_expenses:
        element = float(element)
        result += element


    return (result)

def calculate_monthly_income():
    user_income = income()
    user_income = user_income.split(' ')
    result = 0
    
    for element in user_income:
        element = float(element)
        result += element


    return (result)