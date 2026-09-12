from financial_engine import (
    calculate_safe_amount,
    calculate_monthly_surplus,
    calculate_health_score
)


current_balance = 90000
monthly_income = 60000
essential_expenses = 25000
recurring_expenses = 5000
pending_payments = 10000
minimum_balance = 20000


# Calculate Safe Amount
safe_amount = calculate_safe_amount(
    current_balance,
    essential_expenses,
    recurring_expenses,
    pending_payments,
    minimum_balance
)

print("Safe Amount: ₹", safe_amount)


# Calculate Monthly Surplus
monthly_surplus = calculate_monthly_surplus(
    monthly_income,
    essential_expenses,
    recurring_expenses
)

print("Monthly Surplus: ₹", monthly_surplus)


# Calculate Financial Health Score
total_expenses = (
    essential_expenses
    + recurring_expenses
    + pending_payments
)

health_score = calculate_health_score(
    current_balance,
    monthly_income,
    total_expenses,
    minimum_balance
)

print("Financial Health Score:", health_score, "%")